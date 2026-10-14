<!-- Python validation package and CLI tool for the SemiconFab Equipment Schema v1.0 specification. -->

# schemavalidator — SemiconFab Equipment Schema v1.0 Validator

A bilingual Python validation package and CLI tool for the **SemiconFab Equipment Schema v1.0** specification.

---

## 1. Installation

Requires Python >= 3.9.

```bash
# In the package root directory:
pip install .

# Or editable install for development:
pip install -e .
```

### Dependencies

- `jsonschema >= 4.18.0` (Draft 2020-12 support)
- `pytest >= 7.0.0` (only needed for running tests)

---

## 2. CLI Usage

### Validate a single JSON record

```bash
# English output (default):
python -m schemavalidator validate examples/golden-etch-lam-kiyo.json

# Chinese output:
python -m schemavalidator validate examples/golden-etch-lam-kiyo.json --lang zh

# Or use installed console command:
schemavalidator validate examples/golden-etch-lam-kiyo.json --lang zh
```

**Exit codes:**

- `0`: Record is valid
- `1`: Record has validation errors
- `2`: Invalid CLI invocation arguments

### Batch validate all records in a directory

```bash
python -m schemavalidator validate-dir examples/ --lang zh
```

Prints an aligned table:

```
文件名                           | 状态 | 达标等级 | 错误数 | 告警数
--------------------------------+------+----------+--------+---------
golden-etch-lam-kiyo.json        | 通过 | L3       |      0 |        0
golden-pecvd-amat-producer-gt.json | 通过 | L3       |      0 |        0

总计: 2 个文件，全部校验通过。
```

---

## 3. Python API Usage

```python
from schemavalidator import validate_record

record = {
    "schema_version": "1.0",
    "record_id": "00000000-0000-0000-0000-000000000000",
    "conformance_level": "L1",
    "record_status": "draft",
    "submitted_by": "Researcher",
    "submitted_at": "2026-10-11",
    "updated_at": "2026-10-11",
    "identity": {
        "vendor": {"value": "Lam Research", "provenance": {"tier": "vendor_confirmed"}},
        "model": {"value": "Kiyo", "provenance": {"tier": "vendor_confirmed"}},
        "category": {"value": "dry_etch", "provenance": {"tier": "independent_verified"}},
        "wafer_sizes_mm": {"value": [300], "provenance": {"tier": "vendor_confirmed"}},
    },
    "physical": {
        "width_mm": {"value": 3200, "unit": "mm", "provenance": {"tier": "inferred"}},
        "depth_mm": {"value": 3400, "unit": "mm", "provenance": {"tier": "inferred"}},
        "height_mm": {"value": 2100, "unit": "mm", "provenance": {"tier": "inferred"}},
    }
}

report = validate_record(record)
print("Is valid:", report.is_valid)
print("Detected Conformance:", report.conformance_detected)
print("Summary (EN):", report.summary_en)
print("Summary (ZH):", report.summary_zh)

if not report.is_valid:
    for err in report.errors:
        print(f"[{err.field_path}] {err.message_zh} (rule: {err.rule})")
```

---

## 4. Running Tests

```bash
pytest
# Or verbose output:
pytest -v
```

---

## 5. Architectural Decisions & Design Assumptions

### 1. Handling of `format: "uuid"` on `record_id`

- **Context**: In `schema.json`, `record_id` is defined with `"format": "uuid"`. Some real-world records use 37-character IDs with 13 hex characters in the final chunk (e.g., `...-2d5e7a8b9c0d1`), whereas RFC 4122 specifies 36 characters.
- **Decision**: In accordance with JSON Schema Draft 2020-12 specifications, format assertions are optional vocabularies unless explicitly enforced via format checkers. We default to using `Draft202012Validator` without forcing strict RFC 4122 regex rejection, ensuring golden examples validate cleanly while strictly validating that `record_id` exists and is a valid string.

### 2. Precise `field_path` Construction for `required` Properties

- **Context**: Standard `jsonschema` validation reports errors on the parent container object (e.g., `absolute_path = ['physical', 'width_mm', 'provenance']`) with message `'tier' is a required property`.
- **Decision**: To provide exact diagnostics (e.g., `physical.width_mm.provenance.tier` is named as the exact missing field path), we extract the missing property name and concatenate it to produce the exact target path.

### 3. Layer Conformance Level Detection (`conformance_detected`)

- **Context**: A record may declare a target `conformance_level` (e.g., `L3`), but fail some requirements while still satisfying lower conformance levels (e.g., `L1`).
- **Decision**: `detect_highest_conformance` tests the record against `L1`, `L2`, and `L3` sequentially using the schema's own rules:
  - If meta, identity, and physical are valid -> satisfies `L1`.
  - If L1 is satisfied and the `facilities` layer is present and valid -> satisfies `L2`.
  - If L2 is satisfied and `process_capability`, `reliability`, and `commercial` layers are present and valid -> satisfies `L3`.
  - If L1 fails, `conformance_detected` returns `None`.

### 4. Low-Confidence Warning Threshold

- **Context**: An L3 record where >50% of values are `synthetic` tier should produce a low-confidence warning without failing structural validation (`is_valid == True`).
- **Decision**: We recursively traverse all `provenance.tier` entries across all layers. If target conformance is `L3` and `synthetic_count / total_tiers > 0.50`, a `ValidationWarning` with rule `low_confidence_synthetic_ratio` is emitted in both English and Chinese. It does not alter `is_valid`.

### 5. CLI Behavior and Exit Codes

- **Context**: The CLI supports single file validation (`validate <file>`), batch directory validation (`validate-dir <dir>`), and bilingual output (`--lang en|zh`).
- **Decision**:
  - `validate <file>`: Returns `0` if valid, `1` if invalid.
  - `validate-dir <dir>`: Scans all `*.json` in the directory, outputs a formatted ASCII table, and returns `0` if all files are valid, `1` if any file fails.
  - Subcommands are optional: running `python -m schemavalidator path/to/file.json` directly defaults to validating the file (or directory if a path points to a folder).
