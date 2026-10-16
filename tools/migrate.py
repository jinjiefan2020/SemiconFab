#!/usr/bin/env python3
"""
SemiconFab CSV to Schema v1.0 Migration Tool (migrate.py)
Transforms the semiconductor equipment database CSV into schema-compliant records.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import re
import sys
import uuid

# Deterministic record IDs: uuid5 over "vendor||model" so catalog rebuilds are
# stable across runs. (Changed from uuid.uuid4() in v1.1.0 — random IDs
# invalidated layout-default.json tool_ids and catalog-fallback.js on every rebuild.)
RECORD_ID_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_URL, "https://semiconfab.org/schema/equipment-record/v1")


def make_record_id(vendor: str, model: str, category: str = "") -> str:
    key = f"{(vendor or '').strip().lower()}||{(model or '').strip().lower()}||{(category or '').strip().lower()}"
    return str(uuid.uuid5(RECORD_ID_NAMESPACE, key))


# Site taxonomy refinements (v1.2.0): split DB coarse segments into the
# fab-meaningful categories used by twin bays, 3D colors and filters.
# Applied AFTER the segment->category mapping, BEFORE make_record_id().
RESIST_TRACK_MODELS = {
    ("tokyo electron", "clean track lithius pro z"),
    ("tokyo electron", "clean track act 12"),
    ("tokyo electron", "clean track act 8"),
    ("kingsemi", "ft300"),
}
INSPECTION_MODELS = {
    ("kla", "3935 (39xx series)"),
    ("kla", "2930 (29xx series)"),
    ("kla", "edr7280"),
    ("kla", "2920 series"),
    ("kla", "surfscan sp7xp"),
    ("applied materials", "uvision 4"),
    ("lasertec", "matrics x9ultra"),
    ("skyverse", "spruce-800"),
    ("skyverse", "spruce-600"),
}


def refine_category(vendor: str, model: str, cat: str) -> str:
    key = ((vendor or "").strip().lower(), (model or "").strip().lower())
    if key in RESIST_TRACK_MODELS:
        return "resist_track"
    if key in INSPECTION_MODELS:
        return "inspection"
    return cat
from typing import Any, Dict, List, Optional, Tuple

import jsonschema
from jsonschema import Draft202012Validator

CATEGORY_MAP = {
    "Lithography": "lithography",
    "Etch": "dry_etch",
    "Packaging": "packaging",
    "Deposition": "thin_film_deposition",
    "Test": "test",
    "Ion Implant": "ion_implantation",
    "CMP": "cmp",
    "Cleaning": "wet_clean",
    "Diffusion & Anneal": "thermal_processing",
}

SOURCE_TIER_MAP = {
    "official": "vendor_confirmed",
    "official_mirror": "community_corroborated",
    "dealer": "independent_verified",
    "trade_press": "community_corroborated",
    "analyst": "inferred",
}


def slugify(text: str) -> str:
    """Create a filesystem-safe slug from text."""
    text = (text or "").lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-") or "unknown"


def parse_dimensions(dim_str: Optional[str]) -> Optional[Tuple[int, int, int]]:
    """Parse footprint dimensions into SI millimeters (width, depth, height)."""
    if not dim_str or dim_str.strip() == "not published":
        return None
    clean = dim_str.replace(",", "")

    # 1. Match millimeter patterns like 'W2700 x D4100 x H2500 mm' or '1600 x 1200 x 1540 mm'
    if "mm" in clean:
        m = re.search(r"W(\d+)\s*x\s*D(\d+)\s*x\s*H(\d+)\s*mm", clean)
        if m:
            return int(m.group(1)), int(m.group(2)), int(m.group(3))
        m = re.search(r"(\d+)\s*x\s*(\d+)\s*x\s*(\d+)\s*mm", clean)
        if m:
            return int(m.group(1)), int(m.group(2)), int(m.group(3))

    # 2. Match meter patterns like '2.3 x 3.66 x 3.0 m' or '(W)2.7 x (D)6.6 x (H)2.83 m'
    m = re.search(
        r"(?:\(?W\)?\s*)?([\d\.]+)\s*x\s*(?:\(?D\)?\s*)?([\d\.]+)\s*x\s*(?:\(?H\)?\s*)?([\d\.]+)\s*m(?![a-zA-Z])",
        clean,
    )
    if m:
        w = round(float(m.group(1)) * 1000)
        d = round(float(m.group(2)) * 1000)
        h = round(float(m.group(3)) * 1000)
        return w, d, h

    return None


def parse_weight(wt_str: Optional[str]) -> Optional[float]:
    """Parse installed weight in kilograms."""
    if not wt_str or wt_str.strip() == "not published":
        return None
    clean = wt_str.replace(",", "")
    m = re.search(r"(\d+(?:\.\d+)?)\s*kg", clean)
    if m:
        return float(m.group(1))
    return None


def parse_wafer_size(raw_ws: Optional[str]) -> Tuple[Optional[List[int]], Optional[str], str]:
    """
    Parse wafer size into list of integers subset of [150, 200, 300].
    Returns (sizes, provenance_note, status_tag).
    """
    raw = (raw_ws or "").strip()
    if not raw:
        return None, None, "omitted_empty"
    if raw in ("N/A", "unverified", "panel"):
        return None, None, f"omitted_{raw}"
    if raw.startswith("N/A"):
        return None, None, f"omitted_na_variant ({raw})"
    if any(k in raw for k in ("substrate", "bond area", "work area", "4/6 inch")):
        return None, None, f"omitted_non_wafer ({raw})"

    # Handle '4-12 in wafer frames': 4-12 in corresponds to 100-300mm; 100 is dropped as outside schema enum
    if "4-12 in wafer frames" in raw:
        return [150, 200, 300], "Converted 4-12 in wafer frames to [150, 200, 300] mm; 100mm dropped (outside enum)", "parsed_ok"

    if "unverified" in raw.lower() and "300" in raw and "200" not in raw:
        return [300], "unverified in source", "parsed_ok"
    if "unverified" in raw.lower() and "200" in raw and "300" not in raw:
        return [200], "unverified in source", "parsed_ok"
    if ("200" in raw and "300" in raw) and "150" not in raw:
        return [200, 300], None, "parsed_ok"
    if "100/150/200" in raw:
        return [150, 200], "100mm dropped (not in schema enum)", "parsed_ok"
    if "150" in raw and "200" in raw and "300" in raw:
        return [150, 200, 300], None, "parsed_ok"
    if "<=300mm" in raw:
        return [150, 200, 300], "<=300mm interpreted as [150, 200, 300]", "parsed_ok"
    if "300mm" in raw or "300" in raw:
        return [300], None, "parsed_ok"
    if "200mm" in raw or "200" in raw:
        return [200], None, "parsed_ok"

    return None, None, f"unparseable ({raw})"


def count_provenance_tiers(obj: Any) -> Counter:
    """Recursively collect provenance.tier counts."""
    counts = Counter()
    if isinstance(obj, dict):
        if "tier" in obj and isinstance(obj["tier"], str):
            counts[obj["tier"]] += 1
        for v in obj.values():
            counts.update(count_provenance_tiers(v))
    elif isinstance(obj, list):
        for item in obj:
            counts.update(count_provenance_tiers(item))
    return counts


def map_csv_row_to_record(row: Dict[str, str], row_idx: int) -> Tuple[Dict[str, Any], bool, Optional[str]]:
    """
    Transform a CSV row into a schema v1.0 record structure.
    Returns (record, has_footprint, wafer_parse_status).
    """
    segment = row.get("segment", "").strip()
    model_str = row.get("model", "").strip()
    vendor_str = row.get("vendor", "").strip()

    # Category mapping rule
    if segment == "Metrology & Inspection":
        is_insp = any(k in model_str.lower() for k in ("inspection", "defect"))
        cat = "inspection" if is_insp else "metrology"
    else:
        cat = CATEGORY_MAP.get(segment, "other")

    cat = refine_category(vendor_str, model_str, cat)

    src_tier_raw = row.get("source_tier", "").strip()
    tier_mapped = SOURCE_TIER_MAP.get(src_tier_raw, "inferred")
    source_url = row.get("source_url", "").strip()

    dims = parse_dimensions(row.get("dimensions"))
    wt = parse_weight(row.get("weight"))
    ws_val, ws_note, ws_status = parse_wafer_size(row.get("wafer_size"))

    has_footprint = (dims is not None)

    # Base record structure
    record: Dict[str, Any] = {
        "schema_version": "1.0",
        "record_id": make_record_id(vendor_str, model_str, cat),
        "conformance_level": "L1",
        "record_status": "draft",
        "submitted_by": "csv-migration v1.0",
        "submitted_at": "2026-10-11",
        "updated_at": "2026-10-11",
        "identity": {
            "vendor": {
                "value": vendor_str,
                "provenance": {"tier": tier_mapped, "source": source_url},
            },
            "model": {
                "value": model_str,
                "provenance": {"tier": tier_mapped, "source": source_url},
            },
            "category": {
                "value": cat,
                "provenance": {"tier": "inferred", "source": "segment mapping v1.0"},
            },
        },
        "physical": {},
    }

    # Wafer size
    if ws_val is not None:
        prov: Dict[str, Any] = {"tier": tier_mapped, "source": source_url}
        if ws_note:
            prov["note"] = ws_note
        record["identity"]["wafer_sizes_mm"] = {"value": ws_val, "provenance": prov}

    # Process node
    p_node = row.get("process_node", "").strip()
    if p_node and p_node != "not published":
        node_tier = "inferred" if "(inferred)" in p_node else tier_mapped
        record["identity"]["node_applicability"] = {
            "value": p_node,
            "provenance": {"tier": node_tier, "source": source_url},
        }

    # Physical dimensions
    dim_tier = "independent_verified" if src_tier_raw == "dealer" else "inferred"
    if dims:
        w, d, h = dims
        record["physical"]["width_mm"] = {
            "value": w,
            "unit": "mm",
            "provenance": {"tier": dim_tier, "source": source_url},
        }
        record["physical"]["depth_mm"] = {
            "value": d,
            "unit": "mm",
            "provenance": {"tier": dim_tier, "source": source_url},
        }
        record["physical"]["height_mm"] = {
            "value": h,
            "unit": "mm",
            "provenance": {"tier": dim_tier, "source": source_url},
        }
    if wt:
        record["physical"]["weight_kg"] = {
            "value": wt,
            "unit": "kg",
            "provenance": {"tier": dim_tier, "source": source_url},
        }

    # Key specs
    key_specs = row.get("key_specs", "").strip()
    if key_specs and key_specs != "not published":
        record["process_capability"] = {
            "capabilities": [
                {
                    "process": segment,
                    "detail": {
                        "value": key_specs,
                        "provenance": {"tier": tier_mapped, "source": source_url},
                    },
                }
            ]
        }

    # Notes
    notes = row.get("notes", "").strip()
    if notes and notes != "not published":
        record["notes"] = f"[source note] {notes}"

    return record, has_footprint, ws_status


def generate_migration_report(
    total_rows: int,
    records_written: int,
    needs_footprint_count: int,
    category_counter: Counter,
    wafer_status_counter: Counter,
    raw_wafer_counter: Counter,
    tier_counter: Counter,
    top_review_rows: List[Dict[str, Any]],
    decisions: List[str],
) -> str:
    """Generate Markdown migration report."""
    md = []
    md.append("# Equipment Database Migration Report — Schema v1.0")
    md.append(f"\nGenerated: 2026-10-11 | Source: fab_equipment_db.csv\n")

    md.append("## 1. Row Summary (行数统计)")
    md.append(f"- **Total Rows Read (读取总行数)**: {total_rows}")
    md.append(f"- **Emitted to `output/records/` (符合 Schema v1.0 标准已生成记录)**: {records_written}")
    md.append(f"- **Emitted to `output/needs_footprint/` (缺失外形尺寸暂存记录)**: {needs_footprint_count}")
    md.append(f"- **Synthetic Values Emitted**: {tier_counter.get('synthetic', 0)} (Strictly 0)\n")

    md.append("## 2. Equipment Category Distribution (设备类别分布)")
    md.append("| Category (Schema Enum) | Count | Percentage |")
    md.append("|---|---|---|")
    for cat, count in category_counter.most_common():
        pct = (count / total_rows) * 100
        md.append(f"| `{cat}` | {count} | {pct:.1f}% |")
    md.append("")

    md.append("## 3. Wafer Size Parsing Breakdown (晶圆尺寸解析明细)")
    parsed_ok_cnt = wafer_status_counter.get("parsed_ok", 0)
    omitted_cnt = total_rows - parsed_ok_cnt
    md.append(f"- **Parsed OK (成功解析)**: {parsed_ok_cnt} ({parsed_ok_cnt/total_rows*100:.1f}%)")
    md.append(f"- **Omitted / Non-standard (留空 / 非标基底)**: {omitted_cnt} ({omitted_cnt/total_rows*100:.1f}%)")
    md.append("\n### Raw CSV Values Distribution (原始值分布)")
    md.append("| Raw `wafer_size` | Count | Parsing Outcome |")
    md.append("|---|---|---|")
    for raw_val, count in raw_wafer_counter.most_common():
        val, note, _ = parse_wafer_size(raw_val)
        if val is not None:
            outcome = f"Mapped to `{val}`"
            if note:
                outcome += f" ({note})"
        else:
            outcome = "Omitted (non-wafer / substrate / unverified)"
        md.append(f"| `{raw_val}` | {count} | {outcome} |")
    md.append("")

    md.append("## 4. Provenance Tier Distribution (数据溯源可信度阶梯分布)")
    md.append("| Provenance Tier | Emitted Values Count | Percentage |")
    md.append("|---|---|---|")
    total_tiers = sum(tier_counter.values())
    for tier, count in tier_counter.most_common():
        pct = (count / total_tiers) * 100 if total_tiers else 0
        md.append(f"| `{tier}` | {count} | {pct:.1f}% |")
    md.append("")

    md.append("## 5. Top 10 Records Needing Human Review (优先人工审核记录)")
    md.append("| Row # | Vendor | Model | Inferred Fields | Footprint Status | Note |")
    md.append("|---|---|---|---|---|---|")
    for r in top_review_rows[:10]:
        fp_str = "Published ✓" if r["has_fp"] else "Missing (not published)"
        md.append(f"| {r['row_idx']} | {r['vendor']} | {r['model']} | {r['inferred_count']} | {fp_str} | {r['notes']} |")
    md.append("")

    md.append("## 6. Explicit Ambiguity Decisions (裁决记录清单)")
    for i, dec in enumerate(decisions, 1):
        md.append(f"{i}. {dec}")
    md.append("")

    return "\n".join(md)


def run_migration(csv_path: Path, output_dir: Path, schema_path: Path) -> None:
    """Execute end-to-end migration."""
    print(f"Reading CSV from: {csv_path}")
    if not csv_path.exists():
        print(f"Error: CSV file not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    validator = Draft202012Validator(schema)

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    records_dir = output_dir / "records"
    needs_fp_dir = output_dir / "needs_footprint"
    records_dir.mkdir(parents=True, exist_ok=True)
    needs_fp_dir.mkdir(parents=True, exist_ok=True)

    category_counter = Counter()
    wafer_status_counter = Counter()
    raw_wafer_counter = Counter()
    total_tier_counter = Counter()

    records_written = 0
    needs_footprint_count = 0
    review_rows = []

    decisions = [
        "**Metrology & Inspection Split Rule**: Models containing 'inspection' or 'defect' are mapped to `inspection`, all others mapped to `metrology`. (e.g. broadband plasma tools like 3935/2930 follow this rule as literal models).",
        "**Wafer Size Frame Normalization**: '4-12 in wafer frames' on BESI Datacon 2200 EVO converted to `[150, 200, 300]`, dropping 100mm as outside the closed schema enum.",
        "**Non-wafer Substrate Omission**: Rows with 'panel', 'N/A', 'photomask', or substrate dimensions omit `wafer_sizes_mm` entirely to preserve honesty.",
        "**Multi-unit Dimensions Handling**: Ebara F-REX300 published main unit and power supply dimensions; main unit dimensions (W2700 x D4100 x H2500 mm) were parsed as primary cleanroom footprint.",
        "**Zero Synthetic Tolerance**: No synthetic data was generated. Missing footprint dimensions are left out and records moved to `needs_footprint/` rather than inventing estimates.",
    ]

    for idx, r in enumerate(rows, 1):
        record, has_fp, ws_status = map_csv_row_to_record(r, idx)

        cat = record["identity"]["category"]["value"]
        category_counter[cat] += 1
        wafer_status_counter[ws_status] += 1
        raw_wafer_counter[r.get("wafer_size", "").strip() or "empty"] += 1

        tier_counts = count_provenance_tiers(record)
        total_tier_counter.update(tier_counts)

        # Check schema validity
        is_valid = validator.is_valid(record)

        vendor_slug = slugify(r.get("vendor", ""))
        model_slug = slugify(r.get("model", ""))
        filename = f"{idx:03d}_{vendor_slug}_{model_slug}.json"

        inferred_count = tier_counts.get("inferred", 0)
        review_rows.append({
            "row_idx": idx,
            "vendor": r.get("vendor", ""),
            "model": r.get("model", ""),
            "inferred_count": inferred_count,
            "has_fp": has_fp,
            "notes": "Missing footprint" if not has_fp else ("Valid L1" if is_valid else "Missing wafer size"),
        })

        if has_fp and is_valid:
            target_path = records_dir / filename
            with open(target_path, "w", encoding="utf-8") as f:
                json.dump(record, f, indent=2, ensure_ascii=False)
            records_written += 1
        else:
            target_path = needs_fp_dir / filename
            with open(target_path, "w", encoding="utf-8") as f:
                json.dump(record, f, indent=2, ensure_ascii=False)
            needs_footprint_count += 1

    # Sort review candidates by highest inferred count
    review_rows.sort(key=lambda x: -x["inferred_count"])

    report_md = generate_migration_report(
        total_rows=len(rows),
        records_written=records_written,
        needs_footprint_count=needs_footprint_count,
        category_counter=category_counter,
        wafer_status_counter=wafer_status_counter,
        raw_wafer_counter=raw_wafer_counter,
        tier_counter=total_tier_counter,
        top_review_rows=review_rows,
        decisions=decisions,
    )

    report_path = output_dir / "migration_report.md"
    report_path.write_text(report_md, encoding="utf-8")

    print("\n--- Migration Complete ---")
    print(f"Total Rows: {len(rows)}")
    print(f"Emitted to records/ (Valid L1): {records_written}")
    print(f"Emitted to needs_footprint/: {needs_footprint_count}")
    print(f"Report written to: {report_path}")


def main():
    parser = argparse.ArgumentParser(description="Migrate equipment CSV to Schema v1.0")
    parser.add_argument(
        "csv_file",
        nargs="?",
        default="data/semiconductor_equipment_database.csv",
        help="Path to CSV database (default: data/semiconductor_equipment_database.csv)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="output",
        help="Output directory (default: output)",
    )
    parser.add_argument(
        "--schema",
        "-s",
        default="./schema.json",
        help="Path to schema.json",
    )

    args = parser.parse_args()
    csv_path = Path(args.csv_file)
    output_dir = Path(args.output)
    schema_path = Path(args.schema)

    run_migration(csv_path, output_dir, schema_path)


if __name__ == "__main__":
    main()
