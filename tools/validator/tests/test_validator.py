import copy
import json
from pathlib import Path
import subprocess
import sys
import pytest

from schemavalidator import validate_record
from schemavalidator.report import ValidationReport

EXAMPLES_DIR = Path(__file__).resolve().parent.parent / "examples"


@pytest.fixture
def golden_etch_record():
    with open(EXAMPLES_DIR / "golden-etch-lam-kiyo.json", "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def golden_pecvd_record():
    with open(EXAMPLES_DIR / "golden-pecvd-amat-producer-gt.json", "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def minimal_l1_record():
    return {
        "schema_version": "1.0",
        "record_id": "11111111-2222-3333-4444-555555555555",
        "conformance_level": "L1",
        "record_status": "draft",
        "submitted_by": "Test Submitter",
        "submitted_at": "2026-10-11",
        "updated_at": "2026-10-11",
        "identity": {
            "vendor": {
                "value": "Test Vendor",
                "provenance": {"tier": "vendor_confirmed", "source": "https://example.com"},
            },
            "model": {
                "value": "Test Model 100",
                "provenance": {"tier": "vendor_confirmed", "source": "https://example.com"},
            },
            "category": {
                "value": "lithography",
                "provenance": {"tier": "independent_verified"},
            },
            "wafer_sizes_mm": {
                "value": [300],
                "provenance": {"tier": "vendor_confirmed"},
            },
        },
        "physical": {
            "width_mm": {
                "value": 2500,
                "unit": "mm",
                "provenance": {"tier": "inferred"},
            },
            "depth_mm": {
                "value": 3000,
                "unit": "mm",
                "provenance": {"tier": "inferred"},
            },
            "height_mm": {
                "value": 2200,
                "unit": "mm",
                "provenance": {"tier": "inferred"},
            },
        },
    }


def test_ac1_golden_examples_pass(golden_etch_record, golden_pecvd_record):
    """AC1: Both golden examples validate with is_valid == True."""
    report_etch = validate_record(golden_etch_record)
    assert report_etch.is_valid is True, f"Etch errors: {report_etch.errors}"
    assert report_etch.conformance_detected == "L3"
    assert len(report_etch.errors) == 0

    report_pecvd = validate_record(golden_pecvd_record)
    assert report_pecvd.is_valid is True, f"PECVD errors: {report_pecvd.errors}"
    assert report_pecvd.conformance_detected == "L3"
    assert len(report_pecvd.errors) == 0


def test_ac2_tier_deleted_rejection(golden_etch_record):
    """AC2: A record with physical.width_mm.provenance.tier deleted is rejected;
    the error names the field path and says tier is required."""
    record = copy.deepcopy(golden_etch_record)
    del record["physical"]["width_mm"]["provenance"]["tier"]

    report = validate_record(record)
    assert report.is_valid is False
    assert len(report.errors) > 0

    # Must find error specifically naming physical.width_mm.provenance.tier and tier is required
    matched = False
    for err in report.errors:
        if (
            "physical.width_mm.provenance" in err.field_path
            and "tier" in err.field_path
            and ("required" in err.message_en.lower() or err.rule == "required")
        ):
            matched = True
            break
    assert matched, f"No error matching AC2 criteria in: {[str(e) for e in report.errors]}"


def test_ac3_l3_missing_facilities_rejection(golden_etch_record):
    """AC3: A conformance_level: 'L3' record with facilities deleted is rejected
    (missing required layer for L3)."""
    record = copy.deepcopy(golden_etch_record)
    record["conformance_level"] = "L3"
    if "facilities" in record:
        del record["facilities"]

    report = validate_record(record)
    assert report.is_valid is False
    assert any("facilities" in err.field_path for err in report.errors)
    # Detects L1 because meta+identity+physical are intact, but facilities is absent
    assert report.conformance_detected == "L1"


def test_ac4_minimal_l1_record(minimal_l1_record):
    """AC4: A minimal L1 record (meta + identity + physical only, conformance_level: 'L1')
    validates as True."""
    report = validate_record(minimal_l1_record)
    assert report.is_valid is True, f"Errors: {report.errors}"
    assert report.conformance_detected == "L1"
    assert len(report.errors) == 0


def test_ac5_l3_synthetic_warning(golden_etch_record):
    """AC5: An L3 record where every value is synthetic tier validates structurally True
    BUT produces the low-confidence warning."""
    record = copy.deepcopy(golden_etch_record)

    def set_all_tiers_synthetic(obj):
        if isinstance(obj, dict):
            if "tier" in obj:
                obj["tier"] = "synthetic"
            for v in obj.values():
                set_all_tiers_synthetic(v)
        elif isinstance(obj, list):
            for item in obj:
                set_all_tiers_synthetic(item)

    set_all_tiers_synthetic(record)

    report = validate_record(record)
    assert report.is_valid is True, f"Should be structurally valid, but got: {report.errors}"
    assert len(report.warnings) > 0
    assert any(w.rule == "low_confidence_synthetic_ratio" for w in report.warnings)
    # Check warning has both EN and ZH text
    warn = report.warnings[0]
    assert "low-confidence" in warn.message_en.lower()
    assert "低置信度" in warn.message_zh


def test_ac6_cli_exit_codes_and_bilingual(tmp_path, minimal_l1_record):
    """AC6: CLI exit codes: 0 on valid, 1 on invalid; --lang zh prints Chinese messages."""
    valid_file = tmp_path / "valid_l1.json"
    with open(valid_file, "w", encoding="utf-8") as f:
        json.dump(minimal_l1_record, f)

    invalid_rec = copy.deepcopy(minimal_l1_record)
    del invalid_rec["physical"]["width_mm"]
    invalid_file = tmp_path / "invalid_l1.json"
    with open(invalid_file, "w", encoding="utf-8") as f:
        json.dump(invalid_rec, f)

    root_dir = Path(__file__).resolve().parent.parent

    # Test valid exit code 0
    res_valid = subprocess.run(
        [sys.executable, "-m", "schemavalidator", "validate", str(valid_file)],
        cwd=root_dir,
        capture_output=True,
        text=True,
    )
    assert res_valid.returncode == 0
    assert "VALID" in res_valid.stdout

    # Test invalid exit code 1
    res_invalid = subprocess.run(
        [sys.executable, "-m", "schemavalidator", "validate", str(invalid_file)],
        cwd=root_dir,
        capture_output=True,
        text=True,
    )
    assert res_invalid.returncode == 1
    assert "INVALID" in res_invalid.stdout

    # Test --lang zh prints Chinese messages
    res_zh = subprocess.run(
        [sys.executable, "-m", "schemavalidator", "validate", str(invalid_file), "--lang", "zh"],
        cwd=root_dir,
        capture_output=True,
        text=True,
    )
    assert res_zh.returncode == 1
    assert "错误列表" in res_zh.stdout or "必填属性" in res_zh.stdout or "校验失败" in res_zh.stdout


def test_ac8_assumptions_doc_exists():
    """AC8: ASSUMPTIONS.md or README.md exists and lists >=1 decision."""
    candidates = [
        Path(__file__).resolve().parent.parent.parent.parent / "ASSUMPTIONS.md",
        Path(__file__).resolve().parent.parent / "README.md",
        Path(__file__).resolve().parent.parent / "ASSUMPTIONS.md",
    ]
    assumptions_file = next((p for p in candidates if p.exists()), candidates[0])
    assert assumptions_file.exists(), "ASSUMPTIONS.md must exist in the package or root"
    content = assumptions_file.read_text(encoding="utf-8")
    assert len(content.strip().splitlines()) >= 5, "ASSUMPTIONS.md must contain decisions"


def test_edge_cases_invalid_enums_and_extra_layers(minimal_l1_record):
    """Test invalid enums and L2 conformance detection."""
    # Invalid category
    rec_bad_cat = copy.deepcopy(minimal_l1_record)
    rec_bad_cat["identity"]["category"]["value"] = "laser_welding"
    rep_bad_cat = validate_record(rec_bad_cat)
    assert rep_bad_cat.is_valid is False
    assert any("category" in e.field_path for e in rep_bad_cat.errors)

    # Valid L2 record
    rec_l2 = copy.deepcopy(minimal_l1_record)
    rec_l2["conformance_level"] = "L2"
    rec_l2["facilities"] = {
        "power_kva": {"value": 50, "unit": "kVA", "provenance": {"tier": "inferred"}}
    }
    rep_l2 = validate_record(rec_l2)
    assert rep_l2.is_valid is True
    assert rep_l2.conformance_detected == "L2"


def test_cli_validate_dir(tmp_path, minimal_l1_record, golden_etch_record):
    """Test CLI validate-dir command table output."""
    with open(tmp_path / "rec1.json", "w", encoding="utf-8") as f:
        json.dump(minimal_l1_record, f)
    with open(tmp_path / "rec2.json", "w", encoding="utf-8") as f:
        json.dump(golden_etch_record, f)

    root_dir = Path(__file__).resolve().parent.parent
    res = subprocess.run(
        [sys.executable, "-m", "schemavalidator", "validate-dir", str(tmp_path)],
        cwd=root_dir,
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0
    assert "rec1.json" in res.stdout
    assert "rec2.json" in res.stdout
    assert "VALID" in res.stdout


def test_cli_validate_dir_with_invalid_file(tmp_path, minimal_l1_record):
    """Test CLI validate-dir returns exit code 1 when any file is invalid."""
    with open(tmp_path / "valid.json", "w", encoding="utf-8") as f:
        json.dump(minimal_l1_record, f)
    bad_rec = copy.deepcopy(minimal_l1_record)
    del bad_rec["identity"]["model"]
    with open(tmp_path / "bad.json", "w", encoding="utf-8") as f:
        json.dump(bad_rec, f)

    root_dir = Path(__file__).resolve().parent.parent
    res = subprocess.run(
        [sys.executable, "-m", "schemavalidator", "validate-dir", str(tmp_path), "--lang", "zh"],
        cwd=root_dir,
        capture_output=True,
        text=True,
    )
    assert res.returncode == 1
    assert "bad.json" in res.stdout
    assert "失败" in res.stdout or "INVALID" in res.stdout


def test_missing_l3_other_layers(golden_etch_record):
    """Test L3 record missing commercial, reliability, or process_capability."""
    # Missing commercial
    r1 = copy.deepcopy(golden_etch_record)
    del r1["commercial"]
    rep1 = validate_record(r1)
    assert rep1.is_valid is False
    assert any("commercial" in e.field_path for e in rep1.errors)

    # Missing reliability
    r2 = copy.deepcopy(golden_etch_record)
    del r2["reliability"]
    rep2 = validate_record(r2)
    assert rep2.is_valid is False
    assert any("reliability" in e.field_path for e in rep2.errors)

    # Missing process_capability
    r3 = copy.deepcopy(golden_etch_record)
    del r3["process_capability"]
    rep3 = validate_record(r3)
    assert rep3.is_valid is False
    assert any("process_capability" in e.field_path for e in rep3.errors)


def test_missing_meta_and_physical_dimensions(minimal_l1_record):
    """Test missing top-level meta or physical footprint dimensions."""
    r_no_id = copy.deepcopy(minimal_l1_record)
    del r_no_id["record_id"]
    rep_no_id = validate_record(r_no_id)
    assert rep_no_id.is_valid is False
    assert any("record_id" in e.field_path for e in rep_no_id.errors)

    r_no_height = copy.deepcopy(minimal_l1_record)
    del r_no_height["physical"]["height_mm"]
    rep_no_height = validate_record(r_no_height)
    assert rep_no_height.is_valid is False
    assert any("height_mm" in e.field_path for e in rep_no_height.errors)
