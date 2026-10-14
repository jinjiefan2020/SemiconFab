# Equipment Database Migration Report — Schema v1.0

Generated: 2026-10-11 | Source: fab_equipment_db.csv

## 1. Row Summary (行数统计)

- **Total Rows Read (读取总行数)**: 116
- **Emitted to `output/records/` (符合 Schema v1.0 标准已生成记录)**: 7
- **Emitted to `output/needs_footprint/` (缺失外形尺寸暂存记录)**: 109
- **Synthetic Values Emitted**: 0 (Strictly 0)

## 2. Equipment Category Distribution (设备类别分布)

| Category (Schema Enum) | Count | Percentage |
| ---------------------- | ----- | ---------- |
| `lithography`          | 16    | 13.8%      |
| `dry_etch`             | 15    | 12.9%      |
| `metrology`            | 14    | 12.1%      |
| `thin_film_deposition` | 12    | 10.3%      |
| `packaging`            | 12    | 10.3%      |
| `ion_implantation`     | 10    | 8.6%       |
| `test`                 | 10    | 8.6%       |
| `cmp`                  | 9     | 7.8%       |
| `wet_clean`            | 9     | 7.8%       |
| `thermal_processing`   | 9     | 7.8%       |

## 3. Wafer Size Parsing Breakdown (晶圆尺寸解析明细)

- **Parsed OK (成功解析)**: 91 (78.4%)
- **Omitted / Non-standard (留空 / 非标基底)**: 25 (21.6%)

### Raw CSV Values Distribution (原始值分布)

| Raw `wafer_size`                          | Count | Parsing Outcome                                                                                                  |
| ----------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------- |
| `300mm`                                   | 46    | Mapped to `[300]`                                                                                                |
| `300mm (unverified)`                      | 30    | Mapped to `[300]` (unverified in source)                                                                         |
| `N/A`                                     | 9     | Omitted (non-wafer / substrate / unverified)                                                                     |
| `unverified`                              | 8     | Omitted (non-wafer / substrate / unverified)                                                                     |
| `200/300mm`                               | 3     | Mapped to `[200, 300]`                                                                                           |
| `300/200mm`                               | 2     | Mapped to `[200, 300]`                                                                                           |
| `200mm & 300mm`                           | 1     | Mapped to `[200, 300]`                                                                                           |
| `200mm & 300mm (Si); 150mm & 200mm (HDD)` | 1     | Mapped to `[150, 200, 300]`                                                                                      |
| `<=300mm`                                 | 1     | Mapped to `[150, 200, 300]` (<=300mm interpreted as [150, 200, 300])                                             |
| `N/A (photomask)`                         | 1     | Omitted (non-wafer / substrate / unverified)                                                                     |
| `200mm (unverified)`                      | 1     | Mapped to `[200]` (unverified in source)                                                                         |
| `200mm & 300mm (bridge tool)`             | 1     | Mapped to `[200, 300]`                                                                                           |
| `100/150/200mm`                           | 1     | Mapped to `[150, 200]` (100mm dropped (not in schema enum))                                                      |
| `300mm (12 in)`                           | 1     | Mapped to `[300]`                                                                                                |
| `4-12 in wafer frames`                    | 1     | Mapped to `[150, 200, 300]` (Converted 4-12 in wafer frames to [150, 200, 300] mm; 100mm dropped (outside enum)) |
| `N/A (substrate max 300x100mm)`           | 1     | Omitted (non-wafer / substrate / unverified)                                                                     |
| `substrate 0.3x0.3-16x16mm`               | 1     | Omitted (non-wafer / substrate / unverified)                                                                     |
| `N/A (substrate max 105x300mm)`           | 1     | Omitted (non-wafer / substrate / unverified)                                                                     |
| `200 / 300mm`                             | 1     | Mapped to `[200, 300]`                                                                                           |
| `up to 200mm`                             | 1     | Mapped to `[200]`                                                                                                |
| `N/A (300x300mm bond area)`               | 1     | Omitted (non-wafer / substrate / unverified)                                                                     |
| `N/A (300x300mm work area)`               | 1     | Omitted (non-wafer / substrate / unverified)                                                                     |
| `4/6 inch`                                | 1     | Omitted (non-wafer / substrate / unverified)                                                                     |
| `panel`                                   | 1     | Omitted (non-wafer / substrate / unverified)                                                                     |

## 4. Provenance Tier Distribution (数据溯源可信度阶梯分布)

| Provenance Tier          | Emitted Values Count | Percentage |
| ------------------------ | -------------------- | ---------- |
| `community_corroborated` | 228                  | 33.0%      |
| `inferred`               | 218                  | 31.6%      |
| `vendor_confirmed`       | 174                  | 25.2%      |
| `independent_verified`   | 70                   | 10.1%      |

## 5. Top 10 Records Needing Human Review (优先人工审核记录)

| Row # | Vendor            | Model                 | Inferred Fields | Footprint Status        | Note              |
| ----- | ----------------- | --------------------- | --------------- | ----------------------- | ----------------- |
| 5     | ASML              | TWINSCAN NXE:3400C    | 6               | Missing (not published) | Missing footprint |
| 36    | Kokusai Electric  | TSURUGI-C2            | 6               | Missing (not published) | Missing footprint |
| 43    | KLA               | eDR7280               | 6               | Missing (not published) | Missing footprint |
| 54    | Ebara             | F-REX300              | 6               | Published ✓             | Valid L1          |
| 77    | ASM International | SONORA                | 6               | Missing (not published) | Missing footprint |
| 111   | Piotech           | PF-300T               | 6               | Missing (not published) | Missing footprint |
| 114   | SKYVERSE          | SPRUCE-800            | 6               | Missing (not published) | Missing footprint |
| 11    | Canon             | FPA-6300ES6a          | 5               | Published ✓             | Valid L1          |
| 28    | NAURA             | (model not disclosed) | 5               | Missing (not published) | Missing footprint |
| 37    | NAURA             | Cygnus PECVD          | 5               | Missing (not published) | Missing footprint |

## 6. Explicit Ambiguity Decisions (裁决记录清单)

1. **Metrology & Inspection Split Rule**: Models containing 'inspection' or 'defect' are mapped to `inspection`, all others mapped to `metrology`. (e.g. broadband plasma tools like 3935/2930 follow this rule as literal models).
2. **Wafer Size Frame Normalization**: '4-12 in wafer frames' on BESI Datacon 2200 EVO converted to `[150, 200, 300]`, dropping 100mm as outside the closed schema enum.
3. **Non-wafer Substrate Omission**: Rows with 'panel', 'N/A', 'photomask', or substrate dimensions omit `wafer_sizes_mm` entirely to preserve honesty.
4. **Multi-unit Dimensions Handling**: Ebara F-REX300 published main unit and power supply dimensions; main unit dimensions (W2700 x D4100 x H2500 mm) were parsed as primary cleanroom footprint.
5. **Zero Synthetic Tolerance**: No synthetic data was generated. Missing footprint dimensions are left out and records moved to `needs_footprint/` rather than inventing estimates.
