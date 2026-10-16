# Changelog

All notable changes to the SemiconFab source-available repository will be documented in this file.

---

## [1.3.0] - 2026-10-15

### In-Browser MIMAC-2026 Benchmark Demo (Pyodide WASM)

- **Interactive In-Browser Simulation**: Added zero-backend, browser-native simulation demo on `benchmark.html` (`#try-it`) using Pyodide (v0.27.7 WebAssembly Python runtime). Visitors can test dispatching policies (`FIFO`, `SPT`, `EDD`, `CR`) without downloading packages or setting up local Python environments.
- **Dedicated Web Worker Pipeline**: Offloads simulation (10-day warmup + 60-day run horizon) to a background Web Worker, keeping the main UI responsive. Stages progress indicators (`loading-pyodide` → `installing-simpy` → `loading-model` → `running` → `done`/`error`).
- **5 Core Performance Metrics**: Real-time rendering of Mean Cycle Time, Mean Tardiness, Wafer Throughput, Mean WIP, and TG01_LITHO Bottleneck Utilization, plus completed lots and wall-clock execution time.
- **Session History & Comparison**: Cumulative session history table allowing side-by-side comparison across multiple policy runs and seeds.
- **Honesty & Bilingual Standards**: Explicit honesty banners distinguishing the shortened interactive demo from the full 365-day multi-replication benchmark protocol; seamless bilingual toggle (`en-only` / `zh-only`) adhering to existing site design system.

## [1.2.0] - 2026-10-15

### Catalog expansion: 153 → 167 records

- **Equipment catalog**: 153 → **167 records** (8 L1 verified / 159 draft). Added 14 models from research batch 2 (TEL CLEAN TRACK ACT 8, Kingsemi FT300, ASML PAS 5500/60, Lam Sense.i, Lam TCP 9400, AMEC Primo nanova / Primo AD-RIE, AMAT Centura 5200, ASM Pulsar XP, AMAT Mirra Mesa, HHQK Versatile-GP300, KLA Surfscan SP7XP, SCREEN SU-3200, ACM Ultra C SAPS II); ASML PAS 5500/60 newly qualifies as L1 (full footprint). KLA `2920 Series` replaces `2920 Series Broadband Plasma Inspection` per naming decision.
- **Taxonomy preserved at 13 categories**: `tools/migrate.py` now refines DB segments into fab-meaningful categories (tracks → `resist_track`, defect-inspection tools → `inspection`) via explicit model lists, keeping twin bays, 3D colors and filters intact.

## [1.1.0] - 2026-10-15

### Catalog expansion: 121 → 153 records, deterministic record IDs

- **Equipment catalog**: 121 → **153 records** (7 L1 verified / 146 draft). Added 27 used-market models from SemiMarket pilot extraction (Canon FPA-5500iZ series, Nikon NSR steppers, TEL Tactras/Telius/Trias, Lam 2300/Vector/C3, AMAT Producer/Centura, ASM Dragon 2300, SUSSMicroTec MA200...), all `inferred` tier with per-listing source URLs; plus 5 DB-newer models (SKYVERSE SPRUCE-600, Changchuan QT-8000, C1/C3Q/C8, Lam Akara, Hanmi MSVP 6.0 Griffin) and 5 retained models absent from the research DB (TEL CLEAN TRACK ACT 12 / LITHIUS Pro Z, KLA 2920, AMAT UVision 4, Edwards iXH1820 — kept to avoid data loss; DB reconciliation pending).
- **Deterministic record IDs**: `tools/migrate.py` now derives `record_id` as UUIDv5 over `vendor||model||category` (was random UUIDv4). Catalog rebuilds are now stable — IDs no longer churn on every regeneration.
- **Cascading updates**: `twin/layout-default.json` (121 placements remapped), `js/catalog-fallback.js` (153 entries), `catalog-demo.html` demo records, `catalog-index.json` — all re-keyed to the new IDs; zero stale UUIDs site-wide.

## [1.0.0] - 2026-10-14

### Initial Source-Available Release

SemiconFab 1.0.0 provides a comprehensive, source-available 300mm advanced semiconductor wafer fabrication digital twin, equipment catalog, and fab operations benchmark testbed.

- **Architecture & Deployment**:
  - Purely static web architecture with zero server-side dependencies, optimized for static hosting (Cloudflare Pages, static web servers, or local `file://` execution).
  - Robust relative navigation and universal JSON schemas.

- **Licensing & Governance**:
  - Published under the **PolyForm Noncommercial License 1.0.0** (source-available). Free for education, study, and noncommercial research; commercial use requires a separate license (`info@semiconfab.org`).
  - GitHub repository: `https://github.com/jinjiefan2020/SemiconFab`.

- **Equipment Catalog (121 Records)**:
  - High-fidelity catalog spanning 121 representative semiconductor manufacturing tools across 13 cleanroom bays and 2 fab levels (L1 cleanroom floor and B1 subfab).
  - Strict 3-tier data standard (7 fully compliant L1 verified-footprint models, 114 draft records in pipeline awaiting physical dimensions).
  - Field-level provenance tracking and SEMI E10 operational state mappings.

- **Interactive 3D Cleanroom Digital Twin (`twin.html`)**:
  - Real-time WebGL/Three.js digital twin of a 300mm advanced semiconductor fab with dual-loop AMHS OHT ceiling monorail, ISO Class 1 laminar downflow aerodynamic simulation, and subfab utility network (UPW, PCW, CDA, high-purity gases, vacuum, exhaust).
  - Multi-level inspection (L1 cleanroom, B1 subfab, dual X-ray deconstruction, and exploded view).
  - Full support for uploading and previewing custom fab layouts dynamically.

- **Interactive 2D Fab Layout Editor (`layout-editor.html`)**:
  - Canvas-based 2D cleanroom floor plan editor supporting tool placement, 90° rotation, and deletion across 13 process bays.
  - Real-time design rule validation checking boundary limits and physical equipment envelope overlaps.
  - One-click "Open in 3D" preview and JSON export/import.

- **Equipment Submission Flow (`add-equipment.html`)**:
  - Community contribution form for new tool specifications conforming to Schema v1.0.
  - Dual submission flow: direct GitHub Pull Request creation and structured email submission.

- **MIMAC-2026 Operations Benchmark (`benchmark.html`)**:
  - Comprehensive discrete-event simulation benchmark suite (`mimac2026`) and Gymnasium environment (`FabEnv`) for 300mm wafer fab dispatching, AMHS routing, and opportunistic predictive maintenance.
  - Includes download simulator package (`downloads/mimac2026-simulator.zip`), technical specification (`MIMAC-2026-SPEC-v1.0.md`), and process route data (`benchmark/routes.json`).
