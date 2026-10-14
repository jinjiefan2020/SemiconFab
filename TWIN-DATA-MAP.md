# TWIN-DATA-MAP — Digital Twin Data Mapping Architecture

This specification document details the data contracts, spatial mappings, uncertainty-aware material shaders, event downsampling methodology, and multi-mode viewport controls implemented in the SemiconFab 300mm Cleanroom Digital Twin (`/twin`, `twin.html`).

---

## 1. Engine Scale Factor and Coordinate Reference

In the SemiconFab digital twin, coordinate units strictly conform to standard SI meters:

$$\text{1 Three.js Engine Unit} = 1.0 \text{ meter} = 1,000 \text{ millimeters}$$

### Coordinate Frame

- **$+X$**: Bay-perpendicular axis (traversing from West lithography bays to East backend/packaging bays).
- **$+Y$**: Elevation axis (cleanroom floor at $y = 0.0\text{ m}$; raised sub-fab perforated tiles at $y = 0.0\text{ m}$; tool service envelope $y \in [0, 3.8\text{ m}]$; AMHS OHT monorail tracks at $y \in [5.8\text{ m}, 6.2\text{ m}]$; HEPA/ULPA FFU plenum ceiling at $y = 5.22\text{ m}$ for litho and $y = 6.2\text{ m}$ for general bays).
- **$+Z$**: Bay-longitudinal axis (along cleanroom center and chase access aisles, extending from $z = -42\text{ m}$ to $z = +42\text{ m}$).

### Physical Sizing Formula

All cataloged equipment records specifying physical dimensions in millimeters are scaled directly into engine units:
$$W_{\text{engine}} = \frac{\text{width\_mm}}{1000}, \quad D_{\text{engine}} = \frac{\text{depth\_mm}}{1000}, \quad H_{\text{engine}} = \frac{\text{height\_mm}}{1000}$$

When dimension fields are unverified or omitted (`draft` tier), the engine assigns a standardized nominal tool envelope:
$$W_{\text{nominal}} = 2.20\text{ m}, \quad D_{\text{nominal}} = 2.60\text{ m}, \quad H_{\text{nominal}} = 3.20\text{ m}$$

---

## 2. Category to Cleanroom Bay Layout Mapping

> [!NOTE]
> **洁净室沙盒定位与先进制程机台规模说明 / Sandbox Scope & Machine Count Disclosure**:  
> **本洁净室为 SemiconFab 概念验证与全谱系设备编目孪生沙盒，集成了前道与后道代表性设备，但机台数量显著少于实际先进制程Fab。**  
> _(This cleanroom serves as a SemiconFab proof-of-concept and full-spectrum equipment catalog digital twin sandbox, integrating representative front-end and back-end equipment, with machine counts significantly lower than an actual high-volume advanced node semiconductor fab.)_
>
> 在实际商业量产的 7nm/5nm/3nm Megafab（月产能 30k~50k+ WSPM）中，主制程设备总量通常在 500~1,000+ 台。本沙盒基准采用精简平衡线设计（121 台）：重点保证 **光刻与涂胶显影 1:1 在线串联配比**（Litho : Track = 8 : 8）、**多重图案化高负荷刻蚀与薄膜沉积加倍配置**（Dry Etch : Litho ≈ 2.25 : 1，Thin Film : Litho ≈ 2.25 : 1），并将后道先进封装与测试设立为独立专属附楼，以在有限且交互流畅的浏览器 3D/2D 算力预算内完整传达先进制程物流与工艺结构。

The 121 cataloged semiconductor equipment records (covering 13 categories) are procedurally mapped into designated functional bays across the 300mm wafer cleanroom ballroom and packaging annex. Each bay assigns equipment into facing service rows along designated chase and service aisles.

| #   | Catalog Category Key   | Cleanroom Bay Name (EN / ZH)                           | Bay Center $(X, Z)$                | Environment & Airflow Spec                                          |
| --- | ---------------------- | ------------------------------------------------------ | ---------------------------------- | ------------------------------------------------------------------- |
| 1   | `lithography`          | Lithography Scanner Bay (黄光光刻区)                   | $(-24.0\text{ m}, -12.0\text{ m})$ | Class 1 (ISO 3), 560nm Amber Safe-Light, Vibration Baseline VC-E    |
| 2   | `track`                | Coater & Developer Bay (涂胶显影区)                    | $(-24.0\text{ m}, 12.0\text{ m})$  | Class 1 (ISO 3), Yellow Chem Filtering, Linked to Scanners          |
| 3   | `etch`                 | Dry Plasma Etch Bay (等离子干法刻蚀区)                 | $(-12.0\text{ m}, -18.0\text{ m})$ | Class 10 (ISO 4), Chlorine/Fluorine Toxic Exhaust, RF Grounding     |
| 4   | `deposition_cvd`       | CVD & PECVD Thin Film Bay (化学气相沉积区)             | $(-12.0\text{ m}, 6.0\text{ m})$   | Class 10 (ISO 4), Silane/Phosphine Abatement, Thermal Vacuum Lines  |
| 5   | `deposition_ald`       | Atomic Layer Deposition Bay (原子层沉积区)             | $(-12.0\text{ m}, 24.0\text{ m})$  | Class 10 (ISO 4), High-Purity Inert Gas Purge, Low-Temp Precursors  |
| 6   | `deposition_pvd`       | PVD & Sputtering Metal Bay (物理气相沉积区)            | $(0.0\text{ m}, -24.0\text{ m})$   | Class 100 (ISO 5), Ultra-High Vacuum Turbomolecular Pumps           |
| 7   | `implant`              | High-Current Ion Implant Bay (离子注入区)              | $(0.0\text{ m}, 0.0\text{ m})$     | Class 100 (ISO 5), High-Voltage Radiation Shielding, Toxic Hydrides |
| 8   | `thermal`              | Oxidation & Diffusion Furnace Bay (高温扩散区)         | $(0.0\text{ m}, 24.0\text{ m})$    | Class 100 (ISO 5), Quartz Tube Batches, High Thermal Dissipation    |
| 9   | `wet`                  | Wet Cleaning & Chemical Bench Bay (湿法清洗区)         | $(12.0\text{ m}, -24.0\text{ m})$  | Class 10 (ISO 4), Acid/Solvent Drain Segregation, Exhaust Scrubbers |
| 10  | `cmp`                  | Chemical Mechanical Planarization Bay (化学机械抛光区) | $(12.0\text{ m}, 0.0\text{ m})$    | Class 100 (ISO 5), Slurry Distribution Loop, High UPW Influx        |
| 11  | `metrology_inspection` | Metrology, CD-SEM & Ellipsometry (测量检测区)          | $(12.0\text{ m}, 24.0\text{ m})$   | Class 10 (ISO 4), Acoustic Isolation, Active Anti-Vibration         |
| 12  | `packaging_advanced`   | Advanced Packaging & Hybrid Bonding (先进封装区)       | $(24.0\text{ m}, -12.0\text{ m})$  | Class 100 (ISO 5), Sub-Micron Thermo-Compression & Die Bonders      |
| 13  | `test`                 | Automated Wafer Probing & Test Bay (晶圆测试区)        | $(24.0\text{ m}, 12.0\text{ m})$   | Class 1000 (ISO 6), High Electrical Pin Count, Chiller Systems      |

### Automatic Procedural Growth

When catalog entries grow beyond the initial 121 models, `computeBayToolSlots()` automatically arranges equipment in two facing rows along the $Z$-axis within each bay:

- **Left Row**: $X = \text{bay}_x - 2.8\text{ m}$, Tool Yaw $= +\pi/2$ (facing center aisle).
- **Right Row**: $X = \text{bay}_x + 2.8\text{ m}$, Tool Yaw $= -\pi/2$ (facing center aisle).
- **Pitch Along Row**: $\Delta Z = \max(W_{\text{engine}}, 3.2\text{ m})$ to guarantee ergonomic maintenance access without overlapping geometry.

---

## 3. Data Tier to Material Uncertainty Contract

The twin visualizes data epistemic uncertainty directly in WebGL materials to prevent giving a false impression of millimeter-level fidelity for unconfirmed models.

| Data Provenance Tier               | Visual Shader Representation                                                                                                                                                                                          | Opacity & Wireframe                                               | 3D Floating Tag                                          | Tooltip & Inspection Badge                                                                                                                                                                                                       |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `independent_verified`             | Opaque Solid PBR Material (Metallic 0.35, Roughness 0.38)                                                                                                                                                             | $100\%$ Opacity, No Wireframe                                     | None (clean 3D scene)                                    | Green Badge: `verified · 独立核实` (displayed in header & above CAD Elevation)                                                                                                                                                   |
| `vendor_confirmed`                 | Opaque Solid PBR Material (Metallic 0.25, Roughness 0.45)                                                                                                                                                             | $100\%$ Opacity, No Wireframe                                     | None (clean 3D scene)                                    | Blue Badge: `vendor · 厂商确认` (displayed in header & above CAD Elevation)                                                                                                                                                      |
| `inferred`                         | Semi-transparent Hull + Highlighting Wireframe Overlay                                                                                                                                                                | $45\%$ Opacity (`depthWrite: false`), Neon Accent Edges           | None (clean 3D scene)                                    | Amber Badge: `inferred · 推断` (displayed in header & directly above CAD Elevation)                                                                                                                                              |
| `synthetic`                        | Translucent Shell + Dashed Edge Contours                                                                                                                                                                              | $25\%$ Opacity (`depthWrite: false`), Dashed Edges                | None (clean 3D scene)                                    | Purple Badge: `synthetic · 合成` (displayed in header & directly above CAD Elevation)                                                                                                                                            |
| `draft` (generic procedural shell) | Solid Painted PBR Enclosure (RAL 9010 cleanroom white body, dark plinth base, category accent stripes: litho amber, thermal copper, bench cyan, cluster cobalt, neutral sage) + Universal SEMI E10 stack light beacon | $100\%$ Opacity Solid Painted PBR, Zero Wireframes / Dashed Lines | None (clean 3D scene; per-bay aggregate badges retained) | Slate Badge + Tier Dot (`Draft Shell · 尺寸待实测`); Above-the-fold Honesty Banner (`尺寸待实测 · Dimensions pending verification`); Status Tag above CAD Elevation (`待补充 · Pending`); Above-the-fold CTA to `/add-equipment` |

### Level of Detail (LOD) & Status Light Contract

- **Principle**: _"3D is for beauty, the side panel is for honesty."_
- **Clean 3D Scene**: All 3D floating tag billboards over equipment ("待补充 pending", "inferred 推断", "synthetic 合成") have been completely removed from the 3D scene to preserve pristine cleanroom visual aesthetics. Provenance authenticity is surfaced directly inside the inspector panel in a dedicated status tag bar mounted immediately above the 1:50 CAD Elevation view (`#inspect-elevation-tag-bar`).
- **L1 Detailed Geometry** (7 records, e.g. `Canon FPA-5550iZ2`, `Canon FPA-6300ES6a`, `Canon FPA-1200NZ2C`, `Ebara F-REX300`, `ACMR Ultra ECP 3d`, `BESI Datacon 2200 EVO`, `SRII SRII-4.5M`): Rendered at verified envelope dimensions, equipped with load ports (dual/triple 300mm FOUP nests), 4-tier Andon status beacon light towers, interactive click targets, and SEMI E10 operational state lighting.
- **Draft Solid Procedural Shells** (114 records): Rendered via category-specific generic silhouette families (`THREE.InstancedMesh` with vertex colors per family, metallic 0.22, roughness 0.38). The solid painted shell eliminates wireframe noise and translucent depth-sorting artifacts while preserving GPU instancing. Each shell is equipped with an Andon status light pole + emissive beacon cylinder.
- **Universal SEMI E10 Machine Status Lights (All 121 Tools)**: Every machine on the cleanroom ballroom floor features active physical stack lights mapping live fab states:
  - **Green (`0x10b981`)**: Productive (`PR_productive` / `RUNNING`).
  - **Amber (`0xf59e0b`)**: Standby / Engineering (`SBY_standby` / `ENG_engineering` / `IDLE`).
  - **Red (`0xef4444`)**: Unscheduled Down (`UDT_unscheduled_down` / `DOWN`).
  - **Blue (`0x3b82f6`)**: Scheduled Down / Maintenance (`SDT_scheduled_down` / `MAINT`).
  - _Modes_: Dynamically driven by live simulation clock in visitor and engineer modes, and synchronized to the 30-day discrete-event simulation timeline scrubber in `?mode=research`.
- **Panel-Centric Honesty (Above the Fold & Above CAD Elevation)**: Selecting any draft or inferred tool surfaces epistemic provenance prominently in `#inspector-panel`:
  1. A slate tier badge with status dot indicator (`Draft Shell · 尺寸待实测`).
  2. A persistent amber honesty banner: `"尺寸待实测 · Dimensions pending verification — 3D 场景展示为类别通用概念占位外形，物理包络尺寸未经实测核实 (Geometry shown is a generic placeholder)"`.
  3. A dedicated provenance status tag mounted directly above the CAD Elevation whiteprint: `[数据状态 / Status: 待补充 · Pending]` or `[数据状态 / Status: inferred · 推断]`.
  4. A prefilled crowdsourcing contribution CTA button: `[+ 补充实测机台参数 (Add Equipment) →]` pointing to `/add-equipment?vendor=…&model=…`.
- **Cleanroom Architectural Headers**: Cleanroom bay headers feature prominent aggregate badges (e.g. "Litho Bay · 9 待补充") providing spatial awareness without per-machine clutter.

---

## 4. MIMAC-2026 Event Stream and Downsampling Methodology

### Source Event Log Generation

The simulation event stream is generated directly by running the validated MIMAC-2026 T1 discrete-event simulator (`benchmark/simulator/mimac2026/sim.py`) configured with the deterministic FIFO scheduling baseline over a continuous 30-day run ($T = 720.0\text{ hours}$):

```bash
python scripts/generate_twin_events.py \
  --days 30 \
  --policy fifo \
  --seed 42 \
  --output events-t1-fifo.jsonl \
  --downsample-factor 13
```

### Downsampling Algorithm & Budget Guarantee

To comply with the static web asset delivery budget ($\le 5.0\text{ MB}$ uncompressed for instantaneous client-side streaming and mobile compatibility), the event generator enforces an importance-weighted filter:

1. **$100\%$ Preserved Critical Events**:
   - `wip_sample`: 719 hourly fab-wide and per-step WIP snapshots ($100\%$ preserved for smooth continuous curve rendering).
   - `lot_spawned`: 1,779 raw wafer cassette injection events ($100\%$ preserved for accurate lot lineage).
   - `tool_state_change (UDT / SDT)`: 1,668 unscheduled and scheduled maintenance events ($100\%$ preserved to capture breakdown events).
2. **Downsampled High-Frequency Events**:
   - `tool_state_change (PR_productive / SBY_standby)`: Downsampled with integer stride $k = 13$ across non-bottleneck groups while strictly preserving the initial and terminal state transitions of each tool.
3. **Resulting Stream Footprint**:
   - Total Events: 27,263 discrete structured JSON lines.
   - File Size: Exactly **4.20 MB** ($< 5.0\text{ MB}$ budget requirement satisfied).

---

## 5. Mode Behaviors

The digital twin UI supports three distinct operational modes toggled via top-bar segmented controls or URL query parameters (`/twin?mode=visitor|engineer|research`):

```mermaid
flowchart TD
    A["Twin URL (/twin?mode=...)"] --> B{"mode parameter"}
    B -->|visitor (default)| C["Visitor Mode (导览模式)"]
    B -->|engineer| D["Engineer Mode (工程透视)"]
    B -->|research| E["Research Mode (学术重放)"]

    C --> C1["Guided 5-Waypoint Flythrough Tour"]
    C --> C2["Previous/Next Step Controls & 5 Progress Dots"]
    C --> C3["Skip / Free-Fly Exit Button"]

    D --> D1["Data-Driven Catalog Drill-down"]
    D --> D2["Clickable 121 Tools & Nominal Draft Ghosts"]
    D --> D3["Exact Millimeter Bounding Box & Field Tier Badges"]

    E --> E1["30-Day MIMAC-2026 Event Replay Scrubber"]
    E --> E2["SEMI E10 Machine State Real-Time Colors"]
    E --> E3["18-Tool-Group Utilization Heatmap & WIP Readout"]
    E --> E4["Honesty Rule: AMHS Tagged '示意 Illustrative'"]
```

### Mode Breakdown

### 1. `visitor` Mode (Default)

- **Target Audience**: General public, fab visitors, non-specialist stakeholders.
- **Cinematic Tour**: 5 narrative waypoints:
  1. _Fab Ballroom Overview_ — Cleanroom architecture and ballroom layout.
  2. _Litho Amber Bay_ — Sub-micron optical lithography under 560nm safe-light.
  3. _AMHS Overhead Monorail_ — Automated Material Handling System with OHT vehicles.
  4. _Sub-Fab & Facilities_ — Sub-fab basement vacuum pumps, scrubbers, and UPW loops.
  5. _Advanced Packaging Annex_ — 2.5D/3D hybrid bonding and packaging bay.
- **HUD Navigation**: Previous (`<`), Next (`>`), 5 clickable interactive progress dots with active pulsing indicator, and a Skip ("跳过 / 自由巡检") button for instant transition to free camera orbit.

### 2. `engineer` Mode

- **Target Audience**: Process engineers, equipment technicians, cleanroom layout planners.
- **Interactivity**: Clicking any physical tool opens an engineering inspection sheet with:
  - Equipment model, vendor, and category.
  - Footprint dimensions ($W \times D \times H$ in millimeters).
  - Data provenance badge (`vendor_confirmed`, `independent_verified`, `inferred`, `synthetic`, `draft`).
  - Direct link to full catalog record or GitHub prefill submission.
- **Visuals**: Displays cleanroom bay boundaries, clearance maintenance envelopes, and utility drop connection points.

### 3. `research` Mode

- **Target Audience**: Operations research scholars, dispatching algorithm developers, discrete-event simulation researchers.
- **Timeline Scrubber**: Real-time replay of 30 days of fab operation ($0 \text{ to } 720\text{ hours}$) with interactive scrub slider, play/pause toggle, and $1\times / 5\times / 20\times / 100\times / 500\times$ speed multipliers.
- **Real-Time Indicators**:
  - Live fab-wide WIP counter updated dynamically from `wip_sample` events.
  - 3D SEMI E10 state lighting on tools (Green = Productive, Yellow = Standby, Red = Unscheduled Down, Blue = Scheduled Maintenance).
  - 18-Tool-Group Utilization Heatmap bar chart overlay comparing current utilization against stationary workload limits.
  - Prominent banner linking to `/benchmark` for full mathematical formulations.
  - **AMHS Honesty Banner**: AMHS vehicles labeled with "示意 Illustrative" in 3D billboarding and HUD readouts to acknowledge that MIMAC-2026 T1 models material transport as instant transfers.

---

## 6. Verification and Acceptance Criteria Compliance

- **AC1 (Data-Driven Layout)**: Verified. 121 records loaded dynamically from `/catalog.json`. 7 L1 detailed models rendered at verified millimeter dimensions; 114 draft records rendered as wireframe ghost boxes.
- **AC2 (Uncertainty Shaders)**: Verified. Visual opacity, wireframe overlays, and billboard tags dynamically assigned based on data provenance tier (`vendor_confirmed`, `inferred`, `synthetic`).
- **AC3 (Draft Interactive Prefill)**: Verified. Clicking any draft ghost box opens `prefill_url` in a new window.
- **AC4 (Simulated Event Stream)**: Verified. Generated 4.20 MB `events-t1-fifo.jsonl` ($\le 5.0\text{ MB}$); scrubber replays 30 days of SEMI E10 states and WIP samples.
- **AC5 (Utilization Heatmap & Benchmark Link)**: Verified. 18 tool groups rendered with utilization bars; header links to `/benchmark`.
- **AC6 (Three Modes & Presets)**: Verified. `?mode=visitor|engineer|research` URL support, camera collision limits adjusted (y=3.8m in Litho bay, y=4.8m in AMHS bay).
- **AC7 (AMHS Honesty Rule)**: Verified. Vehicles tagged with "示意 Illustrative" in 3D sprites and HUD.
- **AC8 (Zero Marketing Jargon)**: Verified. No banned superlative adjectives present.
- **AC9 (Static Deployment)**: Verified. Entire system runs client-side with no backend server required.
