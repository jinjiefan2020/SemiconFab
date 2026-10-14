# Changelog

All notable changes to the SemiconFab source-available repository will be documented in this file.

---

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
