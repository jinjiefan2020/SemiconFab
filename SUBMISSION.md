# SemiconFab Equipment Submission Pipeline (`/add-equipment`) & Operator Loop

> Specification & Operational Guide for Contributor Submissions and Maintainer Ingestion  
> Conforms to Schema v1.0 & MIMAC-2026 Catalog Pipeline

---

## 1. Overview 架构概览

The SemiconFab Equipment Catalog operates on **static hosting with zero backend servers or databases**. Equipment submission is handled via a client-side submission pipeline in `add-equipment.html` (`/add-equipment`), closing the feedback loop between draft catalog entries and community contributors.

```
+-----------------------------------------------------------------------------+
|                            CONTRIBUTOR WORKFLOW                             |
|                                                                             |
|  [Catalog Draft Card]                                                       |
|          |                                                                  |
|          v Click "Help complete this record" / "数据待补充"                   |
|  [/add-equipment?vendor=...&model=...] (Prefilled + Trimmed + Editable)     |
|          |                                                                  |
|          v Fill Required L1 Fields (submitted_by, footprint dimensions...)  |
|  [Validate & Submit]                                                        |
|          |                                                                  |
|          +--> 1. Download JSON (Primary: <vendor>-<model>-<short-id>.json)  |
|          +--> 2. Copy to Clipboard                                          |
|          +--> 3. Submit via GitHub PR (submissions/pending/)                |
|          +--> 4. Submit via Email (mailto)                                  |
|          |                                                                  |
|          v                                                                  |
|  [Post-Submit Success Panel: Record ID + 3-Step Review Transparency]        |
+-----------------------------------------------------------------------------+
                                      |
                                      v (Contributor hands JSON to maintainer)
+-----------------------------------------------------------------------------+
|                            MAINTAINER WORKFLOW                              |
|                                                                             |
|  [Inbox Triage] (GitHub Issue / Email / PR Attachment)                      |
|          |                                                                  |
|          v                                                                  |
|  [Step 1: Automated Validation]                                             |
|  `PYTHONPATH=tools/validator python3 -m schemavalidator validate <file>`    |
|  `jsonschema -i <file> schema.json`                                         |
|          |                                                                  |
|          v                                                                  |
|  [Step 2: Migration Tree Placement]                                         |
|  - L1 Complete -> `output/records/<slug>.json`                              |
|  - Incomplete  -> `output/needs_footprint/<slug>.json`                      |
|          |                                                                  |
|          v                                                                  |
|  [Step 3: Rebuild Catalog & Indices]                                        |
|  `python3 tools/build_catalog.py output/ --output-dir .`                    |
|          |                                                                  |
|          v                                                                  |
|  [Step 4: Deploy & Verify]                                                  |
|  `git add ... && git commit && git push` -> Cloudflare Pages                |
+-----------------------------------------------------------------------------+
```

---

## 2. Contributor Path 贡献者工作流

### Step 1: Discover Draft from Catalog

1. Contributor browses the equipment catalog at `/catalog-demo.html`.
2. Tools with missing footprint dimensions display an amber draft callout banner:
   - Text: `数据待补充 · Help complete this record (Missing: width_mm, depth_mm, height_mm)`
   - Call-to-action button: `补全数据 · Complete Record`
3. Clicking the CTA directs the browser to:
   ```
   /add-equipment?vendor=<URL-ENCODED-VENDOR>&model=<URL-ENCODED-MODEL>
   ```
   _Example_: `/add-equipment?vendor=ASML&model=TWINSCAN%20NXT%3A2050i`

### Step 2: Form Prefill & Context Banner

1. On page load, `add-equipment.html` parses `window.location.search` via `URLSearchParams` and automatically trims leading/trailing whitespace.
2. A context banner appears above the form:
   > 正在补全草稿记录 · Completing draft record: **ASML TWINSCAN NXT:2050i**  
   > [← 返回目录 Back to catalog](/catalog-demo.html)
3. After dynamic schema layers finish rendering:
   - `identity.vendor` is automatically set to `ASML`.
   - `identity.model` is automatically set to `TWINSCAN NXT:2050i`.
   - Both inputs display a `来自目录 from catalog` badge.
   - Both fields remain **fully editable** so the contributor can fix typos or casing discrepancies.
4. If no query parameters are present, the form opens blank without a banner or JS errors.

### Step 3: Complete Required Fields & Provenance

1. **Submitter Identity (`submitted_by`)**: Required top-level text input: "Your name / email 你的姓名或邮箱" (e.g. `Linus <linus@example.com>`).
2. **Physical Dimensions (SEMI E72)**:
   - `physical.width_mm` (e.g. `3150`)
   - `physical.depth_mm` (e.g. `2450`)
   - `physical.height_mm` (e.g. `3000`)
3. **Wafer Sizes**: Select applicable sizes (e.g. `300 mm`).
4. **Category**: Select equipment class (e.g. `lithography`).
5. **Provenance Tiers**: Adjust provenance tiers per field (defaults to `inferred` honest uncertainty).
6. Live Conformance Progress Meter updates in real time to show L1 progress (`8/8 ✓`).

### Step 4: Submission & Transport Options

Contributors choose one of four delivery transports in the sticky action bar:

| Transport             | Prominence          | Behavior                                                                                                                             | Degraded State (Empty Config)                          |
| --------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| **Download JSON**     | **Primary (Green)** | Builds canonical JSON record and immediately triggers browser file download: `<sanitized-vendor>-<sanitized-model>-<short-id>.json`. | Always functional offline & on `file://`.              |
| **Copy to Clipboard** | Secondary           | Copies canonical JSON string to system clipboard; toast notification confirms copy.                                                  | Always functional.                                     |
| **Submit via GitHub** | Secondary           | Opens GitHub web editor (`/new/main?filename=submissions/pending/...`) to create file and initiate Pull Request.                     | Tooltip: `not configured — download the JSON instead`. |
| **Submit via Email**  | Secondary           | Triggers `mailto:` handler addressed to maintainer contact email with JSON in email body.                                            | Tooltip: `not configured — download the JSON instead`. |

### Step 5: Post-Submit Success Panel

Upon successful validation and export, the form smoothly transitions to the **Success State**:

- **Title**: `提交成功 · Submitted`
- **Record ID Display**: Displays immutable UUID (e.g., `9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d`) with a one-click copy button.
- **Three-Step Next Process Explanation** (Bilingual):
  1. _Maintainer Review_: Maintainers review specifications for authenticity and source integrity.
  2. _Schema Validation_: Automated Schema v1.0 syntax and constraint checks via `schemavalidator`.
  3. _Merge & Rebuild_: Ingestion into `output/records/` and catalog recompilation.
- **Action Buttons**:
  - `Download JSON Again`
  - `Copy Record ID`
  - `Copy JSON`
  - `Submit Another Record` (clears and returns to blank form)
  - `← Back to catalog`

---

## 3. Maintainer Path 维护者接收与上线指南

When a contributor submits an equipment specification (via GitHub Issue, PR attachment, or email), maintainers follow this exact sequence to validate, place, rebuild, and redeploy.

### Prerequisites 环境要求

All commands run from the repository root `<repo_root>` (or deployed server directory).  
Python virtual environment with dependencies (`jsonschema >= 4.18.0`):

```bash
source .venv/bin/activate
```

---

### Step 1: Save Submission to Staging File

Save the contributor's JSON payload into a staging directory:

```bash
mkdir -p staging
cat << 'EOF' > staging/incoming-tool.json
{
  "schema_version": "1.0",
  "record_id": "4b68e9a1-0df8-4f51-b844-3c66f91d848a",
  "conformance_level": "L1",
  "record_status": "submitted",
  "submitted_by": "Dr. Fab Engineer <fab.engineer@semiconfab.org>",
  "submitted_at": "2026-10-11",
  "updated_at": "2026-10-11",
  "identity": {
    "vendor": { "value": "ASML", "provenance": { "tier": "vendor_confirmed", "source": "https://www.asml.com" } },
    "model": { "value": "TWINSCAN NXT:2050i", "provenance": { "tier": "vendor_confirmed", "source": "https://www.asml.com" } },
    "category": { "value": "lithography", "provenance": { "tier": "inferred" } },
    "wafer_sizes_mm": { "value": [300], "provenance": { "tier": "vendor_confirmed" } }
  },
  "physical": {
    "width_mm": { "value": 3150.0, "unit": "mm", "provenance": { "tier": "inferred" } },
    "depth_mm": { "value": 2450.0, "unit": "mm", "provenance": { "tier": "inferred" } },
    "height_mm": { "value": 3000.0, "unit": "mm", "provenance": { "tier": "inferred" } }
  }
}
EOF
```

---

### Step 2: Automated Schema Validation (Schema Validator)

Run the official **Schema Validator** against the staged record:

#### Option A: Using `schemavalidator` CLI

```bash
PYTHONPATH=tools/validator python3 -m schemavalidator validate staging/incoming-tool.json --lang zh
```

**Expected Output ("Done" state)**:

```
Status: ✅ 校验通过
Summary: 记录结构与类型合法。达标等级: L1 (检测到: L1)。0 个错误, 0 个告警。
目标合规等级: L1
实际达标等级: L1
```

_(Exit code: `0`)_

#### Option B: Using standard `jsonschema` CLI

```bash
jsonschema -i staging/incoming-tool.json schema.json
```

_(Exit code: `0` with no error output)_

> [!NOTE]
> If validation fails (exit code `1`), reject the submission or comment back on the GitHub issue specifying the exact missing or malformed fields output by the CLI.

---

### Step 3: Migration Input Tree Placement

Determine the target folder based on conformance completeness:

1. **L1 Complete** (all 8 required fields present: `submitted_by`, `vendor`, `model`, `category`, `wafer_sizes_mm`, `width_mm`, `depth_mm`, `height_mm`):
   - Place into `output/records/`:
   ```bash
   # Generate canonical slug name
   SLUG="013_asml_twinscan-nxt-2050i.json"
   cp staging/incoming-tool.json output/records/${SLUG}
   ```
2. **If Upgrading an Existing Draft in `output/needs_footprint/`**:
   - Check if an incomplete record previously existed:
   ```bash
   OLD_DRAFT=$(find output/needs_footprint -iname "*twinscan-nxt-2050i*.json")
   if [ -n "$OLD_DRAFT" ]; then
     echo "Upgrading draft: $OLD_DRAFT"
     rm -f "$OLD_DRAFT"
   fi
   ```
3. **If Submitted as Incomplete Draft**:
   - Place into `output/needs_footprint/`:
   ```bash
   cp staging/incoming-tool.json output/needs_footprint/${SLUG}
   ```

**Expected "Done" State**:

- File is placed in `output/records/` (if complete) or `output/needs_footprint/` (if incomplete).
- Obsolete draft file (if any) is removed from `output/needs_footprint/`.

---

### Step 4: Re-Run Catalog Pipeline & Rebuild Artifacts

Execute the catalog builder script:

```bash
python3 tools/build_catalog.py output/ --output-dir .
```

**Expected Output ("Done" state)**:

```
Scanning for equipment records in: <repo_root>/output
Discovered 121 candidate JSON files.
Loaded schema.json successfully.
Emitted catalog.json: 121 entries -> <repo_root>/catalog.json
Emitted catalog-index.json: counts={'total': 121, 'l1': 8, 'draft': 113} -> <repo_root>/catalog-index.json

Summary:
  Total records: 121
  L1 verified:   8
  Draft records: 113
  Categories:    13
```

Verify that the updated catalog reflects the newly merged equipment:

```bash
python3 -c '
import json
with open("catalog-index.json") as f:
    idx = json.load(f)
print("Updated Index Counts:", idx["counts"])
'
```

---

### Step 5: Version Control Commit & Cloudflare Pages Redeployment

1. **Commit Changes**:
   ```bash
   git add output/ catalog.json catalog-index.json
   git commit -m "feat(catalog): merge submitted record for ASML TWINSCAN NXT:2050i (L1 verified)"
   ```
2. **Push to Remote (Triggers Cloudflare Pages Automatic Build)**:
   ```bash
   git push origin main
   ```
3. **Live Verification**:
   Query production endpoint:
   ```bash
   curl -s https://semiconfab.org/catalog-index.json | jq .counts
   ```
   **Expected "Done" state**:
   - Production JSON index shows updated `l1` count.
   - The equipment card on `https://semiconfab.org/catalog-demo.html` changes from amber draft status to verified L1 badge (`100% complete`).

---

## 4. Maintenance Checklist & Troubleshooting 运维排错清单

| Symptom 异常情况                                              | Root Cause 根因分析                                                   | Resolution 处置手段                                                                                                       |
| ------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `jsonschema.ValidationError: 'additionalProperties' false`    | Contributor submitted undocumented metadata fields at top level.      | Strip extraneous fields or move custom commentary into `notes: "..."`.                                                    |
| `ValidationError: 'inferred' is not of type 'number'`         | Contributor omitted the `.value` wrapper on a numeric metric.         | Ensure field conforms to `FieldValue<number>` schema with `{ "value": ..., "provenance": { "tier": ... } }`.              |
| Prefilled field has trailing or leading whitespace            | Browser URL decoding preserved `%20` as space padding.                | `add-equipment.html` automatically calls `.trim()` on `vendor` and `model` URL parameters during form prefill extraction. |
| `tools/build_catalog.py` reports lower L1 count than expected | One of the 8 mandatory fields is missing or contains an empty string. | Run `PYTHONPATH=tools/validator python3 -m schemavalidator validate <file>` to inspect detected vs target level.          |
