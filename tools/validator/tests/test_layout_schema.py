import json
from pathlib import Path
import pytest
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent

def test_layout_schema_validity():
    schema_path = REPO_ROOT / "twin" / "layout-schema.json"
    assert schema_path.exists(), "twin/layout-schema.json must exist"
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    Draft202012Validator.check_schema(schema)

def test_default_layout_conformance():
    schema_path = REPO_ROOT / "twin" / "layout-schema.json"
    layout_path = REPO_ROOT / "twin" / "layout-default.json"
    catalog_path = REPO_ROOT / "catalog.json"

    assert layout_path.exists(), "twin/layout-default.json must exist"
    assert catalog_path.exists(), "catalog.json must exist"

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    with open(layout_path, "r", encoding="utf-8") as f:
        layout = json.load(f)
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    validator = Draft202012Validator(schema)
    errors = list(validator.iter_errors(layout))
    assert len(errors) == 0, f"Default layout has schema errors: {errors}"

    # Verify all 121 tools are present and ids match catalog record_id
    catalog_ids = {item["record_id"] for item in catalog}
    assert len(layout["tools"]) == 121, f"Expected 121 tools, got {len(layout['tools'])}"
    for tool in layout["tools"]:
        assert tool["tool_id"] in catalog_ids, f"Tool id {tool['tool_id']} not in catalog"
        assert tool["rotation"] in (0, 90, 180, 270)
        assert isinstance(tool["x"], (int, float))
        assert isinstance(tool["z"], (int, float))

def test_invalid_layout_rejection():
    schema_path = REPO_ROOT / "twin" / "layout-schema.json"
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    validator = Draft202012Validator(schema)

    # 1. Invalid rotation (e.g. 45 degrees)
    bad_rot = {"version": "1.0.0", "tools": [{"tool_id": "test", "bay": "lithography", "x": 0, "z": 0, "rotation": 45}]}
    assert len(list(validator.iter_errors(bad_rot))) > 0

    # 2. Missing tool_id
    missing_id = {"version": "1.0.0", "tools": [{"bay": "lithography", "x": 0, "z": 0, "rotation": 0}]}
    assert len(list(validator.iter_errors(missing_id))) > 0

    # 3. Invalid bay name
    bad_bay = {"version": "1.0.0", "tools": [{"tool_id": "test", "bay": "non_existent_bay", "x": 0, "z": 0, "rotation": 0}]}
    assert len(list(validator.iter_errors(bad_bay))) > 0

