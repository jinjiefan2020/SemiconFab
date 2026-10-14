#!/usr/bin/env python3
"""
build_catalog.py — SemiconFab Equipment Catalog Data Pipeline
Reads unzipped migration output records, validates against schema.json,
and generates normalized catalog.json and catalog-index.json.
"""

from __future__ import annotations

import argparse
from collections import Counter
import copy
import json
import os
from pathlib import Path
import sys
from typing import Any, Dict, List, Optional, Tuple
import urllib.parse

try:
    import jsonschema
    from jsonschema import Draft202012Validator
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

# The 8 L1 required fields according to Schema v1.0 specification
L1_REQUIRED_FIELDS = [
    ("meta.submitted_by", lambda r: bool(r.get("submitted_by") or (r.get("meta") and r["meta"].get("submitted_by")))),
    ("identity.vendor", lambda r: bool(r.get("identity", {}).get("vendor", {}).get("value"))),
    ("identity.model", lambda r: bool(r.get("identity", {}).get("model", {}).get("value"))),
    ("identity.category", lambda r: bool(r.get("identity", {}).get("category", {}).get("value"))),
    ("identity.wafer_sizes_mm", lambda r: bool(r.get("identity", {}).get("wafer_sizes_mm", {}).get("value"))),
    ("physical.width_mm", lambda r: bool(r.get("physical", {}).get("width_mm", {}).get("value"))),
    ("physical.depth_mm", lambda r: bool(r.get("physical", {}).get("depth_mm", {}).get("value"))),
    ("physical.height_mm", lambda r: bool(r.get("physical", {}).get("height_mm", {}).get("value"))),
]

VALID_TIERS = {
    "vendor_confirmed",
    "independent_verified",
    "community_corroborated",
    "inferred",
    "synthetic",
}


def find_schema(search_dirs: List[Path]) -> Optional[Dict[str, Any]]:
    """Locate and load schema.json from common candidate paths."""
    candidates = [
        Path("schema.json"),
        Path("./schema.json"),
        Path("../schema.json"),
        Path("tools/validator/schemavalidator/schema.json"),
        Path("../tools/validator/schemavalidator/schema.json"),
    ]
    for d in search_dirs:
        candidates.append(d / "schema.json")
        candidates.append(d / ".." / "schema.json")

    for p in candidates:
        if p.exists() and p.is_file():
            try:
                with open(p, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[WARN] Failed to load schema from {p}: {e}", file=sys.stderr)
    return None


def extract_tier_summary(data: Any) -> Dict[str, int]:
    """Recursively search for provenance tiers and return count summary."""
    summary: Dict[str, int] = {t: 0 for t in VALID_TIERS}

    def _walk(node: Any):
        if isinstance(node, dict):
            if "provenance" in node and isinstance(node["provenance"], dict):
                t = node["provenance"].get("tier")
                if t in summary:
                    summary[t] += 1
                elif t:
                    summary[str(t)] = summary.get(str(t), 0) + 1
            for v in node.values():
                _walk(v)
        elif isinstance(node, list):
            for item in node:
                _walk(item)

    _walk(data)
    # Remove tiers with 0 occurrences or keep full tier map?
    # Spec says: "tier_summary ({tier: count} across all values)"
    return {k: v for k, v in summary.items() if v > 0}


def discover_record_files(target_dir: Path) -> List[Path]:
    """Find all equipment record JSON files in target directory."""
    files: List[Path] = []
    
    # Priority subdirectories
    subdirs = ["records", "needs_footprint", "output/records", "output/needs_footprint", "out/records", "out/needs_footprint"]
    found_subdirs = False
    for sub in subdirs:
        sd = target_dir / sub
        if sd.exists() and sd.is_dir():
            found_subdirs = True
            for f in sorted(sd.glob("*.json")):
                if f.is_file() and not f.name.startswith("."):
                    files.append(f)

    if not found_subdirs:
        # Search recursively
        for f in sorted(target_dir.rglob("*.json")):
            if f.is_file() and not f.name.startswith("."):
                name = f.name.lower()
                if name in {"schema.json", "catalog.json", "catalog-index.json", "package.json", "tsconfig.json"}:
                    continue
                files.append(f)

    # De-duplicate by canonical path
    seen = set()
    unique_files = []
    for f in files:
        resolved = f.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique_files.append(f)

    return unique_files


def build_draft_schema(strict_schema: Dict[str, Any]) -> Dict[str, Any]:
    """Create draft-tolerant schema relaxing required arrays for incomplete records."""
    draft_schema = copy.deepcopy(strict_schema)
    if "properties" in draft_schema:
        if "physical" in draft_schema["properties"] and "required" in draft_schema["properties"]["physical"]:
            draft_schema["properties"]["physical"]["required"] = []
        if "identity" in draft_schema["properties"] and "required" in draft_schema["properties"]["identity"]:
            # Keep vendor, model, category required for identity
            draft_schema["properties"]["identity"]["required"] = ["vendor", "model", "category"]
    return draft_schema


def process_records(input_files: List[Path], schema: Optional[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Process, validate, normalize records, and build index."""
    strict_validator = None
    draft_validator = None
    if HAS_JSONSCHEMA and schema:
        try:
            strict_validator = Draft202012Validator(schema)
            draft_schema = build_draft_schema(schema)
            draft_validator = Draft202012Validator(draft_schema)
        except Exception as e:
            print(f"[WARN] Failed to initialize JSON schema validator: {e}", file=sys.stderr)

    catalog_entries: List[Dict[str, Any]] = []
    by_category: Dict[str, List[str]] = {}
    counts = {"total": 0, "l1": 0, "draft": 0}

    for path in input_files:
        try:
            with open(path, "r", encoding="utf-8") as f:
                record = json.load(f)
        except Exception as e:
            print(f"[WARN] Skipping unreadable JSON file {path}: {e}", file=sys.stderr)
            continue

        if not isinstance(record, dict) or "identity" not in record:
            print(f"[WARN] Skipping non-equipment record JSON {path}", file=sys.stderr)
            continue

        # Check L1 completeness
        missing_fields = []
        present_count = 0
        for field_path, checker in L1_REQUIRED_FIELDS:
            if checker(record):
                present_count += 1
            else:
                missing_fields.append(field_path)

        completeness_pct = round((present_count / len(L1_REQUIRED_FIELDS)) * 100.0, 1)
        # AC2: Exactly 7 entries have conformance_level == "L1", 114 have "draft"
        is_l1 = (len(missing_fields) == 0)
        conformance_level = "L1" if is_l1 else "draft"

        # Schema Validation
        if strict_validator and draft_validator:
            if is_l1:
                errors = list(strict_validator.iter_errors(record))
                if errors:
                    print(f"[WARN] Record {path.name} failed L1 schema validation: {errors[0].message}", file=sys.stderr)
                    # If corrupted, skip
                    if any("required" not in e.message for e in errors):
                        continue
            else:
                errors = list(draft_validator.iter_errors(record))
                if errors:
                    print(f"[WARN] Record {path.name} failed draft schema validation: {errors[0].message}", file=sys.stderr)
                    # If structural violation (bad types, unknown props, illegal enums), skip
                    continue

        record_id = record.get("record_id", "")
        vendor = record.get("identity", {}).get("vendor", {}).get("value", "")
        model = record.get("identity", {}).get("model", {}).get("value", "")
        category = record.get("identity", {}).get("category", {}).get("value", "other")

        tier_summary = extract_tier_summary(record)
        prefill_url = f"/add-equipment?vendor={urllib.parse.quote(vendor)}&model={urllib.parse.quote(model)}"

        entry = {
            "record_id": record_id,
            "vendor": vendor,
            "model": model,
            "category": category,
            "conformance_level": conformance_level,
            "completeness_pct": completeness_pct,
            "tier_summary": tier_summary,
            "missing_fields": missing_fields,
            "prefill_url": prefill_url,
            "record": record,
        }

        catalog_entries.append(entry)
        counts["total"] += 1
        if conformance_level == "L1":
            counts["l1"] += 1
        else:
            counts["draft"] += 1

        if category not in by_category:
            by_category[category] = []
        by_category[category].append(record_id)

    catalog_index = {
        "by_category": by_category,
        "counts": counts,
    }

    return catalog_entries, catalog_index


def main():
    parser = argparse.ArgumentParser(description="Build SemiconFab Equipment Catalog")
    parser.add_argument(
        "unzipped_dir",
        nargs="?",
        default=".",
        help="Path to unzipped migration output directory (default: current directory)",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory to write catalog.json and catalog-index.json (default: current directory)",
    )

    args = parser.parse_args()
    target_dir = Path(args.unzipped_dir).resolve()
    out_dir = Path(args.output_dir).resolve()

    if not target_dir.exists():
        print(f"Error: Directory {target_dir} does not exist.", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning for equipment records in: {target_dir}")
    files = discover_record_files(target_dir)
    print(f"Discovered {len(files)} candidate JSON files.")

    schema = find_schema([target_dir, out_dir])
    if schema:
        print("Loaded schema.json successfully.")
    else:
        print("[WARN] schema.json not found, proceeding without jsonschema validation.", file=sys.stderr)

    catalog, index = process_records(files, schema)

    out_dir.mkdir(parents=True, exist_ok=True)
    catalog_path = out_dir / "catalog.json"
    index_path = out_dir / "catalog-index.json"

    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print(f"Emitted catalog.json: {len(catalog)} entries -> {catalog_path}")

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"Emitted catalog-index.json: counts={index['counts']} -> {index_path}")

    print("\nSummary:")
    print(f"  Total records: {index['counts']['total']}")
    print(f"  L1 verified:   {index['counts']['l1']}")
    print(f"  Draft records: {index['counts']['draft']}")
    print(f"  Categories:    {len(index['by_category'])}")


if __name__ == "__main__":
    main()
