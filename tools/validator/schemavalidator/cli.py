from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import List, Optional

from .validator import load_schema, validate_record


def validate_file(
    file_path: Path, lang: str = "en", schema_path: Optional[str] = None
) -> int:
    is_zh = lang == "zh"
    if not file_path.exists():
        msg = f"错误: 文件不存在 '{file_path}'" if is_zh else f"Error: File not found '{file_path}'"
        print(msg, file=sys.stderr)
        return 1

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        msg = (
            f"错误: 无法解析 JSON 文件 '{file_path}': {exc}"
            if is_zh
            else f"Error: Failed to parse JSON file '{file_path}': {exc}"
        )
        print(msg, file=sys.stderr)
        return 1
    except Exception as exc:
        msg = (
            f"错误: 读取文件 '{file_path}' 失败: {exc}"
            if is_zh
            else f"Error: Failed to read file '{file_path}': {exc}"
        )
        print(msg, file=sys.stderr)
        return 1

    schema = load_schema(schema_path) if schema_path else None
    report = validate_record(data, schema=schema)

    print(report.format_report(lang=lang))
    return 0 if report.is_valid else 1


def validate_directory(
    dir_path: Path, lang: str = "en", schema_path: Optional[str] = None
) -> int:
    is_zh = lang == "zh"
    if not dir_path.is_dir():
        msg = (
            f"错误: 目录不存在 '{dir_path}'"
            if is_zh
            else f"Error: Directory not found '{dir_path}'"
        )
        print(msg, file=sys.stderr)
        return 1

    json_files = sorted(list(dir_path.glob("*.json")))
    if not json_files:
        msg = (
            f"提示: 目录 '{dir_path}' 中未找到 .json 文件"
            if is_zh
            else f"Notice: No .json files found in '{dir_path}'"
        )
        print(msg)
        return 0

    schema = load_schema(schema_path) if schema_path else None
    rows: List[tuple[str, str, str, int, int]] = []
    any_invalid = False

    for file_path in json_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            report = validate_record(data, schema=schema)
            valid_str = ("通过" if is_zh else "VALID") if report.is_valid else ("失败" if is_zh else "INVALID")
            conf_str = report.conformance_detected or "-"
            if not report.is_valid:
                any_invalid = True
            rows.append((file_path.name, valid_str, conf_str, len(report.errors), len(report.warnings)))
        except Exception:
            any_invalid = True
            rows.append((file_path.name, "ERROR", "-", 1, 0))

    # Print Table
    header_file = "文件名" if is_zh else "File"
    header_valid = "状态" if is_zh else "Valid"
    header_conf = "达标等级" if is_zh else "Conformance"
    header_errs = "错误数" if is_zh else "#Errors"
    header_warns = "告警数" if is_zh else "#Warnings"

    w_file = max(len(header_file), max(len(r[0]) for r in rows))
    w_valid = max(len(header_valid), max(len(r[1]) for r in rows))
    w_conf = max(len(header_conf), max(len(r[2]) for r in rows))
    w_errs = max(len(header_errs), 7)
    w_warns = max(len(header_warns), 9)

    header_line = (
        f"{header_file:<{w_file}} | {header_valid:<{w_valid}} | "
        f"{header_conf:<{w_conf}} | {header_errs:>{w_errs}} | {header_warns:>{w_warns}}"
    )
    sep_line = (
        f"{'-'*w_file}-+-{'-'*w_valid}-+-{'-'*w_conf}-+-{'-'*w_errs}-+-{'-'*w_warns}"
    )

    print(header_line)
    print(sep_line)
    for r in rows:
        print(f"{r[0]:<{w_file}} | {r[1]:<{w_valid}} | {r[2]:<{w_conf}} | {r[3]:>{w_errs}} | {r[4]:>{w_warns}}")

    total_msg = (
        f"\n总计: {len(rows)} 个文件，{'存在无效记录' if any_invalid else '全部校验通过'}。"
        if is_zh
        else f"\nTotal: {len(rows)} files, {'Some records INVALID' if any_invalid else 'All records VALID'}."
    )
    print(total_msg)
    return 1 if any_invalid else 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="schemavalidator",
        description="SemiconFab Equipment Schema v1.0 Validator CLI",
    )
    subparsers = parser.add_subparsers(dest="command")

    # validate subcommand
    p_validate = subparsers.add_parser("validate", help="Validate a single JSON equipment record")
    p_validate.add_argument("file", type=str, help="Path to JSON record file")
    p_validate.add_argument(
        "--lang", choices=["en", "zh"], default="en", help="Language for error messages (default: en)"
    )
    p_validate.add_argument("--schema", type=str, default=None, help="Custom path to schema.json")

    # validate-dir subcommand
    p_vdir = subparsers.add_parser("validate-dir", help="Validate all JSON files in a directory")
    p_vdir.add_argument("dir", type=str, help="Directory containing JSON records")
    p_vdir.add_argument(
        "--lang", choices=["en", "zh"], default="en", help="Language for output (default: en)"
    )
    p_vdir.add_argument("--schema", type=str, default=None, help="Custom path to schema.json")

    # Fallback positional argument if user runs `schemavalidator <file.json>` directly
    parser.add_argument("fallback_file", nargs="?", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--lang", choices=["en", "zh"], default="en", help="Language (default: en)")
    parser.add_argument("--schema", type=str, default=None, help="Custom path to schema.json")

    args = parser.parse_args(argv)

    if args.command == "validate":
        return validate_file(Path(args.file), lang=args.lang, schema_path=args.schema)
    elif args.command == "validate-dir":
        return validate_directory(Path(args.dir), lang=args.lang, schema_path=args.schema)
    elif args.fallback_file:
        fallback_path = Path(args.fallback_file)
        if fallback_path.is_dir():
            return validate_directory(fallback_path, lang=args.lang, schema_path=args.schema)
        else:
            return validate_file(fallback_path, lang=args.lang, schema_path=args.schema)
    else:
        parser.print_help()
        return 2


if __name__ == "__main__":
    sys.exit(main())
