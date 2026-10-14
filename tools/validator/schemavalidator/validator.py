from __future__ import annotations

import copy
import json
from pathlib import Path
import re
from typing import Any, Dict, List, Optional, Tuple

import jsonschema
from jsonschema import Draft202012Validator

from .report import ValidationError, ValidationReport, ValidationWarning

# Default schema bundled within the package
DEFAULT_SCHEMA_PATH = Path(__file__).resolve().parent / "schema.json"
_CACHED_SCHEMA: Optional[Dict[str, Any]] = None
_CACHED_VALIDATOR: Optional[Draft202012Validator] = None


def load_schema(schema_path: Optional[Path | str] = None) -> Dict[str, Any]:
    global _CACHED_SCHEMA, _CACHED_VALIDATOR
    if schema_path is None:
        if _CACHED_SCHEMA is not None:
            return _CACHED_SCHEMA
        path = DEFAULT_SCHEMA_PATH
    else:
        path = Path(schema_path)

    with open(path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    if schema_path is None:
        _CACHED_SCHEMA = schema
        _CACHED_VALIDATOR = Draft202012Validator(schema)
    return schema


def get_default_validator() -> Draft202012Validator:
    global _CACHED_VALIDATOR
    if _CACHED_VALIDATOR is None:
        schema = load_schema()
        _CACHED_VALIDATOR = Draft202012Validator(schema)
    return _CACHED_VALIDATOR


def _extract_field_path(e: jsonschema.exceptions.ValidationError) -> Tuple[str, str]:
    """Returns (field_path, missing_prop_if_required)"""
    base_path = ".".join(str(p) for p in e.absolute_path)
    missing_prop = ""

    if e.validator == "required":
        m = re.search(r"'([^']+)' is a required property", e.message)
        if m:
            missing_prop = m.group(1)
        elif isinstance(e.validator_value, list) and len(e.validator_value) == 1:
            missing_prop = e.validator_value[0]

        if missing_prop:
            full_path = f"{base_path}.{missing_prop}" if base_path else missing_prop
            return full_path, missing_prop
    return base_path or "root", missing_prop


def _format_error(
    e: jsonschema.exceptions.ValidationError, record: Dict[str, Any]
) -> ValidationError:
    field_path, missing_prop = _extract_field_path(e)
    conformance_level = record.get("conformance_level")

    # Check for conformance layer requirement errors triggered by allOf
    schema_path_str = "/".join(str(p) for p in e.schema_path)
    if "allOf" in schema_path_str and e.validator == "required":
        if missing_prop in ("facilities", "process_capability", "reliability", "commercial"):
            return ValidationError(
                field_path=field_path,
                message_en=(
                    f"Conformance level '{conformance_level}' requires layer '{missing_prop}', "
                    "but it is missing."
                ),
                message_zh=(
                    f"合规等级 '{conformance_level}' 要求包含 '{missing_prop}' 模块层，"
                    "但该模块缺失。"
                ),
                rule=f"conformance_level({conformance_level}).required({missing_prop})",
            )

    if e.validator == "required":
        prop_name = missing_prop or field_path.split(".")[-1]
        return ValidationError(
            field_path=field_path,
            message_en=f"Property '{prop_name}' is required but missing.",
            message_zh=f"必填属性 '{prop_name}' 缺失。",
            rule="required",
        )
    elif e.validator == "enum":
        allowed = e.validator_value
        return ValidationError(
            field_path=field_path,
            message_en=f"Value {json.dumps(e.instance)} is not allowed. Expected one of: {allowed}",
            message_zh=f"值 {json.dumps(e.instance)} 不在合法的枚举列表中。允许的选项为: {allowed}",
            rule=f"enum({allowed})",
        )
    elif e.validator == "type":
        exp = e.validator_value
        actual = type(e.instance).__name__
        return ValidationError(
            field_path=field_path,
            message_en=f"Expected type '{exp}', got '{actual}'.",
            message_zh=f"期望的数据类型为 '{exp}'，但实际传入类型为 '{actual}'。",
            rule=f"type({exp})",
        )
    elif e.validator == "additionalProperties":
        return ValidationError(
            field_path=field_path,
            message_en=f"Unrecognized additional property: {e.message}",
            message_zh=f"发现未在规范中定义的额外字段: {e.message}",
            rule="additionalProperties",
        )
    elif e.validator == "minItems":
        return ValidationError(
            field_path=field_path,
            message_en=f"Array must contain at least {e.validator_value} items (found {len(e.instance)}).",
            message_zh=f"数组至少需要包含 {e.validator_value} 项（当前包含 {len(e.instance)} 项）。",
            rule=f"minItems({e.validator_value})",
        )
    elif e.validator == "minLength":
        return ValidationError(
            field_path=field_path,
            message_en=f"String must have minimum length of {e.validator_value}.",
            message_zh=f"字符串长度不能少于 {e.validator_value} 个字符。",
            rule=f"minLength({e.validator_value})",
        )
    elif e.validator == "format":
        return ValidationError(
            field_path=field_path,
            message_en=f"Value {json.dumps(e.instance)} does not match format '{e.validator_value}'.",
            message_zh=f"值 {json.dumps(e.instance)} 不符合 '{e.validator_value}' 格式要求。",
            rule=f"format({e.validator_value})",
        )
    else:
        return ValidationError(
            field_path=field_path,
            message_en=e.message,
            message_zh=f"校验未通过: {e.message}",
            rule=str(e.validator),
        )


def _collect_tiers(obj: Any) -> List[str]:
    """Recursively collect all provenance.tier values in the record."""
    tiers: List[str] = []
    if isinstance(obj, dict):
        if "tier" in obj and isinstance(obj["tier"], str):
            tiers.append(obj["tier"])
        for v in obj.values():
            tiers.extend(_collect_tiers(v))
    elif isinstance(obj, list):
        for item in obj:
            tiers.extend(_collect_tiers(item))
    return tiers


def _check_warnings(
    record: Dict[str, Any], conformance_target: Optional[str]
) -> List[ValidationWarning]:
    warnings: List[ValidationWarning] = []
    tiers = _collect_tiers(record)
    total_tiers = len(tiers)
    if total_tiers == 0:
        return warnings

    synthetic_count = sum(1 for t in tiers if t == "synthetic")
    synthetic_ratio = synthetic_count / total_tiers

    # Warning rule: L3 record where >50% of values are synthetic tier
    if conformance_target == "L3" and synthetic_ratio > 0.5:
        pct = synthetic_ratio * 100.0
        warnings.append(
            ValidationWarning(
                field_path="provenance.tier",
                message_en=(
                    f"Low-confidence record: {synthetic_count}/{total_tiers} ({pct:.1f}%) "
                    "spec values use 'synthetic' tier, exceeding the 50% warning threshold for L3 conformance."
                ),
                message_zh=(
                    f"低置信度记录：共有 {synthetic_count}/{total_tiers} ({pct:.1f}%) "
                    "个规格值使用 'synthetic'（合成占位）层级，超过了 L3 合规等级 50% 的置信度告警线。"
                ),
                rule="low_confidence_synthetic_ratio",
            )
        )
    return warnings


def detect_highest_conformance(
    record: Dict[str, Any], validator: Draft202012Validator
) -> Optional[str]:
    """
    Detect the highest conformance level (L1, L2, L3) that the record actually satisfies.
    """
    highest: Optional[str] = None
    for level in ["L1", "L2", "L3"]:
        test_rec = copy.deepcopy(record)
        test_rec["conformance_level"] = level
        if validator.is_valid(test_rec):
            highest = level
        else:
            break
    return highest


def validate_record(
    record: Dict[str, Any],
    schema: Optional[Dict[str, Any]] = None,
    schema_path: Optional[Path | str] = None,
) -> ValidationReport:
    """
    Validate an equipment record against SemiconFab Equipment Schema v1.0.

    Args:
        record: The equipment record dict.
        schema: Optional parsed schema dict.
        schema_path: Optional path to schema.json.

    Returns:
        ValidationReport with errors, warnings, conformance level, and bilingual summaries.
    """
    if schema is not None:
        validator = Draft202012Validator(schema)
    elif schema_path is not None:
        parsed_schema = load_schema(schema_path)
        validator = Draft202012Validator(parsed_schema)
    else:
        validator = get_default_validator()

    conformance_target = record.get("conformance_level") if isinstance(record, dict) else None

    # Collect structural errors
    raw_errors = list(validator.iter_errors(record))
    errors: List[ValidationError] = []
    for e in raw_errors:
        errors.append(_format_error(e, record))

    is_valid = len(errors) == 0

    # Collect warnings (non-fatal)
    warnings = _check_warnings(record, conformance_target)

    # Detect highest satisfied conformance level
    conformance_detected = detect_highest_conformance(record, validator)

    # Build bilingual summaries
    err_count = len(errors)
    warn_count = len(warnings)
    if is_valid:
        summary_en = (
            f"Record is valid. Conformance level: {conformance_target} "
            f"(detected: {conformance_detected}). {err_count} errors, {warn_count} warning(s)."
        )
        summary_zh = (
            f"记录校验通过。目标合规等级：{conformance_target} "
            f"（检测达标：{conformance_detected}）。{err_count} 项错误，{warn_count} 项告警。"
        )
    else:
        detected_str = conformance_detected or "None"
        summary_en = (
            f"Record is invalid: {err_count} error(s), {warn_count} warning(s). "
            f"Target: {conformance_target}, detected: {detected_str}."
        )
        summary_zh = (
            f"记录校验未通过：发现 {err_count} 项错误，{warn_count} 项告警。"
            f"目标等级：{conformance_target}，实际达标等级：{detected_str}。"
        )

    return ValidationReport(
        is_valid=is_valid,
        errors=errors,
        warnings=warnings,
        conformance_detected=conformance_detected,
        conformance_target=conformance_target,
        summary_en=summary_en,
        summary_zh=summary_zh,
    )
