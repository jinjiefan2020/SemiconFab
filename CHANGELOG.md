# Changelog

All notable changes to the SemiconFab source-available repository will be documented in this file.

## [Unreleased]

### APC, FDC, SPC, Metrology & Yield (APC / FDC / SPC 与良率、量测与缺陷分析) Teaching Explainer (`fab-apc-yield-metrology.html`)

- **New Standalone Teaching Topic Page (`fab-apc-yield-metrology.html`)**:
  - Independent interactive explainer illustrating the closed-loop fab control cycle: how tool telemetry is monitored by FDC/SPC, how run-to-run recipe adjustments are computed, how inline metrology verifies dimensions, how defect distributions are analyzed on wafer maps, and how overall fab yield is aggregated.
  - Permanent bilingual honest banner (non-dismissible): "教学讲解，非真实 APC / 良率系统 · Teaching explainer, not a real APC / yield system", "数据、Trace、缺陷计数均为示意 · Data, traces, and defect counts are illustrative", "未连接任何真实工厂 · No live fab connection".
  - Six core concepts comparison table clearly separating definitions and scopes of SPC, FDC, APC, Metrology, Defect Analysis, and Yield without architectural conflation.
  - 10-step closed-loop causal architecture flow diagram (responsive SVG) and accessible text inventory sequence.
  - Interactive SPC Control Chart with strictly computed baseline control limits (Lots 1–10, Mean = 50.000, Sample StDev = 0.200, UCL = 50.600, LCL = 49.400), drift segment (Lots 11–18), and outlier point (Lot 19 = 51.200) triggering simplified Nelson Rule 1, Rule 2, and Rule 3 with full baseline/full-series toggles.
  - Interactive FDC Sensor Trace comparing nominal chamber pressure (25.0 mTorr) against a 10-point faulty deviation window (27.6–29.1 mTorr), triggering FDC ALARM at exactly t=19s (5 consecutive points exceeding threshold 27.0 mTorr) with good/faulty/overlay views.
  - Interactive APC Run-to-Run Proportional Feedback widget with worked example (Target 50.0, Measured 52.0, Adjustment -1.0, Next Setting 99.0) and live recalculation slider, accompanied by an explicit Feedback vs. Feedforward comparison.
  - Inline Metrology & Inspection scope table covering CD-SEM, Overlay, Film Thickness, Defect Inspection, and Electrical Test (WAT/PCM) with specific limitations and zero proprietary factory claims.
  - Defect Pareto & Wafer Map interaction using fixed counts (Particle 35, Scratch 20, Pattern defect 18, Contamination 15, Other 12; Total 100) with 4 signature wafer map patterns (Center cluster, Edge ring, Scratch line, Random) and mandatory non-diagnostic disclaimer captions.
  - Yield Waterfall Additive Loss Breakdown walkthrough using fixed arithmetic (1000 starts, -30 process scrap, -40 defect loss, -10 hold/scrap, 920 output, 92.0% yield) with explicit illustrative-only notice.
  - Neighboring systems comparison (MES, Connectivity Layer, Equipment, YMS) with live links to existing files.
  - Representative vendor landscape in two groups (APC/FDC/Yield and Metrology/Inspection) in strict alphabetical order preceded by disclaimer and followed by deployment qualifier.
  - Bilingual 10-term glossary (APC, FDC, SPC, R2R, CD, Overlay, Pareto, Wafer Map, Yield, Hold) and 3-question conceptual quiz (zero tracking).
  - Complete accessible static text edition ensuring full screen-reader and SEO readability without JavaScript.
  - Configurable sponsorship component default-disabled (`enabled: false`) with zero DOM footprint.
- **Dedicated Machine-Readable Data (`data/fab-apc-yield-metrology.json`)**:
  - Structured storage of SPC baseline numbers and Nelson rule triggers, FDC sensor traces, APC worked example parameters, Pareto counts, wafer map patterns, metrology types, neighbor boundaries, vendor landscape, glossary, and quiz.
- **Fab Operations Hub Status Updates (Both Topics Synchronized)**:
  - Updated both `apc-fdc-spc-yield` and `metrology-defect-analysis` from `planned` to `available` linking to `fab-apc-yield-metrology.html` in both `data/fab-operations.json` and `fab-operations.html`.
- **Site-Wide Discoverability & Navigation**:
  - **`js/site-nav.js`**: Added "APC, Yield & Metrology" / "APC 与良率量测" under the Learn dropdown and mobile drawer (`fabApcYield` / `fabApcYieldDesc`), activated for `fab-apc-yield-metrology`.
  - **`js/translations.js`**: Registered bilingual `fab_apc_*` localization dictionary keys for English and Chinese.
  - **`sitemap.xml`**: Added canonical clean URL entry `https://semiconfab.org/fab-apc-yield-metrology`.
  - **`README.md`**: Added single bullet pointing to the new APC, Yield & Metrology topic page.

### MES & Dispatch (MES 与派工调度) Teaching Explainer (`fab-mes.html`)

- **New Standalone Teaching Topic Page (`fab-mes.html`)**:
  - Independent interactive explainer explaining what a semiconductor MES does and what it does NOT do (ERP, equipment control, data lake, AMHS).
  - Permanent bilingual honest banner (non-dismissible): "教学讲解，非真实 MES · Teaching explainer, not a real MES", "Lot 与数字均为示意 · Lots and numbers are illustrative", "未连接任何真实工厂 · No live fab connection".
  - 8 core MES functions structured strictly according to SEMI / ISA-95 standards.
  - Interactive Toy Dispatching Simulator featuring 5 illustrative lots (Lot A–E) with strictly distinct processing times (8, 3, 6, 2, 5), allowing comparison of FIFO, SPT, EDD, and CR heuristics. Model assumptions (single tool, sequential, non-preemptive, no breakdown) and critical ratio definition explicitly documented; results independently calculated and verified.
  - 9-step interactive wafer lot lifecycle stepper (Create lot, Queuing, Dispatching, Recipe verification, Execution, Data collection, Metrology, Release or Hold, Next step) with handoff targets and missing-info impacts, including explicit Release / Hold branching.
  - 3 real-world exception scenarios (Recipe mismatch hold, tool breakdown re-dispatch, metrology out-of-spec hold) with state changes and reset capability.
  - MES and neighboring systems comparison table (ERP, EAP, AMHS/MCS, APC/FDC/SPC, YMS).
  - Representative vendor landscape in strict alphabetical order (Applied Materials SmartFactory, Critical Manufacturing MES, Dassault DELMIA Apriso, Eyelit MES, Siemens Opcenter Semiconductor) preceded by non-endorsement disclaimer and followed by custom extension reality note.
  - Complete 11-term bilingual glossary and 3-question conceptual quiz (click to reveal answer/explanation, zero tracking).
  - Complete accessible static text edition ensuring full screen-reader and SEO readability without JavaScript.
  - Configurable sponsorship component default-disabled with zero empty placeholder.
- **Dedicated Machine-Readable Data (`data/fab-mes.json`)**:
  - Structured storage of toy lot parameters, dispatching verification baseline, 9-step journey metadata, exception scenarios, neighbor systems, vendor landscape, glossary, and quiz.
- **Fab Operations Hub Status Update**:
  - Updated MES topic status from `planned` to `available` with href `fab-mes.html` in both `data/fab-operations.json` and `fab-operations.html`.
- **Site-Wide Discoverability & Navigation**:
  - **`js/site-nav.js`**: Added "MES & Dispatch" / "MES 与派工" under the Learn dropdown and mobile drawer (`fabMes` / `fabMesDesc`), activated for `fab-mes`.
  - **`js/translations.js`**: Registered bilingual `fab_mes_*` localization dictionary keys.
  - **`sitemap.xml`**: Added canonical clean URL entry `https://semiconfab.org/fab-mes`.
  - **`README.md`**: Added single bullet pointing to the new MES topic page.

### Fab Operations (晶圆厂运营总览) Architecture Hub & Operational Topic Map

- **New Standalone Hub Page (`fab-operations.html`)**:
  - Independent overview hub organizing existing SemiconFab modules and planned operational domains into one unified visual map.
  - Zero 3D/Three.js dependencies: pure vanilla JS and responsive SVG styled strictly with Nature/FT editorial design tokens (`css/semicon-theme.css`).
  - Permanent bilingual honest banner (non-dismissible): "教学总览，非真实工厂 · Teaching overview, not a real fab", "已上线与计划中严格区分 · Available and Planned are strictly separated", "未连接任何真实设备 · No live equipment connection".
  - Three navigation perspectives with in-page smooth anchor jumps: By Wafer Journey (`#view-journey`), By Architecture & Layers (`#view-layers`), and By Engineering Role (`#view-roles`).
  - High-level architecture map (SVG schematic) depicting physical wafer processing flow (Wafer In → Litho/Etch/Dep/CMP/Metrology loop → OSAT → Out) supported by 4 architectural tiers, complete with an accessible full text node inventory.
  - 4 Topic Groups (Operations Core, Facility & Environment, Process & Equipment, Business & People) with strict binary status badges (Available linking to real verified files / Planned non-clickable cards with `#contribute` jump).
  - Cross-flow synthesis explaining Material, Data, and Decision flows, contextualizing shop-floor connectivity without claiming live integration.
  - Educator & Contributor section (`#contribute`) and 5-point bilingual FAQ clarifying pedagogical scope, Planned topic rationale, zero-sponsorship stance, classroom application, and data provenance.
- **Dedicated Machine-Readable Index (`data/fab-operations.json`)**:
  - Structured index maintaining 4 topic groups, bilingual titles, strict binary status flags, real verified href targets, and scope descriptions.
- **Site-Wide Discoverability & Navigation**:
  - **`js/site-nav.js`**: Added "Fab Operations" under the Learn dropdown and mobile drawer with bilingual en/zh support (`fabOperations` / `fabOperationsDesc`).
  - **`index.html`**: Added dedicated `glass-card` in the primary capability grid placed after the Fab Data Layer card with `odr_fabops_*` localization keys.
  - **`sitemap.xml`**: Added canonical URL entry `https://semiconfab.org/fab-operations`.
  - **`README.md`**: Added single bullet pointing to the new operations overview.

### SEO & URL Redirection Harmonization (Google Search Console Fix)

- **Canonical URL Standardization**: Standardized all content pages to use clean canonical URLs without `.html` extensions or query parameters. Corrected canonical tags on `finfet`, `gaa`, `dram`, `nand`, `hbm`, and `guide`; added missing canonical tags to `compare`, `add-equipment`, `catalog-demo`, `benchmark`, `data-standard`, `verification`, `fab-capex`, `twin-osat`, and `twin-mega`.
- **Alternate & hreflang Sanitization**: Removed dirty `?lang=en` and `?lang=zh` alternate links from HTML `<head>` in device process pages (`finfet`, `gaa`, `dram`, `nand`, `hbm`). In `sitemap.xml`, eliminated duplicate localized hreflang alternates pointing to identical URLs, retaining single clean `x-default` per canonical page.
- **Sitemap.xml Rebuilt**: Reconstructed sitemap with 21 canonical clean URLs. Replaced `.html` entries, added missing `catalog-demo`, and updated `lastmod` to `2026-10-26` strictly for modified/added entries.
- **Eliminated Multi-Hop Redirect Stubs**: Updated redirect targets in `twin/index.html` (`/twin`), `benchmark/index.html` (`/benchmark`), and `submit-equipment.html` (`/add-equipment`) to directly target clean canonical URLs with query/hash pass-through, preventing 2-hop redirect chains.
- **Cleanroom Twin URL State Fix (`twin.html`)**: Fixed `switchEntryMode` in `twin.html` to eliminate automatic addition of default `?mode=visitor` parameter to the browser address bar on initial load while preserving interactive state restoration when explicit modes or modals are requested.
- **Site-Wide Internal Link Hygiene**: Replaced internal `.html` links across all HTML pages, navigation controllers (`js/site-nav.js`), and dynamic scripts (`js/i18n.js`) with clean canonical URLs.

## [1.9.0] - 2026-10-25

### Fab Data Layer (晶圆厂数据层) & Architecture Teaching Model

- **New Standalone Teaching Page (`fab-data-layer.html`)**:
  - Educational, interactive visualization explaining how wafer fab data flows layer-by-layer: from equipment to connectivity, MES, analytics, and planning/twin.
  - Zero 3D/Three.js dependencies: built entirely with responsive SVG and vanilla JavaScript aligned with Nature/FT editorial design tokens.
  - Permanent bilingual honest banner: "数据流为示意 · Data Flow Illustrative", "教学级模型，非真实工厂数据 · Teaching model, not real fab data", "未连接任何真实设备 · No live equipment connection".
  - 5 decoupled architectural layers: Equipment, Connectivity (EAP & SECS/GEM/EDA), Execution (MES), Analytics & Control (APC/FDC/SPC), and Planning, Simulation & Twin.
  - Interactive SVG cleanroom schematic with animated upward data pulses and play/pause controls, fully respecting `prefers-reduced-motion`.
  - 5-step wafer lot journey stepper (Litho → Etch → Deposition → CMP → Metrology) detailing 4 mandatory data breakdown items per step (data produced, protocol, consumer, if-missing impact).
  - 3 fault injection experiments (Connectivity Severed, Data Throttled/Delayed, MES Dispatch Delayed) demonstrating visual state changes, WIP accumulation, and explaining which layer alarms first in reality.
  - Expanded comprehensive pure text architecture covering 5-layer deep dive (SECS/GEM, GEM300, EDA Interface A, APC R2R, FDC, MES, YMS, DES simulation), 5-step wafer lot data journey, and latency QoS tiering.
  - Ergonomic layout refactor: moved the 4-item Lot Step Data Breakdown directly beneath the stepper controller in a 2x2 dashboard grid, eliminating dead space and unifying controller and breakdown view.
  - Configurable sponsorship slot (`sponsorship.enabled` in `data/fab-data-layer.json`, strictly default `false` with zero rendering or placeholders).
  - Deep-link support: `?layer=<id>` and `?tool=<vendor>-<model>` with runtime lookup against `catalog.json` (explicitly stating absence of connectivity protocol assumptions).
- **Dedicated Teaching Data Repository (`data/fab-data-layer.json`)**:
  - Independent structured JSON maintaining layer specifications, lot journey steps, fault scenarios, quiz definitions, and sponsorship configuration without bloating `catalog.json`.
- **Site-Wide Entry Points & Discoverability**:
  - **`twin.html`**: Added deep-link anchor in the equipment inspector drawer (`#inspector-panel`) pointing to `fab-data-layer.html`.
  - **`js/site-nav.js`**: Added "Fab Data Layer" (`dataLayer` / `dataLayerDesc`) under the **Learn (学习)** menu dropdown and mobile drawer with bilingual en/zh support.
  - **`data-standard.html`**: Added contextual callout link bridging equipment specification schema with shop-floor operational data flow.
  - **`index.html`**: Added new `glass-card` in the primary capability grid placed directly after the Fab Construction Cost card, fully localized with `odr_fabdata_*` i18n keys.
  - **`sitemap.xml`**: Added canonical URL entry `https://semiconfab.org/fab-data-layer`.
- **Strict Baseline Protection & Release Management**:
  - Zero diff on `twin-osat.html` (untouched).
  - Minimal 1-link diff on `twin.html` (zero changes to 3D scene, controls, or tour logic).
  - Upgraded project release version to **1.9.0** in `package.json`, `js/site-nav.js`, `guide.html`, `twin-mega.html`, and `vision.html`.

---

## [1.8.0] - 2026-10-19

### Site-Wide Information Architecture (IA) Refactoring & Navigation Unification

- **Unified 5-Category Navigation Architecture (`js/site-nav.js`, `index.html`)**: Refactored top navigation and mobile slide-out menus into 5 standardized categories with consistent English and Chinese bilingual labels:
  - **3D Twins (3D 孪生)**: 300mm Fab Cleanroom (`twin.html`), OSAT Packaging & Test (`twin-osat.html`), 2D Layout Editor (`layout-editor.html`).
  - **Equipment (设备库)**: Equipment Catalog (`catalog-demo.html`), Comparison Matrix (`compare.html`), Submit Equipment (`add-equipment.html`), Data Standards (`data-standard.html`), Verification Policy (`verification.html`).
  - **Cost (成本模型)**: Construction Cost Report (`fab-cost.html`), Capex Estimator (`fab-capex.html`).
  - **Learn (知识库)**: FinFET, GAAFET, DRAM, 3D NAND, HBM.
  - **Research (研究)**: MIMAC-2026 Benchmark (`benchmark.html`), Vision & 6 Pillars (`vision.html`).
- **Correction of Misleading Tags & Historical Labels**:
  - Corrected `benchmark.html` references from `"System Benchmarks"` / `"Hardware & WebGL Performance"` to **MIMAC-2026 Benchmark** (fab dispatching & scheduling benchmark).
  - Corrected `verification.html` references from `"Verification Suite"` / `"Automated Data Integrity Tests"` to **Verification** (data provenance & integrity verification policy).
  - Cleaned up navigation terminology: standardized "Facility Cost Report" to "Construction Cost Report", and aligned "Open Initiative" in nav to "Vision".
- **Cost Modeling Alignment & Cross-Link Banners (`fab-cost.html`, `fab-capex.html`, `js/fab-cost-i18n.js`)**:
  - Retitled `fab-cost.html` to **Fab Construction Cost Report · 晶圆厂建设成本研究报告** (Top-down parametric model) and added a prominent cross-link banner to `fab-capex.html`.
  - Retitled `fab-capex.html` to **Fab Capex Estimator · 晶圆厂总投资测算器** (Bottom-up cleanroom tool BOM model) and added a cross-link banner to `fab-cost.html`.
- **Site-Wide Catalog Count Alignment (253 Tools · 24 Categories)**:
  - Updated all outdated mentions of 167 tools / 13 categories across `index.html` (SEO meta tags, OpenGraph, Twitter cards, JSON-LD schemas, and hero/card text) and `js/translations.js` to **253 OEM equipment models across 24 categories** (167 front-end fab + 86 back-end OSAT).
- **Sitemap Index Expansion (`sitemap.xml`)**:
  - Added dedicated `<loc>https://semiconfab.org/twin-osat</loc>` entry directly adjacent to `/twin` with weekly update frequency and x-default/en/zh-CN hreflang links.
- **Strict Site-Wide Language Policy**:
  - Preserved full 9-language internationalization on the globalization portal (`index.html`).
  - Preserved 9-language dictionary architecture in `vision.html`.
  - Strict English and Simplified Chinese (EN / 简体中文) dual-language enforcement across all other pages.
  - Standardized the navigation language switcher button label to **`EN / 中文`** across all pages.
  - Added `window.I18N_LANG_ALLOWLIST` support in `js/i18n.js` and restricted `twin.html` language dropdown to English and Simplified Chinese.
- **Cleanroom Digital Twin Interaction Enhancements (`twin.html`)**:
  - Disabled automatic tour playback on initial entry, preserving user camera control for self-directed exploration.
  - Restricted cinematic inspection tour to a single full 5-station cycle before automatically stopping and restoring free orbit controls.
  - Positioned tour HUD details banner at the bottom center above the legend (`bottom-12`, matching follow-a-wafer panel layout) with elevated `z-index: 1000` to completely eliminate top status bar occlusion, guaranteeing unobstructed access to Skip, Previous, and Next buttons across all viewports.
  - Added a lightweight 3-step dismissible beginner onboarding bubble with `localStorage` persistent dismissal memory.
  - Enforced strict zero-reference rule with 0 links or text citations to `twin-osat.html`.
- **OSAT 3D Twin Viewport Optimization (`twin-osat.html`)**:
  - Added horizontal touch scrolling (`-webkit-overflow-scrolling: touch`, `touch-action: pan-x`) and mouse wheel horizontal scrolling support to the bottom 11 process category filter pills bar.
  - Elevated bottom pills bar layer to `z-30` and inspector panel to `z-40` to prevent pointer event occlusion.
- **Homepage Capability Cards URL Deduplication (`index.html`)**:
  - Mapped the 4 core capability cards to 4 distinct deep-link URLs: `twin.html` (3D cleanroom), `twin.html?modal=catalog` (253-tool OEM database modal), `twin.html?modal=yms` (cascading yield & wafer map), and `twin.html?mode=engineer` (SEMI E10 engineer telemetry mode).

---

## [1.7.0] - 2026-10-18

### Standalone OSAT Packaging & Testing Facility (`twin-osat.html`), Front-End Cleanroom Purification (`twin.html`) & 86 Tool Ingestion

- **Dedicated Standalone OSAT 3D Twin (`twin-osat.html`)**: Separated the OSAT packaging and testing facility completely from `twin.html` into a dedicated, high-performance standalone 3D twin page:
  - **Zero-Lag Offline & HTTP Architecture**: Inlined the 86-item OSAT ground-truth dataset directly into `<script id="osat-catalog-data">` (141 KB), achieving sub-100ms instant load times and 100% `file://` protocol compatibility without CORS browser restrictions.
  - **Centered Dual-Hall Coordinates**: Centered the facility at `(0, 0, 0)` (`x: [-54, 54]`, `z: [-25.5, 25.5]`, `H = 4.8m`) for optimal OrbitControls rotation, damping, and zooming.
  - **Assembly Hall (ISO 7 / ISO 8, West)**: Dedicated epoxy ESD flooring, overhead crane columns, and utility spiral ducts housing bays 1 to 7 (Dicing, Die Attach, Wire Bonding, Flip Chip, Molding, Singulation, Bumping/RDL).
  - **Final Test Hall (Data Center / Industrial, East)**: Raised anti-static flooring, CRAC precision cooling units with status LEDs, overhead busbars, and cable trays housing bays 8 to 11 (Prober, ATE, Handler, AOI Inspection).
  - **Central Logistics Spine & 10 Glowing Chevron Flow Arrows**: Features illuminated process chevrons and floating 11-step process flow bar guiding visitors through the post-wafer manufacturing lifecycle.
- **Front-End Fab Cleanroom Twin Purification (`twin.html`)**: Restored `twin.html` to its pure 300mm front-end pilot line focus by removing heavy procedural OSAT geometry and unneeded back-end equipment instances, reducing file size by ~200 KB and eliminating ballroom visual clutter. Added prominent `🏭 OSAT Twin →` cross-navigation pill buttons in header and camera toolbar.
- **Global Navigation Architecture (`js/site-nav.js`)**: Upgraded the top navigation "3D Twin" item to a rich dropdown featuring both "300mm Fab Cleanroom" (`twin.html`) and "OSAT Packaging & Test" (`twin-osat.html`), fully synchronized with mobile drawer, footer links, and bilingual switching.
- **86 OSAT Equipment Models Ingestion (`catalog.json`, `catalog-index.json`, `data/osat-86-ground-truth.json`)**: Expanded the global equipment catalog by 86 models across 23 Tier-1 vendors (DISCO, Accretech/Tokyo Seimitsu, ASMPT, Besi, Kulicke & Soffa, Shibaura Mechatronics, Toray Engineering, TOWA, Advantest, Teradyne, Cohu, Chroma, Hontech, FormFactor, MPI, Camtek, KLA, Onto Innovation, Nordson/CyberOptics, Viscom, ACM Research, Ultratech/Veeco). Total catalog count increased from 167 to 253.
- **11 Packaging & Testing Process Categories (`schema.json`, `twin/layout-schema.json`, `tools/migrate.py`)**: Defined and validated 11 official taxonomy keys: `osat_dicing`, `osat_die_attach`, `osat_wire_bonding`, `osat_flip_chip`, `osat_molding`, `osat_singulation`, `osat_bumping_rdl`, `osat_prober`, `osat_ate`, `osat_test_handler`, and `osat_inspection`.
- **Zero Fabrication & Strict Provenance Architecture**:
  - **55 Official Vendor Records**: Directly verified against official OEM product specifications and catalog brochures, classified under `provenance.source_tier: "vendor_confirmed"`.
  - **31 Trade Press Records**: Extracted from reputable technical trade press (Semiconductor Engineering, Chip1Stop, EE Times, SEMI), classified honestly under `provenance.source_tier: "inferred"`.
  - **TOWA Compression Mold Gap Row**: Preserved as `model: "(型号未公开)"` with `is_gap_row: true` to document industry adoption of undisclosed custom multi-strip compression molding architectures without fabricating model numbers.
- **Honest Envelope Rendering & Draft Shells**:
  - The 5 models with verified physical dimensions (Accretech SS20, Kulicke & Soffa Asterion, Chroma 3210, Nordson/CyberOptics MX3000, Viscom X7056-II) render with exact millimeter bounding envelopes and solid opaque PBR materials.
  - The remaining 81 unverified models render as lightweight draft instanced shells (nominal 2.2m × 2.6m × 3.2m envelope).
  - Inspector tool drawer displays a prominent amber honesty banner ("尺寸待实测 · Dimensions pending verification"), tier provenance badge, direct source citations, and a 1-click GitHub issue submission CTA prefilled with vendor and model parameters.
- **High-Fidelity Dynamic Logistics Simulation (`twin-osat.html`)**:
  - **4 Autonomous Mobile Robots (AMRs)**: Cleanroom-grade AGV/AMRs equipped with front/rear safety LIDAR bumpers, flashing beacon LED masts, and forward floor-projected blue safety warning spots (`BlueSpot`), carrying realistic FOUPs, leadframe strip magazines, and JEDEC trays.
  - **2 Cleanroom Technicians & Manual Stainless Trolleys**: Modeled technicians wearing ISO Class 7 white bunny suits, hoods, visors, and cleanroom boots pushing two-shelf stainless transport carts.
  - **Continuous Closed-Loop Corridor System**: Dual dedicated transport lanes (Eastbound at $z = +1.15$, Westbound at $z = -1.15$) with industrial yellow dashed floor markings, smooth 180° turnaround arcs ($r = 1.15\text{m}$, total length 175.2m), zero-collision parametric trajectory at $v = 2.2\text{ m/s}$, and isolated raycasting for undisturbed equipment inspection.
  - **Live Floating Telemetry Pill**: Real-time bilingual logistics status indicator (`● 自动化物流: 6 台运行中 (4台 AMR · 2台 人工推车)` / `● Logistics: 6 Active (4 AMR · 2 Trolleys)`).
- **Unified Equipment Catalog & Segmented Domain Switcher (`catalog-demo.html`)**:
  - Integrated high-performance domain switcher (`All Equipment (253)` | `Front-end FAB (167)` | `Back-end OSAT (86)`) with live dynamic category chips filtering (13 FAB vs 11 OSAT process categories).
  - Instant live stats recalculation (Total, L1 Verified, Draft) matching the active domain.
  - Deep linking support with URL search parameters (`?domain=osat`, `?domain=fab`, `?category=...`).
  - Updated offline embedded JSON cache to all 253 records for 100% `file://` compatibility.
  - Cross-linked `twin-osat.html` sidebar directly to `catalog-demo.html?domain=osat`.
- **Top Navigation Refinement (`index.html`, `js/site-nav.js`)**:
  - Replaced `add-equipment.html` ("Add your equipment") in `index.html` navigation with `catalog-demo.html` ("Equipment Catalog" / "设备目录") with `book-open` icon, strictly fulfilling the design system rule to maintain a focused, professional top navigation.
  - Updated site-wide navigation dropdown descriptions to `253 OEM Models (167 FAB · 86 OSAT)`.
  - Cleaned homepage layout flow by temporarily stashing the spotlight banner card.

---

## [1.6.0] - 2026-10-18

### Equipment Cross-Comparison & Full Catalog Price Estimates (`compare.html`, `catalog-demo.html`, `data/price_estimates.json`)

- **Full Catalog Price Estimates Dataset (`data/price_estimates.json`)**: Built a structured price estimate database covering 100% of the 167 catalog records (surpassing the ≥80% / 134-item threshold). Keyed deterministically by UUIDv5 `record_id`, each entry specifies engineering low/high USD ranges, equipment condition (`new`, `used`, `refurbished`), valuation basis (`reported`, `category_estimate`, `observed_listing`), estimation date (`2026-10`), and technical notes with verified public citation URLs.
- **Strict Honesty & Zero Fabrication Architecture**: Enforced strict provenance rules — 36 reported tools carry 100% verified, live public references (Reuters ASML disclosures, Tom's Hardware, STAR Market IPO prospectuses on sse.com.cn for AMEC, Hwatsing, ACM Research, Piotech, Skyverse, Kingsemi). SemiMarket B2B inquiry records were honestly classified under engineering category estimates noting the absence of public fixed price tags, guaranteeing 0 fabricated listings.
- **Dedicated Equipment Comparison View (`compare.html`)**: Authored a publication-grade side-by-side comparison matrix supporting 2 to 4 equipment tools. Features 10 cross-dimensional technical rows (vendor, model, category, conformance level, price range with basis badge, footprint dimensions, equipment weight, wafer sizes, process capabilities, provenance tier breakdown, data completeness, and source notes). Includes sticky metric headers, smooth horizontal scrolling, dynamic "+ Add Tool" picker modal with search, and one-click tool removal.
- **Dynamic Cross-Category Warning**: Integrated automated functional category detection. Compairing equipment across heterogeneous processes immediately triggers a prominent amber warning banner ("Cross-category comparison is for reference only").
- **Shareable Deep Links (`?compare=id1,id2`)**: Implemented two-way URL query synchronization (`window.history.replaceState`) and a 1-click "Share Comparison" button with clipboard toast notification, enabling instant reproduction of any comparison view across engineering teams.
- **Catalog Demo Interactive Integration (`catalog-demo.html`)**: Added comparison selection checkboxes to all 167 equipment cards with visual card highlights, rendered formatted price ranges with basis badges (`● Reported`, `● Category Estimate`), and built a slide-up floating comparison drawer displaying selected count (N/4), equipment tag pills, clear button, and direct navigation into comparison view.
- **Advance Pilot Line Subtitle & Full Localization (`twin.html`, `js/translations.js`)**: Added localized subtitle line (`Advanced Pilot Line` / `先进试验线` / `先端パイロットライン` / `첨단 파일럿 라인` etc.) directly below `300mm Semiconductor Fab` in the top-left brand header with pure 9-language i18n support (`twin_header_pilot_line`), clearly designating the 3D twin cleanroom as a balanced modular R&D pilot line prototype.
- **Fab Total Capex & Cleanroom Tool BOM Model (`fab-capex.html`)**: Built an Alpha-stage total fab capital expenditure estimator linking the 3D Cleanroom Digital Twin layout (`twin/layout-default.json`, 121 tools) with equipment price estimates and top-down parametric facility models (`fab-cost.html`). Supports Low/Median/High investment scenarios ($2.24B – $2.78B – $3.32B for modular pilot line), regional economic multipliers (Asia 1.0x, Europe 1.25x, US 1.35x), dynamic production scaling across 6 industry tiers (1.0x Pilot Baseline, 5.0x Specialty Fab, 10.0x Single-Phase Fab, 20.0x Dual-Phase MegaFab, 60.0x GIGAFAB® Campus, 80.0x Mega GIGAFAB® Campus), process bay capital allocation charts, top-down 7-subsystem facility breakdown, and an interactive 103-model cleanroom BOM table linked directly to comparison and catalog views.
- **Accurate GIGAFAB® Campus Nomenclature & HVM Allocation (8,000–12,000+ Main Tools)**: Strictly aligned terminology with global semiconductor foundry standards (e.g. TSMC Fab 18 Phase 1–8). Refactored 20.0x to "Dual-Phase MegaFab (~45k WSPM, ~2,920 tools)" and introduced 60.0x (~100k–120k WSPM, ~8,750 tools) and 80.0x (~150k+ WSPM, ~11,660 tools) to realistically model 4 to 8-phase contiguous cleanroom GIGAFAB® campuses operating 8,000 to 12,000+ main process and metrology tools. Normalizes lithography to realistic volume benchmarks (22%–25% WFE, ~17%–19% Total Capex) with full bilingual caveats.

### Unified Design System, Dual-Theme Engine (Light Default / Dark Option) & Mobile Responsive Adaptation (`css/semicon-theme.css`, `js/site-nav.js`)

- **Site-Wide Palette & Typography Alignment with `fab-cost.html` Editorial Standard (`css/semicon-theme.css`, `js/site-nav.js`)**: Aligned the color palette and typography across all static pages to match the highly-regarded publication aesthetic of `fab-cost.html`:
  - **Light Mode Warm Paper Palette**: Shifted from cold slate-50 (`#f8fafc`) to the warm linen/paper base (`--sc-bg-base: #f2f1ec`), pure white surface cards (`--sc-bg-panel: #ffffff`), warm stone subpanels/chips (`--sc-bg-subpanel: #e9e7df`), rich charcoal ink typography (`--sc-text-main: #1c2126`, `--sc-text-muted: #4c5560`, `--sc-text-dim: #7a838d`), subtle warm stone borders (`--sc-border: #d8d4c8`), and signature viridian teal accents (`--sc-accent-cyan: #0e6e6b`, hover `#0a5451`).
  - **Dark Mode Charcoal Navy Palette**: Deep charcoal navy base (`--sc-bg-base: #12161a`), slate card panels (`--sc-bg-panel: #1a2026`), secondary charcoal surfaces (`--sc-bg-subpanel: #232b33`), charcoal borders (`--sc-border: #333c45`), luminous off-white text (`--sc-text-main: #e8eaec`), and luminous mint teal accents (`--sc-accent-cyan: #3fbdb8`).
  - **Typography Standardization**: Standardized body text across all static pages to **Manrope** (`"Manrope", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`) and code/tabular numeric cells to **IBM Plex Mono** (`"IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace`).
  - **Component Harmonization**:
    - **Filter Chips & Category Badges (`.chip`)**: White background, warm stone border `#d8d4c8`, slate-charcoal text `#4c5560`, transitioning to solid viridian teal `#0e6e6b` with white text on active selection.
    - **Disclaimer & Callout Notes (`.disclaimer-note`, `.disclaimer-box`)**: Warm stone `#e9e7df` panel with `#d8d4c8` border and `#4c5560` text (7.0:1 contrast).
    - **Draft / Warning Alert Banners (`.draft-banner`)**: Soft amber callout `#fdf3e3` with `#b45309` border, `#b45309` title, and `#1c2126` text (9.2:1 contrast).
    - **Form Controls & Production Drivers (`.control-label`, `.control-value`, `.control-desc`)**: Rich ink `#1c2126` labels with viridian teal `#0e6e6b` metric indicators.
    - **Model Indicator Banners (`.model-indicator-box`)**: Pilot baseline renders in warm amber `#fdf3e3` with `#b45309` border and `#1c2126` title; HVM volume scale renders in soft teal `#e6f4f1` with `#0e6e6b` border and `#0a5451` text.
    - **BOM & Price Row Styling**: Prices render in high-contrast viridian teal `#0e6e6b` on warm stone `#e9e7df` backings with basis badges (`● Reported` in `#fdf3e3`/`#b45309`, `● Category Estimate` in `#e6f4f1`/`#0e6e6b`).
  - **Homepage & Vision Alignment (`index.html`, `vision.html`)**: Updated landing page and whitepaper theme variables, grid lines, and button gradients to seamlessly adopt the warm paper `#f2f1ec` tone and Manrope typography.
- **Theme Switcher & LocalStorage Persistence**: Integrated responsive theme toggle buttons (☀️ Light / 🌙 Dark, with bilingual label support) in the global desktop navigation header and mobile drawer. Automatically persists theme choice in `localStorage.getItem("semicon_theme")`, supports instant URL query overrides (`?theme=light` / `?theme=dark`), and evaluates theme state before initial render to eliminate FOUC (flash of unstyled content).
- **Cross-Component Theme Propagation**: Dispatches two-way synchronization via global `window.onSemiconThemeChange(theme)` callback, synchronizing legacy page calculators (e.g. `fab-cost.html` Day/Night toggles) and dynamically rendered charts/tables.
- **Unified Design System Token Architecture (`css/semicon-theme.css`)**: Standardized semantic tokens mapping `--bg-main`, `--bg-panel`, `--bg-card`, `--border-color`, `--text-main`, and `--text-muted` consistently to theme variables across all interactive pages.
- **Dynamic Site-Wide Navigation & Footer Controller (`js/site-nav.js`)**: Developed an auto-mounting navigation and footer controller (`#sc-header-mount` & `#sc-footer-mount`). Implements structured grouped menus (Digital Twin & 3D, Economics & Capex, Equipment & Standards, Initiative), active page detection, and synchronous bilingual language switching via global `window.onSemiconLanguageChange(lang)` hook and root `[data-lang]` propagation.
- **Mobile Responsive Drawer & Touch Ergonomics**: Integrated a full-screen slide-out mobile drawer with frosted backdrop (`backdrop-filter: blur(12px)`), animated hamburger toggle button, touch-friendly tap targets ($\ge 44\text{px}$), and automatic drawer collapse on link navigation or outside click.
- **Responsive Table & Grid Wrapping System**: Designed `.sc-table-responsive` providing sticky metric columns, horizontal smooth-scrolling, and custom scrollbars across the equipment comparison matrix (`compare.html`), cleanroom BOM breakdown table (`fab-capex.html`), benchmark test matrix (`benchmark.html`), and schema data standards (`data-standard.html`).
- **Complete Visual Unification Across 9 Static Pages**:
  - `fab-capex.html`: Piloted unified navbar and footer, corrected Alpha Version badge, and converted Production Scale controller into a full-width prominent driver card.
  - `compare.html`: Standardized side-by-side comparison matrix with unified header/footer, mobile drawer, and responsive metric cards.
  - `fab-cost.html`: Upgraded 10-link legacy header to unified navigation while preserving day/night theme toggling and parametric calculators.
  - `catalog-demo.html`: Replaced isolated header with unified navbar + sub-toolbar, fixed mobile card blowout to single-column stacking, and made the comparison floating drawer responsive.
  - `data-standard.html`: Converted discordant white light-theme pages into the unified dark slate cleanroom aesthetic, with responsive tables and synchronized bilingual toggle.
  - `verification.html`: Restyled schema validation suite into the dark slate aesthetic with unified navigation.
  - `benchmark.html`: Restyled industrial MIMAC-2026 benchmark into the dark slate aesthetic with responsive code blocks and tables.
  - `add-equipment.html`: Upgraded equipment submission forms, level selector cards, and floating save bar to dark slate styling.
  - `404.html`: Mounted unified navigation and footer for missing route handling.

---

## [1.5.5] - 2026-10-18

### Fab Construction Cost Breakdown Report & Parametric Estimator (`fab-cost.html`)

- **Bilingual Fab Construction Cost Report (`fab-cost.html`)**: Created a dedicated, publication-grade cost research report and parametric model analyzing where capital expenditures go beyond process tools (the remaining 20–30% in cleanroom, UPW, power, gases, HVAC, AMHS, land, and engineering design).
- **Interactive Parametric Estimator**: Built a real-time parametric cost model driven by process node anchors (2nm IBS, 2nm Samsung Taylor, 3nm IBS range, 5nm early TSMC Arizona, 28nm-class TSMC Kumamoto Fab 1, advanced DRAM SK hynix Yongin Y2) × monthly wafer capacity (WSPM) × facility share slider (20% to 35%) × regional construction timelines (Asia, US, Europe), with dynamic multi-tier cost breakdown and split visualizer.
- **Node Scaling & Dynamic SVG Chart**: Implemented node-scaling cost comparison per 1k WSPM with hand-authored SVG range chart and responsive dark/light palette synchronization.
- **Honesty Disclosure & Data Gaps Architecture**: Strictly observed data integrity red lines — zero fabrication/interpolation of unanchored nodes (e.g. 7nm omitted), clear preservation of all data confidence flags (`Weak source`, `IBS figures considered high`, `Not confirmed by TSMC`, `Treat with caution`), and explicit enumeration of the 8 unverified industry data gaps.
- **27 Verified Public Reference Links**: Included 19 categorized bibliographic entries containing 27+ live, verified citations across trade journals, engineering interviews, and corporate regulatory disclosures.
- **Comprehensive Multilingual i18n (`js/fab-cost-i18n.js` & `js/translations.js`)**: Implemented complete 1-click bilingual switching between English and Simplified Chinese across all 296 text keys, form inputs, dynamic calculator metrics, SVG charts, and responsive mobile card headers via `data-i18n-lbl`.
- **Homepage Strategic Feature Card (`index.html`)**: Integrated an amber-themed functional card in the open data & research grid adjacent to the MIMAC-2026 Benchmark card, adapting the layout cleanly to `grid-cols-1 md:grid-cols-2 xl:grid-cols-4`.
- **Global Navigation & Sitemap Integration**: Added `fab-cost.html` across site headers (`index.html`, `benchmark.html`, `data-standard.html`, `verification.html`, `404.html`) and XML sitemap index (`sitemap.xml`).

---

## [1.5.0] - 2026-10-18

### Demand-Driven AMHS Closed-Loop Traffic Simulation & UI Polish (`twin.html`)

- **Loop Traffic Simulation Engine**: Upgraded the AMHS (Automated Material Handling System) OHT monorail logistics from a decorative constant-speed loop into a demand-driven closed-loop traffic simulation across 24 ceiling vehicles (12 vehicles on Loop 1, 12 on Loop 2).
- **Bay Station Geometry & Derivation**: Established formal load port stations mapped directly from cleanroom tool positions in `twin/layout-default.json`: 7 stations on outer perimeter Loop 1 (265.3m) and 7 stations on inner inter-bay Loop 2 (196.1m), with arc-length coordinates ($s$) and process bay annotations.
- **Poisson Task Generation & NVF Dispatching**: Implemented a stochastic Poisson process (mean arrival interval ~4s) generating intra-loop point-to-point wafer transport tasks. Implemented Nearest Vehicle First (NVF) dispatching upstream of pickup stations with a FIFO task queue.
- **Kinematic Accel/Decel & Smooth Docking**: Integrated physical motion control ($s \in [0, L)$, $v_{\max} = 3.0\text{ m/s}$, $a = 1.5\text{ m/s}^2$). Approaching vehicles follow the parabolic braking profile $v(dist) = \min(v_{\max}, \sqrt{2 \cdot a \cdot dist})$ and dock with smooth station arrival speeds strictly $< 0.3\text{ m/s}$.
- **Car-Following Safety & Anti-Collision ($\ge 2.0\text{m}$)**: Implemented front-vehicle distance tracking. Vehicles enforce speed constraints when gap $< 4.0\text{m}$ and hard-stop when gap $\le 2.05\text{m}$ with strict step bounds, guaranteeing a minimum headway of $\ge 2.0\text{m}$ and zero overtaking.
- **Physical Hoist & Cargo Handling**: Replaced hardcoded fake actions with realistic 3.0s dwell cycles. Empty grippers descend, latch FOUPs at machine load port elevation ($y=2.1\text{m}$), and hoist them into vehicle carriages; at dropoff, FOUPs descend, unlatch, and empty grippers return aloft.
- **Multi-State LED Status Signaling**: Vehicles reflect real-time operational states via luminescent roof status bars: Emerald Green (`IDLE` cruising), Sky Blue (`TO_PICKUP` / `TO_DROPOFF`), and Amber (`LOADING` / `UNLOADING`).
- **Telemetry HUD Relocation & Bottom Stack Architecture**: Relocated the floating AMHS telemetry pill from the top toolbar to the bottom center directly above the legend bar, avoiding top-bar button overflow. Integrated into a unified vertical stack (`#bottom-center-hud-stack`) with Airflow and Heatmap telemetry panels, dynamically stacking upwards with flex-col-reverse. Docked the 2D floor plan editor trigger button (`#btn-edit-layout`) cleanly inside the bottom toolbar, completely eliminating horizontal and vertical overlapping across all resolutions.
- **Top Camera Presets & Action Buttons Hover Popover Tooltips**: Added dark semi-transparent frosted glass popover tooltips (`bg-slate-900/95` with subtle border and upward-pointing arrow) for all 7 camera preset buttons (Isometric, Top-Down, Litho Core, Cleanroom Air Shower, Roof/HVAC, Patrol Engineer, Reset) and Cinematic Tour button. Fully supports dynamic bilingual text in English and Simplified Chinese via `I18N_DICTIONARY` and `t()` without native browser tooltip delay or viewport clipping.
- **DOM Hierarchy Integrity**: Closed lingering container tags in `open-architecture-modal` and `bottom-hud-footer`, restoring strict well-formed HTML5 DOM tree structure.

## [1.4.0] - 2026-10-16

### "Follow a Wafer" Route Roaming & Roof / HVAC Infrastructure Layer (`twin.html`)

- **Follow a Wafer (Process Route Roaming)**: Integrated full 3D interactive route tracking across Products A (120 steps), B (104 steps), and C (92 steps) defined in canonical `benchmark/routes.json`. Features an amber-glowing FOUP carrier with point lighting, smooth Catmull-Rom spline interpolation visiting representative tools across all 18 tool groups mapped to `twin/layout-default.json`, a 30-segment fading path trail, follow/free camera tracking with OrbitControls auto-release, default 1x (with 4x/16x) playback speed controls with auto-play, seamless mutual exclusion with visitor cinematic inspection tour, and bilingual step metadata with mandatory honesty disclosure.
- **Roof & HVAC Facility Layer**: Added a comprehensive exterior roof and cleanroom HVAC infrastructure view ($y=8\text{m}$) rendered in solid PBR materials. Includes a 85m × 60m roof slab, 3 Make-up Air Units (MAU-1/2/3) with bilingual floating 3D sprites, triple main supply air ducts (`#7db8e8`) with vertical bay drop pipes reaching the ceiling grid ($y=5.22\text{m}$), 5 orange exhaust chimneys (`#e8935a`) with subtle rising particulate plumes, interactive duct hover tooltips, a dedicated `'roof'` camera preset, and schematic honesty badging without altering existing MEP/aerodynamic layer controls.
- **Navigation & Layout Alignment**: Repositioned Section clipping, Roof HVAC layer, and Follow a wafer action controls to the second-row status bar directly adjacent to YMS Map for a streamlined, uncluttered primary toolbar.

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
