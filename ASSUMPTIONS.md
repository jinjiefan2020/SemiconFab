# SemiconFab Architectural Assumptions & Decisions (ASSUMPTIONS.md)

This document records the architectural decisions, pedagogical trade-offs, engineering judgment calls, and data contracts established across the SemiconFab open semiconductor data and digital twin simulation platform.

---

## 1. Benchmark Specification & Architecture Assumptions

### Judgment Call 1: Complete 18-Row Master Equipment Table vs Truncated Summary (AC3, AC9)

- **Context**: Spec Table 1 defines 18 tool groups with 217 machines, covering serial scanners, batch furnaces, chemical benches, and metrology stations. For a web overview page, designers often consider truncating tables to the top 4–5 bottleneck groups (e.g. `TG01_LITHO`, `TG02_TRACK`, `TG03_ETCH`) with an ellipses placeholder.
- **Decision**: Render all 18 tool groups in full, character-identical to Table 1 of `MIMAC-2026-SPEC-v1.0.md`, including tool class, batch limits ($B_{\min}, B_{\max}$), availability ($A_g$), MTBF, MTTR, and setup families, explicitly summing to 217 machines.
- **Rationale**:
  1. _Implementation Certainty_: Researchers developing custom Gymnasium wrappers, discrete-event simulators, or mathematical programming models require complete machine inventories. Omitting batch furnace capacities (e.g., $B \in [2, 4]$ for `TG07`/`TG08`) or metrology station counts would force researchers to leave the page to locate missing parameters.
  2. _Verification Anchor_: A full 18-row table allows immediate verification of the stationary workload formula ($C_g = N_g \cdot A_g$) and confirms that the fab topology has not been simplified into a toy model.

---

### Judgment Call 2: Phrasing and Prominence of the Preliminary Results Caveat (AC5, AC6, AC9)

- **Context**: The preliminary T1 baseline results table was generated from 5 simulation replications, whereas the formal MIMAC-2026 evaluation protocol specified in §4 requires 30 replications with Common Random Numbers (CRN).
- **Decision**: The baseline results table prominently embeds the word `(Preliminary)` in the table title, in the surrounding English and Chinese narrative, and in the `Reps` column for all four rows. Section 9 (_Limitations_) bluntly reiterates that these numbers are 5-replication preliminary data.
- **Rationale**:
  1. _Academic Integrity_: In semiconductor manufacturing operations research, comparing novel dispatching or reinforcement learning policies against under-replicated baselines risks Type I statistical errors. Labeling preliminary data explicitly prevents authors from citing 5-run figures as definitive 30-run baselines.
  2. _Immediate Directional Utility_: Despite being preliminary, publishing 5-run figures confirms that the 4 behavioral sanity gates pass (e.g., bottleneck utilization at 88.30% inside the $[88\%, 93\%]$ band; Critical Ratio at 11.69 days directional superiority over FIFO at 17.46 days), giving researchers a tangible sanity check for their own local test runs.

---

### Judgment Call 3: Alternating Bilingual Paragraph Structure vs Tabbed UI Switching

- **Context**: The website supports both English and Chinese audiences. Content can be organized as monolithic language blocks, tabbed switches, or alternating bilingual paragraphs.
- **Decision**: Adopt an alternating paragraph structure (English paragraph immediately followed by its Chinese counterpart) across all 10 required sections.
- **Rationale**:
  1. _Markdown Portability_: `benchmark.md` is authored as portable content with YAML frontmatter, intended to be parsed by static site generators or read directly in repository viewers without requiring custom JavaScript tab components or CSS dependencies.
  2. _Search & Cross-Referencing_: Technical researchers comparing bilingual semiconductor terminology (e.g., "re-entrant routes / 循环重入工序", "overhead hoist transport / 天车物料传输") benefit from side-by-side linguistic alignment without having to toggle UI state.

---

### Judgment Call 4: Absolute Elimination of Promotional & Marketing Prose (AC7)

- **Context**: Product landing pages frequently rely on high-energy promotional phrasing to attract user engagement.
- **Decision**: Strictly prohibit all promotional and hyperbolic terminology (including "revolutionary", "next-gen", "cutting-edge", "game-changer", and "disruptive"). Use calm, precise mathematical and operational language throughout.
- **Rationale**: MIMAC-2026 is an open scientific benchmark. Hyperbolic language damages academic credibility among operations research scholars and semiconductor industrial engineers. Plain descriptions of physical constraints, synthetic modeling boundaries, and statistical test protocols establish durable trust.

---

### Judgment Call 5: Clean Standalone SVG Diagram without External Fonts or Scripts (AC8)

- **Context**: Overview diagrams often embed web fonts (e.g. Google Fonts) or external vector icons that fail to render when viewed offline or in local markdown previews.
- **Decision**: `diagrams/benchmark-overview.svg` is authored as valid standalone XML with system font fallbacks (`system-ui, -apple-system, sans-serif`), pure vector geometry (boxes and directional arrows only), inline styling, and bilingual labels across all 5 architecture columns.
- **Rationale**: Ensures the diagram renders consistently across all browser engines, local image viewers, and printed technical reports at standard 800px–1100px viewports without network requests or font substitution artifacts.

---

## 2. Cleanroom Digital Twin Assumptions

### Judgment Call 6: Event Stream Downsampling Balancing Client-Side Performance with Temporal Fidelity (AC4)

- **Context**: A full 30-day discrete-event simulation of the 217-machine MIMAC-2026 T1 dataset under continuous lot arrivals produces in excess of 150,000 state transitions. Loading an uncompressed 25+ MB JSONL file directly into browser memory would degrade initial page responsiveness on standard client hardware and mobile connections.
- **Decision**: Implement an importance-weighted downsampling pipeline (`scripts/generate_twin_events.py`) that strictly preserves 100% of critical events:
  - All 719 hourly fab-wide and per-step WIP snapshots (`wip_sample`).
  - All 1,779 raw wafer lot arrival events (`lot_spawned`).
  - All 1,668 unscheduled and scheduled maintenance transitions (`UDT` and `SDT`).
    High-frequency productive and standby operational state flips (`PR_productive` and `SBY_standby`) across non-bottleneck tool groups are downsampled by a stride factor of $k = 13$, while anchoring initial and terminal state boundaries.
- **Rationale**:
  1. _File Size Compliance_: Produces a 4.20 MB JSONL stream (`twin/events-t1-fifo.jsonl`), well within the $\le 5.0\text{ MB}$ static asset budget.
  2. _Statistical Accuracy_: WIP trajectory curves, machine MTBF/MTTR downtime frequencies, and bottleneck utilization heatmaps remain character-exact relative to the underlying 30-day simulation run without skipping critical breakdowns.

---

### Judgment Call 7: Visualizing Epistemic Uncertainty via Procedural Shaders and Ghost Meshes (AC1, AC2)

- **Context**: The open catalog contains 121 tool records, of which 7 possess verified dimensional envelopes (Level 1 detailed geometry) while 114 represent draft community contributions with unverified footprint measurements. Rendering all machines as polished, solid CAD enclosures would mislead viewers regarding data certainty.
- **Decision**: Physically map provenance tiers into WebGL material shaders:
  - Verified equipment (`vendor_confirmed`, `independent_verified`) renders as opaque solid PBR surfaces ($100\%$ opacity, specular metallic highlights).
  - Inferred equipment (`inferred`) renders at $45\%$ opacity with high-contrast edge wireframe highlighting and a 3D billboard tag (`inferred · 推断`).
  - Synthetic equipment (`synthetic`) renders at $25\%$ opacity with dashed contours and a 3D billboard tag (`synthetic · 合成`).
  - Draft tools with unmeasured dimensions (114 records) render as instanced cyan wireframe ghost boxes ($2.2\text{ m} \times 2.6\text{ m} \times 3.2\text{ m}$) with floating tags (`待补充 · dimensions pending`).
- **Rationale**:
  1. _Epistemic Honesty_: Visually separates peer-reviewed physical dimensions from crowdsourced estimates, reinforcing the source-available repository's rigorous verification standards.
  2. _Crowdsourcing Incentive_: Clicking any wireframe ghost directly navigates the user to the submission form with prefilled dimensional parameters (`prefill_url`), converting unverified records into an active crowdsourcing funnel.
  3. _GPU Draw Call Optimization_: Rendering 114 draft tools as a single `THREE.InstancedMesh` maintains a consistent 60 FPS frame rate on integrated GPUs.

---

### Judgment Call 8: Procedural Facing-Aisle Bay Slotting vs Hardcoded Coordinates (AC1)

- **Context**: In traditional 3D web visualizations, tool coordinates are statically hardcoded into JavaScript arrays. As new tools are added to `/catalog.json`, hardcoded layouts require manual 3D modeling and coordinate adjustments.
- **Decision**: Define 13 functional bay center anchors corresponding to catalog categories and procedurally slot tools into opposing service rows ($X_{\text{bay}} \pm 2.8\text{ m}$) along the bay service chase, automatically orienting tool front-end load ports toward the center aisle.
- **Rationale**:
  1. _Zero-Maintenance Growth_: Future additions or edits to `/catalog.json` instantly populate their designated bays without requiring any Three.js coordinate alterations.
  2. _Fab Design Realism_: Mirrored service rows reflect real-world fab ballroom architecture, separating clean service aisles (front load-port access) from gray chase utility corridors (sub-fab exhaust and chemical feeds).

---

### Judgment Call 9: Explicit Labeling of AMHS Vehicles as "示意 Illustrative" (AC7)

- **Context**: The cleanroom model features animated Overhead Hoist Transport (OHT) vehicles traveling on ceiling monorail tracks above the tool bays. However, the MIMAC-2026 T1 benchmark specification models lot transfer times as instantaneous rather than tracking physical vehicle routing delay.
- **Decision**: Prominently label all AMHS vehicles with a bilingual 3D billboard tag reading `"示意 Illustrative"` and explicitly state in the tour HUD and research panel that material transport in T1 is instantaneous.
- **Rationale**:
  1. _Scientific Transparency_: Avoids confusing operations research benchmarkers into believing that the digital twin is executing a track-level AMHS collision simulation.
  2. _Visual Context_: Retaining moving OHT vehicles provides indispensable spatial context for cleanroom ceiling height clearance, bay layout, and 300mm FOUP automation flow while remaining completely honest about model boundaries.

---

### Judgment Call 10: Category-Specific Procedural Generic Shells vs Bare Wireframes for Draft Tools

- **Context**: The 114 draft equipment records in `/catalog.json` with unverified physical dimensions were originally rendered as bare wireframe boxes with 114 always-on floating "待补充" billboard tags. User feedback indicated that the cleanroom ballroom appeared unfinished/skeletal and dense tag clutter impaired visual clarity.
- **Decision**: Replace bare wireframes with procedural generic shells across 5 visually distinguishable category silhouette families (`litho` tall stepped scanner, `thermal` vertical tube-stack, `bench` long low chemical bench, `cluster` multi-chamber mainframe pods, and `neutral` modular enclosure with load-port notch), while strictly anchoring the epistemic honesty signal in the _material shader_, _legend_, and _inspection metadata_:
  - **Draft Shader Material**: Translucent $25\%$ opacity desaturated cool-gray (Slate-400 PBR), accented with dashed edge highlights (`THREE.LineDashedMaterial`), unmistakably distinct from the $100\%$ opaque L1 verified solids at a glance.
  - **Explicit Legend Contract**: The legend states `"Draft Shell (25% 概念外形) — silhouette is a category-generic placeholder; dimensions pending verification."` Never label or imply these generic shapes represent real proprietary machine exteriors.
  - **Tag De-Cluttering**: Replace 114 always-on floating tags with distance-culled sparse tags showing at most $\le 12$ nearest to camera focus with smooth distance fade-out. Provide a top toolbar UI toggle `"待补充标签 / Pending labels"` (default: ON, sparse mode).
  - **Per-Bay Aggregate Badges**: Mount architectural 3D floating headers above each cleanroom bay (e.g. `"Litho Bay · 9 待补充"`), enabling instant at-a-glance awareness of unverified equipment per bay.
  - **Inspection Drill-Down & Prefill CTA**: Clicking any procedural shell opens the CAD inspection drawer with nominal placeholder badges (`2.20m × 2.60m × 3.20m 概念占位尺寸 · 尺寸待实测`) and an interactive prefill CTA linking to `/add-equipment?vendor=…&model=…`.
- **Rationale (Why generic shells do not violate the honesty contract)**:
  1. _Explicitly Generic Archetypes_: Geometry reflects category functional archetypes (e.g. optics turret step, furnace tube towers, chemical immersion deck) rather than fabricate false millimeter precision or proprietary OEM exterior styling.
  2. _Explicitly Draft Materiality_: The desaturated $25\%$ translucent cool-gray material with dashed contours provides an unmistakable visual break from verified solid machines.
  3. _Maintained Crowdsourcing Funnel_: Retains the high-conversion contributor path from 3D viewport into `/add-equipment` form prefill without visually polluting the cleanroom.
  4. _Zero Performance Regression_: Preserves GPU instancing (one `THREE.InstancedMesh` per silhouette family + a single merged `THREE.LineSegments` draw call for all dashed edges), maintaining a stable 60 FPS on integrated GPUs.

---

### Judgment Call 11: Pivot from Translucent Wireframe Ghosts to Solid Painted PBR Enclosures with Panel-Centric Honesty

- **Context**: While Judgment Call 10 introduced procedural silhouette families for the 114 draft tools, rendering them as $25\%$ translucent ghosts with dashed wireframe contours produced significant visual noise, translucent depth sorting artifacts, and an unfinished/skeletal aesthetic.
- **Decision**:
  1. **Solid Painted PBR Enclosures**: Replace all wireframe / dashed ghost meshes with solid, opaque cleanroom-white PBR enclosures (RAL 9010 cleanroom white, dark plinth base, dark load ports, subtle category accent stripes: litho amber, thermal copper, bench cyan, cluster cobalt, neutral sage) utilizing vertex colors within `THREE.InstancedMesh` (metallic 0.22, roughness 0.38). This completely eliminates wireframes, dashed lines, and depth sorting visual artifacts while preserving 60 FPS GPU instancing performance.
  2. **Panel-Centric Honesty Above the Fold**: Shift epistemic transparency strictly and prominently above the fold inside `#inspector-panel`:
     - Slate tier badge with dot status indicator (`#inspect-tier-dot` & `#inspect-tier-text`: `Draft Shell · 尺寸待实测`).
     - Prominent persistent warning banner: `"尺寸待实测 · Dimensions pending verification — 3D 场景展示为类别通用概念占位外形，物理包络尺寸未经实测核实 (Geometry shown is a generic placeholder)"`.
     - Direct crowdsourcing CTA button: `[+ 补充实测机台参数 (Add Equipment) →]` prefilled with `/add-equipment?vendor=…&model=…`.
     - Legend explicit disclosure: `"Draft shell — generic placeholder geometry, dimensions unverified. See the side panel for provenance."`
  3. **Universal SEMI E10 Machine Status Lights (All 121 Tools)**: Install physical status beacon tower lights (Andon towers) on _every tool_ across the cleanroom floor (7 verified + 114 draft):
     - Green (`0x10b981`): Productive (`PR_productive` / `RUNNING`).
     - Amber (`0xf59e0b`): Standby / Engineering (`SBY_standby` / `ENG_engineering` / `IDLE`).
     - Red (`0xef4444`): Unscheduled Down (`UDT_unscheduled_down` / `DOWN`).
     - Blue (`0x3b82f6`): Scheduled Down / Maintenance (`SDT_scheduled_down` / `MAINT`).
     - Status lights actively cycle with discrete operational simulation in visitor/engineer mode and synchronize to the 30-day MIMAC-2026 event scrubber in research mode.
  4. **Art Direction & Fab Lighting Refinement**: Eliminate flat/washed-out cleanroom lighting by reducing ambient light (`0.48`), boosting warm directional light with soft shadow radius, intensifying amber lithography room core glow, and fine-tuning floor epoxy specular response (`roughness: 0.36, metalness: 0.16`).
- **Rationale**:
  1. _Visual Cohesion & Immersion_: Solid cleanroom enclosures reflect real modern semiconductor fab aesthetics (cleanroom white aesthetic, heavy plinths, modular tool bay alignments) without sacrificing performance or epistemic integrity.
  2. _Epistemic Precision_: Shifting transparency into the metadata drawer above the fold prevents users from being misled regarding dimensional accuracy while keeping the 3D scene beautiful and uncluttered.
  3. _Alive Fab Floor_: Universal SEMI E10 status stack lights transform static CAD geometry into a pulsating, active digital twin that accurately mirrors semiconductor manufacturing realities across all operating modes.

---

## 3. Catalog Migration Assumptions

### Judgment Call 12: Completeness Percentage Formula Scope

- **Context**: The product requires an intuitive completeness progress indicator (`completeness_pct` from 0 to 100%) for each equipment card in the catalog.
- **Decision**: The completeness formula strictly counts only the **8 L1-required fields**:
  1. `submitted_by` (or `meta.submitted_by`)
  2. `identity.vendor`
  3. `identity.model`
  4. `identity.category`
  5. `identity.wafer_sizes_mm`
  6. `physical.width_mm`
  7. `physical.depth_mm`
  8. `physical.height_mm`
- **Formula**:
  $$\text{completeness\_pct} = \text{round}\left(\frac{\text{count of present L1 fields}}{8} \times 100\%, 1\right)$$
  - Each present field contributes exactly $12.5\%$.
  - When all 8 fields are present, completeness is $100.0\%$ and `conformance_level` is `"L1"`.
  - When any of the 8 fields are absent, `conformance_level` is set to `"draft"`.
- **Rationale**: Incorporating optional layers (e.g. `facilities`, `reliability`, `process_capability`, `commercial`) into the denominator would unfairly penalize tools that meet complete L1 physical envelope compliance, making it impossible for a cleanroom layout engineer to distinguish a fully verified L1 envelope tool from a partially drafted record.

---

### Judgment Call 13: Draft Record Schema Ingestion & Tolerant Validation

- **Context**: `schema.json` strictly requires `physical.width_mm`, `physical.depth_mm`, and `physical.height_mm`. However, product specifications mandate publishing all 121 records (7 L1 and 114 drafts) while still enforcing that every record must be validated against `schema.json` with `jsonschema` (skipping invalid files without crashing).
- **Decision**: `tools/build_catalog.py` implements a two-tier validation approach:
  1. **Strict L1 Validation**: Records asserting complete status must satisfy 100% of `schema.json` requirements without any validation errors.
  2. **Structural Draft Validation**: For draft entries, validation relaxes the mandatory `required` constraints on physical dimensions and wafer size, but strictly enforces data types (e.g. integer wafer sizes, positive numbers), closed enums (`categoryEnum`, `provenanceTier`), UUID formats, provenance object schema, and `additionalProperties: false`.
  3. **Non-crashing Skip Strategy**: Any file with corrupted JSON, illegal category enum values, or malformed top-level fields is logged as a warning to `stderr` and safely skipped, preventing catastrophic build failures.

---

### Judgment Call 14: Draft Acquisition Funnel UI Design

- **Context**: The catalog contains 114 incomplete records that lack physical cleanroom envelope dimensions or wafer sizes.
- **Decision**: Incompleteness is treated as an acquisition funnel rather than hidden as an error:
  1. **Default Visibility**: Filtering includes drafts by default. A "Hide incomplete records" checkbox is provided for advanced users but defaults to `OFF`.
  2. **Prominent Callout**: Every draft card displays a distinct amber CTA banner (`数据待补充 · Help complete this record`) that explicitly details which L1 fields are missing (e.g., `width_mm, depth_mm, height_mm`).
  3. **One-Click Prefill**: The CTA button links to `/add-equipment?vendor=...&model=...` with strict URL encoding, enabling engineers to jump directly into the contribution workflow with vendor and model pre-populated.

---

### Judgment Call 15: Safe URL-Encoding for Tool Model Nomenclature

- **Context**: Semiconductor equipment model designations regularly incorporate colons (e.g. `TWINSCAN NXT:2050i`), slashes (`2300 Versys Kiyo3X/Kiyo F Series`), spaces, and hyphens.
- **Decision**: Prefill URLs are generated using `urllib.parse.quote(val, safe="")`, ensuring that all reserved characters (including `:` and `/`) are encoded into RFC 3986 compliant percent-encoded strings (e.g., `%3A`, `%2F`).
- **Rationale**: This prevents query parameter parser breakage when URLs are shared across browser URL bars, team chats, and email clients.

---

## 4. Equipment Submission Form Integration Assumptions

### Judgment Call 16: Prefilled Form Fields Remain Fully Editable

- **Context**: When a contributor arrives at `/add-equipment` via a catalog draft card CTA (e.g. `?vendor=ASML&model=TWINSCAN%20NXT%3A2050i`), the form pre-populates `identity.vendor` and `identity.model`.
- **Decision**: Prefilled inputs remain **standard, unlocked, editable text inputs** rather than read-only or disabled fields. A visual tag (`来自目录 from catalog`) is attached to indicate prefill origin.
- **Rationale**:
  1. _Typo Remediation_: Source-available catalog drafts may have inherited minor spelling errors, capitalization oddities, or obsolete marketing suffixes from early ingestion scripts. Locking inputs would force contributors to abandon the form if they noticed a typo they couldn't correct.
  2. _Contributor Agency_: Cleanroom engineers often possess the exact revision plate number (e.g., adding a specific sub-variant suffix like `:2050i-B`). Allowing edits preserves user intent while still saving 95% of the typing effort.

---

### Judgment Call 17: Download JSON as the Primary Static Submission Transport

- **Context**: The site runs on purely static hosting (Cloudflare Pages) with no centralized database or API backend. We needed to choose the primary submission mechanism among file download, clipboard copy, GitHub Issues, and email mailto.
- **Decision**: **Download JSON** is prioritized as the primary (prominent green button) transport, followed by clipboard copy, with GitHub and email as secondary integrations.
- **Rationale**:
  1. _URL Length Limitations_: Advanced equipment records (especially L2 facilities maps and L3 multi-step process gas recipes) easily exceed 3,000–6,000 characters. Embedding entire JSON files in GET query strings (`mailto:?body=...` or `github.com/.../issues/new?body=...`) frequently exceeds browser/OS URL length boundaries (typically 2,048 to 8,192 bytes), resulting in truncated, invalid JSON payloads.
  2. _Zero Authentication Friction_: File download requires no GitHub account sign-in, corporate firewall bypass, or desktop email client setup (many cleanroom engineers operate on corporate webmail or sandboxed terminals where `mailto:` links fail).
  3. _Offline & `file://` Guarantee_: Client-side Blob download operates reliably offline, in disconnected fab intranets, and from direct `file://` browser launches with 100% byte integrity.

---

### Judgment Call 18: Graceful Degradation for Unconfigured GitHub & Email Endpoints

- **Context**: The `SUBMISSION_CONFIG` object ships with empty default values (`org: ""`, `repo: ""`, `contactEmail: ""`) for self-hosted mirrors, local clones, and unconfigured deployments.
- **Decision**: Buttons for GitHub and Email are visible in the action bar, but when clicked with empty configuration, they trigger an informative alert advising the user to use the primary Download option. In addition, the button `title` tooltip explicitly displays `not configured — download the JSON instead` (or Chinese equivalent).
- **Rationale**: Hiding the buttons entirely would obscure the pipeline's full capabilities from operators, whereas leaving broken links would result in 404 navigation or empty mail client crashes. Explicit tooltip degradation guides contributors along the golden path without disruption.

---

### Judgment Call 19: Strict XSS Inertness via DOM `textContent` and Property Assignment

- **Context**: URL parameters (`?vendor=...&model=...`) originate from untrusted external sources and can be crafted maliciously (e.g. `?vendor=<script>alert(1)</script>`).
- **Decision**: Query parameters are parsed strictly via `URLSearchParams` and injected into the DOM exclusively through `element.textContent` and `input.value`. Under no circumstances are URL parameters concatenated or interpolated into `innerHTML`, `outerHTML`, or `eval()`.
- **Rationale**: In modern single-page applications, DOM-based reflected XSS is a prevalent vulnerability when rendering URL query parameters. Using strict text nodes ensures any HTML tags or script elements are rendered as inert text strings without executing.

---

### Judgment Call 20: Post-Submit Success Panel Replaces Form View rather than Dismissable Modal

- **Context**: Following a valid submission, contributors need immediate confirmation, access to the immutable `record_id`, and instructions on what happens next.
- **Decision**: The post-submit success panel replaces the active form container within the document flow rather than popping up as a modal dialog overlay.
- **Rationale**: Modal overlays in responsive web pages are prone to accidental closure (e.g. accidental backdrop tap on mobile, pressing the Escape key, or clicking outside), which can panic the user into thinking their progress was discarded. An in-page state transition provides a calm, persistent receipt showing the `record_id`, idempotent re-download buttons, and an explicit "Submit another record" button to return to the form.

---

## 5. Data Standard & Verification Terminology Assumptions

### Judgment Call 21: `notes` Layer Representation & Semantics

- **Context**: In `schema.json`, `notes` is defined as a top-level string (`"notes": {"type": "string"}`), whereas Layers 1–6 are nested objects containing `FieldValue` wrappers. However, `SPEC.md` §3 lists `notes` as the seventh structural constituent (`Layer 7 — notes: Free-text remarks`).
- **Decision**: In `data-standard.md` and diagrams, we present `notes` explicitly as **Layer 7: 备注层 (Tribal Knowledge & Engineering Footnotes)** to maintain the 7-layer architectural narrative. We specifically document that `notes` contains unstructured contextual observations, lacks the `FieldValue` provenance wrapper, and is excluded from automated cross-tool comparison matrices.

---

### Judgment Call 22: `community_corroborated` Operational Criteria

- **Context**: The literal Chinese translation of "community" (社区) can connote casual online forum commentary or unverified crowdsourced public votes, which would compromise the credibility of an industrial equipment catalog.
- **Decision**: We translated `community_corroborated` as **“社区交叉确认”**, and established a strict, deterministic operational threshold: **data confirmed independently by two or more unrelated fab engineering teams, cleanroom facility technicians, or research institutions with numerical agreement within 5% tolerance**. This distinguishes peer-corroborated industrial field experience from unverified public speculation.

---

### Judgment Call 23: Alignment of Conformance Levels

- **Context**: The specification documentation anchors the conformance definitions directly to `SPEC.md` §7:
  - **L1 (Minimum Listing / 最低上架级)**: `meta` + `identity` + `physical` ("it exists and fits in the cleanroom").
  - **L2 (Fab Planning / 厂务规划级)**: `L1` + `facilities` (utilities and cleanroom hookups).
  - **L3 (Full Benchmark Grade / 完整基准级)**: `L2` + `process_capability` + `reliability` + `commercial` (simulation and drop-in tool comparison).
- **Decision**: Standardize all conformance documentation across `/data-standard`, `/verification`, and `/catalog-demo.html` on this exact 3-level progression.

---

### Judgment Call 24: Tone and Banned Superlative Guardrails

- **Context**: High-tech marketing copy frequently relies on superlative buzzwords that undermine the academic and industrial credibility of an equipment standard.
- **Decision**: A strict zero-tolerance lint check is enforced to exclude all banned marketing hype words. The copy maintains an objective, neutral, and confident tone grounded in SEMI/ISA-95 standardization, verifiable SI units, and provenance tracking.

---

### Judgment Call 25: Solo-Maintainer Verification Feasibility

- **Context**: The verification flow in `/verification` must balance rigorous anti-fraud gating against practical administrative operational limits for a single maintainer.
- **Decision**: We designed the gating mechanism to be deterministic:
  - Automation handles schema parsing, UUID validation, and SI unit compliance.
  - Initial submissions default strictly to `inferred`, preventing any automated elevation to `vendor_confirmed`.
  - Human review is scoped to two concrete checks: confirming the submitter's corporate email domain and verifying that the provided datasheet link directly substantiates the claimed dimensions and specifications.

---

## 6. Canonical Data Assets & Single Source of Truth

### Judgment Call 26: Byte-Identical Preservation of `catalog.json` and Event Streams

- **Context**: Formatting tools (e.g. Prettier) format JSON and text files according to general style rules. However, `catalog.json` (121 records, SHA256: `ebcf74a744105f1ea551433946eeb8556286b736a51d4947a3c8b76a879dc67a`) and `twin/events-t1-fifo.jsonl` represent canonical simulation and taxonomy contracts.
- **Decision**: Added `catalog.json`, `**/catalog.json`, `*.jsonl`, `schema.json`, and `benchmark/routes.json` directly to `.prettierignore`. All other application and documentation files are formatted with Prettier.
- **Rationale**: Guaranteeing that `catalog.json` retains its exact SHA-256 hash ensures that zero data drift occurs between releases.

---

### Judgment Call 27: Single Canonical Process Routes File (`benchmark/routes.json`)

- **Context**: Previous iterations contained duplicate copies of `routes.json` at repository root, in `benchmark/routes.json`, and in the simulator package.
- **Decision**: Retain `benchmark/routes.json` as the single canonical file across the entire repository. Root duplicates and simulator duplicates are removed. The simulator test suite (`benchmark/simulator/tests/test_routes.py`) points directly to `benchmark/routes.json`.
- **Rationale**: Single source of truth eliminates drift risk between the web documentation (`/benchmark/routes.json`) and the discrete-event simulation engine.

---

### Judgment Call 28: Canonical HTML Redirect for `submit-equipment.html`

- **Context**: `submit-equipment.html` was the early prototype implementation of the equipment submission web form. `add-equipment.html` (served at `/add-equipment`) superseded this, introducing URL parameter prefill, conformance scoring meters, and bilingual localization.
- **Decision**: Replaced duplicate logic in `submit-equipment.html` with an instant client-side redirect (`<meta http-equiv="refresh" content="0; url=/add-equipment">`) pointing to `/add-equipment`.
- **Rationale**: Eliminates duplicate validation logic and protects historical bookmarks or links without requiring server-side Cloudflare Pages configuration rules.

---

### Judgment Call 29: PolyForm Noncommercial 1.0.0 and Strict "Source-Available" Terminology

- **Context**: The project restricts commercial exploitation without a dedicated commercial agreement. While the codebase is freely accessible for study, research, and noncommercial fab modeling, applying the term "open source" would violate Open Source Initiative (OSI) criteria.
- **Decision**: Adopted the canonical **PolyForm Noncommercial License 1.0.0** and strictly standardized on the term **"source-available" / "源码公开"** across all files (`README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `package.json`, and all web page footers). Never write "open source" in new or modified files.

---

### Judgment Call 30: Decommissioning Cloudflare D1 & Functions in Favor of a Purely Static Architecture

- **Context**: SemiconFab previously included Cloudflare Pages Functions edge scripts and a Cloudflare D1 SQLite database (`semiconfab_db`). In practice, the digital twin (`twin.html`) and catalog viewer (`catalog-demo.html`) operate directly and reliably against the canonical static `catalog.json` without requiring edge SQLite queries. Maintaining edge serverless functions and an active D1 database introduced operational complexity and security attack surfaces.
- **Decision**:
  1. Fully decommission Cloudflare D1 database bindings and Pages Functions.
  2. Back up the remote Cloudflare D1 database (`semiconfab_db`) to a standalone SQL dump (`semiconfab_db.sql`) before decommissioning.
  3. Remove `functions/`, `d1/`, `admin-review.html`, client database connectors, and the D1 database binding in `wrangler.toml`.
  4. Retain all data submissions via GitHub Pull Requests, GitHub Issues, and email workflows (`mailto:info@semiconfab.org`), eliminating edge submission endpoints.
  5. Deploy SemiconFab as a purely static site to Cloudflare Pages edge network.
- **Rationale**: Purely static deployment on Cloudflare Pages guarantees maximum reliability, zero edge cold starts, global edge caching, and zero attack surface.

---

### Judgment Call 31: Cleanroom Sandbox Scope & Balanced Pilot Line Machine Ratios

- **Context**: An actual commercial 300mm leading-edge logic megafab (e.g., TSMC Fab 18, Samsung Pyeongtaek, 30k–50k+ WSPM) deploys between 500 and 1,000+ primary process tools. By contrast, the SemiconFab digital twin cleanroom models 121 tools across 13 bays to remain lightweight and fully interactive in standard client browsers.
- **Decision**:
  1. Explicitly document across all specifications: **“本洁净室为 SemiconFab 概念验证与全谱系设备编目孪生沙盒，集成了前道与后道代表性设备，但机台数量显著少于实际先进制程Fab。”** _(This cleanroom serves as a SemiconFab proof-of-concept and full-spectrum equipment catalog digital twin sandbox, integrating representative front-end and back-end equipment, with machine counts significantly lower than an actual high-volume advanced node semiconductor fab.)_
  2. Adopt a **balanced pilot line configuration (精简平衡线, 121 tools)** that honors real semiconductor operational physics:
     - **1:1 Litho-Track Inline Pairing**: Solves the previous 16:2 bottleneck by pairing 8 advanced EUV/ArFi scanners with 8 coater/developer tracks (`TG01_LITHO` : `TG02_TRACK` = 8 : 8).
     - **Multi-Patterning Etch & Deposition Ratios**: Allocates 18 dry etch tools and 18 thin film deposition tools (~2.25× scanner count) to reflect heavy SADP/SAQP and high-aspect-ratio FEOL/BEOL processing steps.
     - **Annex Separation**: Positions advanced packaging (12 tools) and final test (10 tools) in the East Wing annex, maintaining cleanroom architectural fidelity while preserving whole-value-chain visibility.
- **Rationale**: A browser WebGL application cannot render 1,000 unique CAD-detailed machines without GPU memory exhaustion. Calibrating the 121 tools to a realistic pilot line ratio preserves both academic honesty and operations research integrity.
