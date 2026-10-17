// ==========================================
// SemiconFab.org — Vision Whitepaper 9-Language Dictionary
// Open Initiative Vision & 6 Pillars Multilingual Content
// ==========================================

const VISION_I18N = {
  en: {
    vision_page_title: "Open Initiative Vision & 6 Pillars — SemiconFab.org",
    vision_brand_sub: "Open Fab Digital Twin Initiative",
    vision_nav_pillars: "6 Core Pillars",
    vision_nav_phase1: "Phase 1 Strategy",
    vision_nav_roadmap: "Roadmap",
    vision_nav_stack: "Stack Matrix",

    // Hero
    vision_hero_badge:
      "THE OPEN INITIATIVE · VISION WHITE-PAPER & ARCHITECTURAL BLUEPRINT",
    vision_hero_title_1: "The Open Semiconductor",
    vision_hero_title_2: "Fab Digital Twin Vision",
    vision_hero_desc:
      "Semiconductor manufacturing represents the pinnacle of precision engineering and computing. Yet legacy industrial software has long been monopolized inside closed walled gardens. The <b>SemiconFab Open Initiative</b> aims to unite global engineers, researchers, and ecosystem partners to build a source-available, first-principles 300mm advanced fab digital twin reference framework spanning physical cleanrooms to microscopic wafer physics.",
    vision_hero_cta_pillars: "Explore 6 Core Pillars",
    vision_hero_cta_phase1: "Phase 1 Morphological Strategy",
    vision_hero_cta_twin: "Experience 3D Cleanroom Prototype",

    // 4 Highlight Cards
    vision_hl_pillars_title: "6 Technical Pillars",
    vision_hl_pillars_desc:
      "Covering spatial CAD, MES dispatching, GEM300, process physics to big data fabric.",
    vision_hl_p1_title: "Phase 1 High-Fidelity Pilot",
    vision_hl_p1_desc:
      "Modular anatomy, realistic kinematics, and physical waveforms with zero backend.",
    vision_hl_semi_title: "Strict SEMI Standards",
    vision_hl_semi_desc:
      "Aligned with SEMI E10, E40, E87, E90, E94, E157, and STDF V4 specifications.",
    vision_hl_open_title: "Open Core Benchmark",
    vision_hl_open_desc:
      "Lowering barriers to provide open benchmarks for academia, universities, and industry.",

    // Why Open Initiative
    vision_why_title:
      "Why Does Semiconductor Manufacturing Need an Open Initiative?",
    vision_why_subtitle:
      "Chip design has welcomed open-source waves like RISC-V and OpenROAD, yet wafer manufacturing remains constrained by three structural dilemmas:",
    vision_why_p1_title: "1. Proprietary Monopolies & Prohibitive Costs",
    vision_why_p1_desc:
      "Commercial Fab software suites (Applied SmartFactory, Siemens Opcenter, KLA Klarity) cost tens of millions per site with closed proprietary protocols, creating stubborn data silos.",
    vision_why_p2_title: "2. Severe Talent Gap in Universities & Research",
    vision_why_p2_desc:
      "Students and researchers rarely access real 300mm production systems. The absence of open, sanitized simulation sandboxes leaves the industry chronically short of interdisciplinary talent.",
    vision_why_p3_title: "3. Scarcity of Open Reference Benchmarks",
    vision_why_p3_desc:
      "AI researchers seeking to advance FDC diagnostics, OHT dispatching, or yield root-cause analysis lack compliant, physics-consistent benchmarks. The Open Initiative creates this golden standard.",
    vision_why_p4_title: "4. Winner-take-all ecosystem",
    vision_why_p4_desc:
      "Every equipment category is owned by one or two giants — lithography, etch, inspection alike. The moat isn't just technology; it's the cost of evaluation. No fab can risk production to qualify a challenger's tool, so challengers can never earn the track record they'd need. An open equipment catalog plus reference-grade simulation attacks exactly this wall.",

    // Design Principles
    vision_principles_badge: "CORE PRINCIPLES",
    vision_principles_title: "Design Principles",
    vision_principles_sub:
      "Four foundational values guiding our open-architecture engineering approach.",
    vision_principle_1_title: "Open knowledge",
    vision_principle_1_desc:
      "Fab know-how is among the most secretive in industry. An open equipment catalog and scheduling benchmark give students, researchers, and the curious a place to start.",
    vision_principle_2_title: "Honesty over precision",
    vision_principle_2_desc:
      "A teaching and research tool, not an industrial twin. Every record carries a source tier; gaps are labeled, synthetic data is marked synthetic.",
    vision_principle_3_title: "Source-available",
    vision_principle_3_desc:
      "PolyForm Noncommercial 1.0.0, free for education and personal use. (Deliberately not 'open source': the noncommercial term matters.)",
    vision_principle_4_title: "A healthier ecosystem",
    vision_principle_4_desc:
      "An open catalog lets challengers sit side by side with incumbents under one schema; reference simulation gives new tools a credible first step; subfab vendors get their first public storefront.",

    // Section 6 Pillars
    vision_pillars_badge: "THE SIX FOUNDATIONAL PILLARS",
    vision_pillars_title: "The 6 Full-Stack Digital Twin Pillars",
    vision_pillars_subtitle:
      "A genuine fab digital twin is never just a 3D showroom—it is a comprehensive architecture integrating spatial geometry, operations research, industrial protocols, process physics, streaming data, and open ecosystems.",

    // Pillar 1
    vision_p1_name: "Physical & CAD Spatial Twin",
    vision_p1_desc:
      "Elevating generic bounding boxes into verified <b>SEMI E72</b> footprints and BIM LOD300 models. Faithfully reconstructing internal machine anatomy, cleanroom microenvironments, and underground Subfab utility runs.",
    vision_p1_c1_title: "Modular Tool Anatomy",
    vision_p1_c1_desc:
      "EFEM mini-environments, 300mm Load Ports with FOUP docking pins, vacuum transfer chambers (VTC), robotic arms, and cluster chamber viewports.",
    vision_p1_c2_title: "Subfab Basement & Piping Topology",
    vision_p1_c2_desc:
      "Edwards dry vacuum pumps, SMC chillers, abatement scrubbers, and color-coded utility pipelines for UPW, specialty gases, vacuum, and chemical exhaust.",
    vision_p1_c3_title: "ISO Class 1/3 Cleanroom Environment",
    vision_p1_c3_desc:
      "Ceiling 1200×600mm FFU arrays, 0.45 m/s laminar downflow velocity fields, perforated raised floor tiles (30% open ratio), and positive pressure control.",
    vision_p1_c4_title: "Photolithography Amber Bay Optical Zone",
    vision_p1_c4_desc:
      "UV-blocking 589nm amber yellow lighting zone to prevent photoresist premature exposure.",
    vision_p1_spec_title: "// Spatial CAD Specifications",
    vision_p1_spec_l1: "Footprint Standard:",
    vision_p1_spec_s1: "SEMI E72 Equipment Footprint",
    vision_p1_spec_l2: "Model Format:",
    vision_p1_spec_s2: "glTF 2.0 / USD / IFC BIM",
    vision_p1_spec_l3: "Level of Detail:",
    vision_p1_spec_s3: "LOD0 (Layout) ~ LOD300 (Detailed Assembly)",
    vision_p1_spec_l4: "Utility Pipe Codes:",
    vision_p1_spec_s4: "SEMI S2 / NFPA 79 Facility Standards",
    vision_p1_spec_l5: "Rendering Engine:",
    vision_p1_spec_s5: "Three.js (Web) / WebGPU",

    // Pillar 2
    vision_p2_name: "MES & AMHS Logistics DES Engine",
    vision_p2_desc:
      "Advanced semiconductor manufacturing is a massively re-entrant discrete logistics network. Powered by Discrete Event Simulation (DES) to route 25-wafer FOUPs through hundreds of processing bays.",
    vision_p2_c1_title: "800+ Step Re-entrant Routing Tree",
    vision_p2_c1_desc:
      "Litho, Etch, Implant, Deposition, and CMP cycling, realistically simulating repeat tool visits, queue buildup, and tool contention.",
    vision_p2_c2_title: "Strict Inter-Step Q-Time Windows",
    vision_p2_c2_desc:
      "Enforcing 2-4 hour limits between pre-clean and dielectric deposition to prevent native oxide and molecular contamination, with dynamic priority preemption.",
    vision_p2_c3_title: "AMHS OHT Anti-Collision & Deadlock Prevention",
    vision_p2_c3_desc:
      "Time-Space Network Flow routing algorithms for overhead transport vehicles to eliminate main track congestion and gridlock.",
    vision_p2_c4_title: "Stocker Automation & Dispatch Optimization",
    vision_p2_c4_desc:
      "Integration with Google OR-Tools for dispatching heuristics (FIFO, SPT, Critical Ratio) to maximize bottleneck tool OEE.",
    vision_p2_spec_title: "// MES & Logistics Engine Stack",
    vision_p2_spec_l1: "DES Kernel:",
    vision_p2_spec_s1: "SimPy / Salabim (Python) / Rust-DES",
    vision_p2_spec_l2: "Operations Solver:",
    vision_p2_spec_s2: "Google OR-Tools / OptaPlanner",
    vision_p2_spec_l3: "Carrier Standard:",
    vision_p2_spec_s3: "SEMI E87 CMS / SEMI E40 PJM",
    vision_p2_spec_l4: "Commercial Suite:",
    vision_p2_spec_s4: "Siemens Tecnomatix / FlexSim / Muratec",
    vision_p2_spec_l5: "Time Sync:",
    vision_p2_spec_s5: "Discrete-Event Virtual Clock Engine",

    // Pillar 3
    vision_p3_name: "Connectivity & Virtual GEM300 Tool Layer",
    vision_p3_desc:
      "Full implementation of SEMI 300mm communication standards. Open <b>Virtual Tool Simulators</b> allow end-to-end testing of MES commands, state reporting, and alarms without physical hardware.",
    vision_p3_c1_title: "Full GEM300 Standard Suite",
    vision_p3_c1_desc:
      "SEMI E40 (Process Job), E87 (Carrier Management), E90 (Substrate Tracking), and E94 (Control Job Management).",
    vision_p3_c2_title: "High-Frequency EDA / Interface A Channel",
    vision_p3_c2_desc:
      "High-bandwidth sensor telemetry channel compliant with SEMI E157/E164, decoupled from transactional MES traffic.",
    vision_p3_c3_title: "Open Virtual Tool Simulator",
    vision_p3_c3_desc:
      "Bidirectional S1F1 handshakes, S2F41 remote commands, S6F11 event reports with SEMI E10 state machines (Run/Idle/Down/PM).",
    vision_p3_c4_title: "OPC UA & Industrial Gateway Adapters",
    vision_p3_c4_desc:
      "Open62541 and Eclipse Milo bridges connecting tool controllers to modern enterprise IoT buses.",
    vision_p3_spec_title: "// Industrial Protocol Stack",
    vision_p3_spec_l1: "Transport Layer:",
    vision_p3_spec_s1: "HSMS (SEMI E37) / SECS-II (E5)",
    vision_p3_spec_l2: "Generic Model:",
    vision_p3_spec_s2: "GEM (SEMI E30) / GEM300",
    vision_p3_spec_l3: "Open Protocol Lib:",
    vision_p3_spec_s3: "secsgem (Python) / Open-SECS",
    vision_p3_spec_l4: "Commercial Suite:",
    vision_p3_spec_s4: "PEER Group / Cimetrix CIM300",
    vision_p3_spec_l5: "State Definition:",
    vision_p3_spec_s5: "SEMI E10 RAM (Reliability, Availability)",

    // Pillar 4
    vision_p4_name: "Process Physics & YMS Engine",
    vision_p4_desc:
      "Yield is the lifeblood of the fab. Transitioning from macroscopic empirical formulas to compact surrogate physics, industrial STDF/KLARF stream parsing, and spatial commonality root cause analysis (RCA).",
    vision_p4_c1_title: "Compact Surrogate Physics Metamodels",
    vision_p4_c1_desc:
      "Within-wafer non-uniformity (WIWNU) for etch/CVD, chamber seasoning drift, and lithography overlay 3-sigma residuals.",
    vision_p4_c2_title: "STDF V4 & KLARF Industrial Ingestion",
    vision_p4_c2_desc:
      "High-throughput binary parsers extracting ATE wafer test bins, defect coordinate maps, and parametric parametric distributions.",
    vision_p4_c3_title: "Commonality Analysis & Root Cause Traceback",
    vision_p4_c3_desc:
      "Reverse indexing shared tools and chamber IDs for wafer lots exhibiting ring or localized cluster defect patterns.",
    vision_p4_c4_title: "Spatial Defect Adder Analysis",
    vision_p4_c4_desc:
      "Subtracting baseline defect maps between consecutive inspection points to isolate tool-induced particle adders.",
    vision_p4_spec_title: "// Process & Yield Engine Stack",
    vision_p4_spec_l1: "Test Data Standard:",
    vision_p4_spec_s1: "SEMI STDF V4 / STDF-V4-Spec",
    vision_p4_spec_l2: "Open Parser:",
    vision_p4_spec_s2: "PySTDF (Python) / rust-stdf (Rust)",
    vision_p4_spec_l3: "Defect Benchmark:",
    vision_p4_spec_s3: "WM-811K (811,472 Wafers)",
    vision_p4_spec_l4: "Commercial Suite:",
    vision_p4_spec_s4: "KLA Klarity / PDF Solutions Exensio",
    vision_p4_spec_l5: "Yield Model:",
    vision_p4_spec_s5: "Poisson / Murphy / Seeds Negative Binomial",

    // Pillar 5
    vision_p5_name: "Industrial High-Throughput Data Fabric",
    vision_p5_desc:
      "A 300mm fab generates tens of terabytes of telemetry daily. Transcending standalone relational databases with a modern streaming bus, time-series telemetry store, and columnar OLAP analytics fabric.",
    vision_p5_c1_title: "Sub-Second Industrial Message Bus",
    vision_p5_c1_desc:
      "Apache Kafka and MQTT ingesting tens of thousands of S6F11 events, tool state changes, and OHT telemetry points.",
    vision_p5_c2_title: "Time-Series Telemetry Store",
    vision_p5_c2_desc:
      "TimescaleDB and InfluxDB storing high-frequency RF power, mass flow controller (MFC) curves, chuck temperatures, and chamber pressures.",
    vision_p5_c3_title: "High-Throughput OLAP Analytics",
    vision_p5_c3_desc:
      "ClickHouse and DuckDB executing sub-second aggregations and multi-dimensional drill-downs across billions of wafer test points.",
    vision_p5_c4_title: "Streaming SPC & Nelson Rule Engine",
    vision_p5_c4_desc:
      "Real-time Cp/Cpk process capability calculations and Shewhart charts triggering automated alarms and tool interlocks.",
    vision_p5_spec_title: "// Data Architecture Stack",
    vision_p5_spec_l1: "Event Bus:",
    vision_p5_spec_s1: "Apache Kafka / Eclipse Mosquitto",
    vision_p5_spec_l2: "Time-Series DB:",
    vision_p5_spec_s2: "TimescaleDB / InfluxDB",
    vision_p5_spec_l3: "OLAP Columnar:",
    vision_p5_spec_s3: "ClickHouse / DuckDB",
    vision_p5_spec_l4: "SPC Algorithm:",
    vision_p5_spec_s4: "pyspc / spc-kit (SQL) / mfgQC",
    vision_p5_spec_l5: "Telemetry Dashboard:",
    vision_p5_spec_s5: "Grafana / Apache Superset",

    // Pillar 6
    vision_p6_name: "Open Ecosystem & Reference Benchmarks",
    vision_p6_desc:
      "The longevity of an open initiative hinges on transparent standards, strict IP boundaries, and reproducible benchmarks that benefit both academia and the semiconductor industry.",
    vision_p6_c1_title: "Open 28nm Reference Process PDK",
    vision_p6_c1_desc:
      "Sanitized 300mm production dataset including equipment bill-of-materials, standard recipe steps, Q-Time limits, and target yields.",
    vision_p6_c2_title: "One-Click Local Sandbox",
    vision_p6_c2_desc:
      "Docker-Compose bundle provisioning 3D Web UI, virtual MES, simulated tools, and telemetry databases in minutes.",
    vision_p6_c3_title: "Modular Open Fab Plugin API",
    vision_p6_c3_desc:
      "Extensible gRPC and REST interfaces for third-party tool models, FDC anomaly algorithms, and AMHS dispatch solvers.",
    vision_p6_c4_title: "IP Governance & Synthetic Sanitization",
    vision_p6_c4_desc:
      "Rigorous compliance with OEM commercial secrets and foundry IP through mathematically synthesized parametric data.",
    vision_p6_spec_title: "// Governance & Ecosystem Model",
    vision_p6_spec_l1: "License:",
    vision_p6_spec_s1: "PolyForm Noncommercial 1.0.0 (source-available)",
    vision_p6_spec_l2: "Deployment Stack:",
    vision_p6_spec_s2: "Docker-Compose / Helm Chart",
    vision_p6_spec_l3: "Analogy Benchmark:",
    vision_p6_spec_s3: "RISC-V International / OpenROAD Project",
    vision_p6_spec_l4: "Governance Model:",
    vision_p6_spec_s4: "Community-driven",
    vision_p6_spec_l5: "Open APIs:",
    vision_p6_spec_s5: "OpenFab gRPC & REST Standard",

    // Phase 1 Strategy
    vision_p1_strat_badge: "PHASE 1 IMPLEMENTATION STRATEGY",
    vision_p1_strat_title: "Phase 1 Strategy: Utmost Morphological Realism",
    vision_p1_strat_sub:
      "In Phase 1, our objective is morphological fidelity rather than full closed-loop control: <b>complete visual modularity, authentic industrial proportions, and convincing realism</b>. Achieving professional engineering credibility at minimal compute and infrastructure cost.",
    vision_p1_t1_title: "1. Modular Machine Feature Decomposition",
    vision_p1_t1_desc:
      "Transcending monolithic cubes with lightweight procedural assemblies:",
    vision_p1_t1_i1:
      "<b>EFEM Mini-Environment</b>: Antistatic glass viewports and SCARA transfer arms",
    vision_p1_t1_i2:
      "<b>Load Ports</b>: 2-4 angled docking stations with kinematic pins and tri-color status lights",
    vision_p1_t1_i3:
      "<b>Cluster Architecture</b>: Central vacuum transfer chamber with 4-6 reaction chambers",
    vision_p1_t1_i4:
      "<b>Peripheral Details</b>: Overhead exhaust flanges, cantilevered touchscreens, and SEMI E10 light towers",
    vision_p1_t1_tag: "Cost: Minimal (client-side 3D) · Fidelity: Leaps ahead",

    vision_p1_t2_title: "2. Cleanroom Spatial Atmosphere & Depth",
    vision_p1_t2_desc:
      "Recreating the unmistakable aura of an advanced semiconductor cleanroom:",
    vision_p1_t2_i1:
      "<b>Perforated Floor Tiles</b>: 30% open ratio airflow grid with recessed sub-floor seams",
    vision_p1_t2_i2:
      "<b>Ceiling FFU Array</b>: Tightly packed HEPA filter louvers and shadowless high-lumen white lighting",
    vision_p1_t2_i3:
      "<b>Photolithography Amber Glow</b>: Distinctive 589nm amber yellow illumination in litho bays",
    vision_p1_t2_i4:
      "<b>Subfab Utility Racks</b>: Pipe runs color-coded for UPW blue, specialty gas orange, and vacuum gray",
    vision_p1_t2_tag: "Spatial Depth: Immersive · Brand Recognition: Instant",

    vision_p1_t3_title: "3. Procedural Mechanical Kinematics",
    vision_p1_t3_desc:
      "Choreographing realistic mechanical actions using client-side timelines without complex dispatch servers:",
    vision_p1_t3_i1:
      "<b>OHT Drop Sequences</b>: Vehicle halts $\\rightarrow$ hoist cables descend $\\rightarrow$ FOUP latches onto Load Port",
    vision_p1_t3_i2:
      "<b>Wafer Transfer Arm</b>: Load Port opens, vacuum end-effector transfers 300mm wafer into loadlock",
    vision_p1_t3_i3:
      "<b>Chamber Glow</b>: Etch chamber viewports pulse with soft violet/magenta plasma illumination",
    vision_p1_t3_i4:
      "<b>Andon Towers</b>: Steady green running, blinking blue standby, breathing amber recipe change",
    vision_p1_t3_tag:
      "Visual Authenticity: Uncompromising · User Experience: Dynamic",

    vision_p1_t4_title: "4. Physics-Consistent Telemetry Sparklines",
    vision_p1_t4_desc:
      "Generating telemetry curves that adhere strictly to real semiconductor process physics:",
    vision_p1_t4_i1:
      "<b>Etch RF Power Signature</b>: Pumpdown vacuum drop $\\rightarrow$ ignition strike spike $\\rightarrow$ steady etch $\\rightarrow$ EPD step",
    vision_p1_t4_i2:
      "<b>Thermal Inertia</b>: Electrostatic chuck temperature exhibiting authentic first-order lag response",
    vision_p1_t4_i3:
      "<b>Shewhart Control Charts</b>: Statistical UCL/LCL bounds with occasional Nelson rule alert points",
    vision_p1_t4_i4:
      "<b>SEMI E10 OEE Breakdown</b>: Live dynamic pie allocation across Productive, Standby, Down, and PM",
    vision_p1_t4_tag: "Domain Inspection: Flawless · Industrial Rigor: Maximal",

    vision_p1_takeaway_title:
      "Phase 1 Core Value: Winning Trust with High-Velocity Agility",
    vision_p1_takeaway_desc:
      "By perfecting the external modular form and industrial detail first, we build visual consensus and industry awareness. In Phases 2 and 3, we progressively integrate discrete simulation (DES) and GEM300 protocols upon this trusted foundation.",
    vision_p1_takeaway_btn: "Explore Phase 1 Prototype",

    // Roadmap
    vision_roadmap_title: "Four-Phase Evolution Roadmap",
    vision_roadmap_sub:
      "A pragmatic progression from authentic visual form to fully closed-loop industrial digital twins.",
    vision_rm_completed: "✓ Completed",
    vision_rm_p1_title: "High-Fidelity Visual Form",
    vision_rm_p1_desc:
      "Modular tool anatomy (EFEM/Chambers), perforated flooring, amber litho bay, Subfab utility racks, OHT kinematics, and physics-consistent FDC waveforms.",
    vision_rm_p1_tag: "✓ Pure frontend · Low cost · High impact",
    vision_rm_p2_title: "Discrete-Event Simulation (DES)",
    vision_rm_p2_desc:
      "Introducing SimPy/Rust DES engines: re-entrant 800+ step lot routing, strict Q-Time residency windows, and deadlock-free OHT logistics scheduling. (delivered via the MIMAC-2026 benchmark and in-browser simulation)",
    vision_rm_p2_tag: "→ Physics-consistent fab logistics",
    vision_rm_p3_title: "GEM300 Virtual Tool Sandbox",
    vision_rm_p3_desc:
      "Open SECS/GEM servers simulating SEMI E40/E87/E90/E94 protocols, recipe execution, and high-speed EDA telemetry streams.",
    vision_rm_p3_tag: "→ Complete industrial interoperability",
    vision_rm_p4_title: "Closed-Loop Ecosystem Benchmark",
    vision_rm_p4_desc:
      "STDF/KLARF stream parsing, open 28nm benchmark dataset release, one-click Docker sandbox, and open plugin ecosystem.",
    vision_rm_p4_tag: "→ Growing open ecosystem",

    // Version Milestones
    vision_milestones_badge: "RELEASE MILESTONES",
    vision_milestones_title: "Release Milestones",
    vision_milestones_sub:
      "Continuous iteration journey from public release to the current version.",
    vision_ms_v1_0:
      "Public launch: 121-record catalog, 3D twin, pure-static site",
    vision_ms_v1_1: "153 records, deterministic IDs; used-market data merged",
    vision_ms_v1_2: "167 records, 8 true-scale L1 models",
    vision_ms_v1_3:
      "Interactive benchmark: in-browser Pyodide dispatching simulation",
    vision_ms_v1_4: "Follow-a-wafer route animation; roof/HVAC layer",

    // Matrix
    vision_matrix_title:
      "Commercial Suites vs. Open-Source Technology Stack Matrix",
    vision_matrix_sub:
      "Benchmarking industry standard software against recommended open-source equivalents across all operational layers.",
    vision_matrix_th_layer: "Architectural Layer",
    vision_matrix_th_std: "SEMI Standard / Protocol",
    vision_matrix_th_comm: "Commercial Benchmark",
    vision_matrix_th_open: "Open Initiative Recommended Stack",
    vision_matrix_th_val: "Functionality & Engineering Value",
    vision_mat_r1_layer: "Spatial & 3D Tool Assembly",
    vision_mat_r1_val:
      "Lightweight web 2D/3D cleanroom with verified elevation drawings and multi-angle views",
    vision_mat_r2_layer: "AMHS & Line Dispatch Simulation",
    vision_mat_r2_val:
      "Re-entrant routing, FOUP queue scheduling, and deadlock-free network flow routing",
    vision_mat_r3_layer: "Equipment Protocol & Connectivity",
    vision_mat_r3_val:
      "Bidirectional S1F1 handshakes, S6F11 event streams, and software tool simulators",
    vision_mat_r4_layer: "Statistical Process Control (SPC)",
    vision_mat_r4_val:
      "Shewhart control charts, Nelson 8 rules, and real-time chamber anomaly detection",
    vision_mat_r5_layer: "Yield & Wafer Map Management",
    vision_mat_r5_val:
      "ATE binary ingestion, defect spatial clustering, and multi-tool commonality RCA",
    vision_mat_r6_layer: "Industrial Data Fabric",
    vision_mat_r6_val:
      "Sub-second event bus, sensor time-series DB, and multi-billion die OLAP analytics",

    // CTA
    vision_cta_title:
      "Co-Building the Open Future of Semiconductor Manufacturing",
    vision_cta_desc:
      "Whether you are a fab process engineer, industrial software architect, optimization researcher, or university educator, the SemiconFab Open Initiative welcomes your participation.",
    vision_cta_btn_twin: "Launch 3D Digital Twin",
    vision_cta_btn_contact: "Contact Working Group",
    vision_footer_home: "Home",
    vision_footer_twin: "3D Twin",
    vision_footer_license:
      "Source-available · PolyForm Noncommercial 1.0.0 · Free for education and personal use · Commercial licensing funds ongoing development.",
  },

  "zh-CN": {
    vision_page_title: "Open Initiative 愿景与 6 大核心支柱 — SemiconFab.org",
    vision_brand_sub: "半导体晶圆厂数字孪生开放倡议",
    vision_nav_pillars: "6 大核心支柱",
    vision_nav_phase1: "Phase 1 方案",
    vision_nav_roadmap: "演进路线图",
    vision_nav_stack: "开源替代矩阵",

    // Hero
    vision_hero_badge:
      "THE OPEN INITIATIVE · VISION WHITE-PAPER & ARCHITECTURAL BLUEPRINT",
    vision_hero_title_1: "开放半导体晶圆制造",
    vision_hero_title_2: "数字孪生全景愿景白皮书",
    vision_hero_desc:
      "半导体芯片制造是人类精密工程与计算科学的最高峰。然而，传统的工业软件长期被寡头垄断于封闭的“围墙花园”中。<b>SemiconFab Open Initiative</b> 旨在联合全球工程师、学者与生态伙伴，构建开放透明、基于第一性原理、贯穿物理洁净室与微观晶圆物理的 300mm 先进制程数字孪生参考框架。",
    vision_hero_cta_pillars: "深入探索 6 大核心支柱",
    vision_hero_cta_phase1: "Phase 1 形态拟真方案",
    vision_hero_cta_twin: "体验 3D 洁净室原型",

    // 4 Highlight Cards
    vision_hl_pillars_title: "6 大核心支柱",
    vision_hl_pillars_desc:
      "覆盖空间CAD、MES调度、GEM300、工艺物理到大数据底座",
    vision_hl_p1_title: "Phase 1 形态高拟真",
    vision_hl_p1_desc:
      "模块解构、动效拟真、物理感波形，零后端实现高逼真工业视觉",
    vision_hl_semi_title: "严格工业标准",
    vision_hl_semi_desc:
      "对齐 SEMI E10, E40, E87, E90, E94, E157 及 STDF V4 规范",
    vision_hl_open_title: "开放黄金基准",
    vision_hl_open_desc:
      "破除商业套件高门槛，为科研、高校与智造企业提供开放基准",

    // Why Open Initiative
    vision_why_title: "为什么半导体制造需要开放倡议？",
    vision_why_subtitle:
      "芯片设计已迎来 RISC-V 与 OpenROAD 的开源浪潮，而晶圆制造（Fab Manufacturing）仍受困于三大结构性困境：",
    vision_why_p1_title: "1. 专有巨头垄断与高昂门槛",
    vision_why_p1_desc:
      "商业 Fab 工业软件（Applied SmartFactory、Siemens Opcenter、KLA Klarity 等）单厂软件授权费高达数千万美元，且各厂商协议互相封闭，形成极其顽固的数据孤岛。",
    vision_why_p2_title: "2. 高校与科研人才严重断层",
    vision_why_p2_desc:
      "微电子与智能制造专业学生无法在实验室接触真实的 300mm 产线系统。缺乏脱敏开放的虚拟仿真沙盒，导致产业界长期面临懂制造、懂算法的复合型人才荒。",
    vision_why_p3_title: "3. 缺乏开源参考基准（Benchmarks）",
    vision_why_p3_desc:
      "AI 算法学者想要做 FDC 故障诊断、天车调度优化或良率溯源，却根本找不到一份公开合规、物理自洽的先进制程基准数据包。开放倡议将建立首个“黄金参考基准”。",
    vision_why_p4_title: "4. 赢家通吃的设备生态",
    vision_why_p4_desc:
      "每个设备品类都被一两家巨头把持——光刻、刻蚀、检测莫不如此。护城河不只是技术，更是评估成本：一座 fab 承担不起拿量产去验证挑战者设备的风险，挑战者于是永远攒不出进入 fab 所需的 track record。开放的设备目录与参考级仿真，攻击的正是这道评估成本墙。",

    // Design Principles
    vision_principles_badge: "CORE PRINCIPLES",
    vision_principles_title: "设计原则",
    vision_principles_sub: "指导 SemiconFab 开放数字孪生演进的四项核心准则。",
    vision_principle_1_title: "开放知识",
    vision_principle_1_desc:
      "Fab know-how 是全工业界最封闭的知识之一。开放的设备目录与调度 benchmark 给学生、研究者和好奇的人一个起点。",
    vision_principle_2_title: "诚实优先于精确",
    vision_principle_2_desc:
      "教学研究级工具，非工业级数字孪生。每条记录带来源分级，数据不全就明说，合成数据就标注合成。",
    vision_principle_3_title: "源码公开",
    vision_principle_3_desc:
      "PolyForm Noncommercial 1.0.0，教育与个人使用免费。（刻意不用“开源”：非商业条款对我们很重要。）",
    vision_principle_4_title: "更健康的设备生态",
    vision_principle_4_desc:
      "开放目录让挑战者设备与巨头同 schema 并排可比，参考仿真给新设备一个可信的第一步；subfab 长尾厂商第一次拥有公开店面。",

    // Section 6 Pillars
    vision_pillars_badge: "THE SIX FOUNDATIONAL PILLARS",
    vision_pillars_title: "数字孪生全栈 6 大核心支柱",
    vision_pillars_subtitle:
      "一个真正的晶圆厂数字孪生，绝不仅仅是 3D 展厅，而是贯通“几何空间、调度运筹、工业通讯、工艺物理、流式数据、开源生态”的完整技术体系。",

    // Pillar 1
    vision_p1_name: "物理与几何空间孪生",
    vision_p1_desc:
      "将传统单一的长方体白模，升华为符合 <b>SEMI E72</b> 占地标准与 BIM LOD300 规范的高保真物理模型体系。精细化还原机台内部结构、洁净室微环境与地下 Subfab 动力管廊。",
    vision_p1_c1_title: "机台内部机构解构",
    vision_p1_c1_desc:
      "细化 EFEM 前端微环境仓、Load Port 晶圆盒装载口、真空传输室(VTC)机械臂、多腔体(Cluster Chambers)法兰与观察视窗。",
    vision_p1_c2_title: "Subfab 地下动力层与管线拓扑",
    vision_p1_c2_desc:
      "还原 Edwards 干式真空泵、SMC 冷水机、减排洗涤塔(Scrubber)，构建 UPW 纯水、特气、真空与酸碱排气的色标路由管网。",
    vision_p1_c3_title: "ISO Class 1/3 洁净室微环境",
    vision_p1_c3_desc:
      "吊顶 1200×600mm FFU 阵列、0.45m/s 垂直层流沉降风速场、微穿孔防静电地板(Perforated Tiles)、微正压梯度控制。",
    vision_p1_c4_title: "黄光微影区光学特征",
    vision_p1_c4_desc:
      "防紫外线琥珀色纯黄色滤光区（589nm 波长），防光刻胶意外曝光的专属隔离空间。",
    vision_p1_spec_title: "// 几何与空间规范指标",
    vision_p1_spec_l1: "外形标准:",
    vision_p1_spec_s1: "SEMI E72 Equipment Footprint",
    vision_p1_spec_l2: "模型格式:",
    vision_p1_spec_s2: "glTF 2.0 / USD / IFC BIM",
    vision_p1_spec_l3: "精细度级别:",
    vision_p1_spec_s3: "LOD0 (规划) ~ LOD300 (设备结构)",
    vision_p1_spec_l4: "动力管线色标:",
    vision_p1_spec_s4: "SEMI S2 / NFPA 79 Facility Standard",
    vision_p1_spec_l5: "渲染引擎:",
    vision_p1_spec_s5: "Three.js (Web) / WebGPU",

    // Pillar 2
    vision_p2_name: "制造执行与物流离散仿真",
    vision_p2_desc:
      "真正的半导体制造是极度重入式（Re-entrant）的超级物流系统。基于离散事件仿真（Discrete Event Simulation - DES）驱动晶圆批次（FOUP 25片/批）在全厂数百台机台间穿梭流转。",
    vision_p2_c1_title: "800+ 工步重入式路由树",
    vision_p2_c1_desc:
      "光刻、刻蚀、注入、沉积、CMP 循环往复，精确模拟每道工序对同一机台的重复访问与等待。",
    vision_p2_c2_title: "苛刻的 Q-Time 超时管控",
    vision_p2_c2_desc:
      "清洗到生长薄膜严格限制在 2~4 小时内，超时导致自然氧化或分子污染报废，模型支持动态优先级插队。",
    vision_p2_c3_title: "AMHS OHT 天车防碰撞与防死锁",
    vision_p2_c3_desc:
      "基于时空网络流算法（Time-Space Network Flow）计算空中天车路由，防止环路死锁与干线堵塞。",
    vision_p2_c4_title: "Stocker 晶圆立体仓与派工算法",
    vision_p2_c4_desc:
      "支持 Google OR-Tools 求解派工规则（FIFO, SPT, Critical Ratio），优化全厂瓶颈工序 OEE。",
    vision_p2_spec_title: "// 制造执行与物流技术选型",
    vision_p2_spec_l1: "离散仿真内核:",
    vision_p2_spec_s1: "SimPy / Salabim (Python) / Rust-DES",
    vision_p2_spec_l2: "运筹优化器:",
    vision_p2_spec_s2: "Google OR-Tools / OptaPlanner",
    vision_p2_spec_l3: "载具标准:",
    vision_p2_spec_s3: "SEMI E87 CMS / SEMI E40 PJM",
    vision_p2_spec_l4: "商业替代标杆:",
    vision_p2_spec_s4: "Siemens Tecnomatix / FlexSim / Muratec",
    vision_p2_spec_l5: "时间同步:",
    vision_p2_spec_s5: "Discrete-Event Virtual Clock Engine",

    // Pillar 3
    vision_p3_name: "工业通信与虚拟设备层",
    vision_p3_desc:
      "实现完整的 SEMI 300mm 工业通讯标准。提供完全开放的<b>“虚拟设备服务端（Virtual Tool Simulators）”</b>，无需实体机台即可完整体验与调试 MES 指令下发、状态上报与报警机制。",
    vision_p3_c1_title: "完整 GEM300 标准族实现",
    vision_p3_c1_desc:
      "SEMI E40 (工艺作业)、E87 (载具与LoadPort握手)、E90 (单片基板跟踪)、E94 (控制作业管理)。",
    vision_p3_c2_title: "高频 EDA / Interface A 数据通路",
    vision_p3_c2_desc:
      "基于 SEMI E157/E164 标准，建立独立于日常 MES 控制链路的数百赫兹传感器采集通道。",
    vision_p3_c3_title: "开放虚拟机台仿真器 (Virtual Tool)",
    vision_p3_c3_desc:
      "支持双向 S1F1 握手、S2F41 远程命令、S6F11 事件上报，内置 SEMI E10 状态机（Run/Idle/Down/PM）。",
    vision_p3_c4_title: "OPC UA 与工业网关适配",
    vision_p3_c4_desc:
      "集成 open62541 与 Eclipse Milo，实现设备底座与现代物联网工业总线的无缝转换。",
    vision_p3_spec_title: "// 工业通信技术协议栈",
    vision_p3_spec_l1: "通讯底层:",
    vision_p3_spec_s1: "HSMS (SEMI E37) / SECS-II (E5)",
    vision_p3_spec_l2: "通用模型:",
    vision_p3_spec_s2: "GEM (SEMI E30) / GEM300",
    vision_p3_spec_l3: "开源协议库:",
    vision_p3_spec_s3: "secsgem (Python) / Open-SECS",
    vision_p3_spec_l4: "商业替代标杆:",
    vision_p3_spec_s4: "PEER Group / Cimetrix CIM300",
    vision_p3_spec_l5: "状态定义:",
    vision_p3_spec_s5: "SEMI E10 RAM (Reliability, Availability)",

    // Pillar 4
    vision_p4_name: "工艺物理与良率工程引擎",
    vision_p4_desc:
      "良率（Yield）是晶圆厂的生命线。从简单的宏观经验公式，迈向紧凑物理代理模型（Surrogate Physics）、工业级 STDF/KLARF 数据解析与时空缺陷共性根因溯源（RCA）。",
    vision_p4_c1_title: "紧凑物理代理模型",
    vision_p4_c1_desc:
      "刻蚀与薄膜片内不均匀性 (WIWNU)、腔体季化老化漂移 (Seasoning Drift)、光刻套刻误差 (Overlay) 模型。",
    vision_p4_c2_title: "STDF V4 与 KLARF 工业流解析",
    vision_p4_c2_desc:
      "并行解析 ATE 自动测试机台标准测试数据流，提取 Bin Map 与数万颗测试晶粒的电学参数。",
    vision_p4_c3_title: "共性分析与根因溯源",
    vision_p4_c3_desc:
      "对产生环状(Ring)或局部聚集缺陷的晶圆批次，逆向检索其共同途经的机台与腔体号。",
    vision_p4_c4_title: "缺陷空间减法",
    vision_p4_c4_desc:
      "对比前后道暗场光学缺陷检测图，滤除已有缺陷，精确计算当前机台引入的新增颗粒。",
    vision_p4_spec_title: "// 良率与工艺工程技术方案",
    vision_p4_spec_l1: "测试数据标准:",
    vision_p4_spec_s1: "SEMI STDF V4 / STDF-V4-Spec",
    vision_p4_spec_l2: "开源解析器:",
    vision_p4_spec_s2: "PySTDF (Python) / rust-stdf (Rust)",
    vision_p4_spec_l3: "缺陷基准数据集:",
    vision_p4_spec_s3: "WM-811K (811,472 Wafers)",
    vision_p4_spec_l4: "商业替代标杆:",
    vision_p4_spec_s4: "KLA Klarity / PDF Solutions Exensio",
    vision_p4_spec_l5: "良率理论模型:",
    vision_p4_spec_s5: "Poisson / Murphy / Seeds Negative Binomial",

    // Pillar 5
    vision_p5_name: "实时工业数据底座架构",
    vision_p5_desc:
      "300mm 晶圆厂每日产生数以 TB 计的高频时序与缺陷数据。必须摆脱单机关系型数据库局限，采用现代“消息流 + 时序库 + 列式分析”的高通量工业混合数仓架构。",
    vision_p5_c1_title: "毫秒级工业消息总线",
    vision_p5_c1_desc:
      "基于 Apache Kafka 或 MQTT，吞吐全厂数万点位 S6F11 事件、机台状态变更与 OHT 天车站网坐标。",
    vision_p5_c2_title: "时序数据存储",
    vision_p5_c2_desc:
      "TimescaleDB / InfluxDB 存储腔体高频射频功率、气体流量(MFC)、静电吸盘温度与真空度工步曲线。",
    vision_p5_c3_title: "高通量列式分析",
    vision_p5_c3_desc:
      "ClickHouse / DuckDB 实现亿级晶圆芯片参数测试点跨批次秒级聚合与多维钻取。",
    vision_p5_c4_title: "实时 SPC 与 Nelson 规则引擎",
    vision_p5_c4_desc:
      "流式计算 Cp/Cpk 能力指数与休哈特控制图，毫秒级触发异常报警并推送机台联锁。",
    vision_p5_spec_title: "// 工业数据中枢架构栈",
    vision_p5_spec_l1: "消息流总线:",
    vision_p5_spec_s1: "Apache Kafka / Eclipse Mosquitto",
    vision_p5_spec_l2: "时序遥测库:",
    vision_p5_spec_s2: "TimescaleDB / InfluxDB",
    vision_p5_spec_l3: "OLAP 列式库:",
    vision_p5_spec_s3: "ClickHouse / DuckDB",
    vision_p5_spec_l4: "SPC 算法库:",
    vision_p5_spec_s4: "pyspc / spc-kit (SQL) / mfgQC",
    vision_p5_spec_l5: "可视化大屏:",
    vision_p5_spec_s5: "Grafana / Apache Superset",

    // Pillar 6
    vision_p6_name: "开放倡议生态与数据治理",
    vision_p6_desc:
      "倡议之所以能够长久，核心在于建立开源开放的标准、合规安全的数据边界与可复现的评测基准，让全球半导体科研机构与工业界共同受益。",
    vision_p6_c1_title: "开放 28nm 参考制程包",
    vision_p6_c1_desc:
      "提供自洽、脱敏的完整 300mm 流程配置（包含机台清单、标准工步、Q-Time 参数与参考良率）。",
    vision_p6_c2_title: "单键运行的本地沙箱",
    vision_p6_c2_desc:
      "基于 Docker-Compose 提供完整测试环境：前端看板 + 虚拟 MES + 模拟器机台 + 时序数据库。",
    vision_p6_c3_title: "插件化接入规范",
    vision_p6_c3_desc:
      "基于 gRPC / REST 定义清晰的机台模型扩展插槽、FDC 异常算法插槽与 AMHS 调度求解器插槽。",
    vision_p6_c4_title: "学术与工业脱敏治理规范",
    vision_p6_c4_desc:
      "严格遵守知识产权与 OEM 商业机密规范，使用参数化合成数据确保工程合法合规。",
    vision_p6_spec_title: "// 开放生态治理模式",
    vision_p6_spec_l1: "许可协议:",
    vision_p6_spec_s1: "PolyForm Noncommercial 1.0.0（源码公开）",
    vision_p6_spec_l2: "部署载体:",
    vision_p6_spec_s2: "Docker-Compose / Helm Chart",
    vision_p6_spec_l3: "类比参照:",
    vision_p6_spec_s3: "RISC-V International / OpenROAD Project",
    vision_p6_spec_l4: "组织形式:",
    vision_p6_spec_s4: "社区共建",
    vision_p6_spec_l5: "开放 API:",
    vision_p6_spec_s5: "OpenFab gRPC & REST Standard",

    // Phase 1 Strategy
    vision_p1_strat_badge: "PHASE 1 IMPLEMENTATION STRATEGY",
    vision_p1_strat_title: "Phase 1 实施策略：极致的“形态高拟真”",
    vision_p1_strat_sub:
      "在第一阶段，我们不求真正的复杂离散调度和真实网络协议通信，而是聚焦于<b>“外表模块完整、细节严谨逼真、第一眼无可挑剔”</b>。如何以最低的算力与研发成本，达成顶级半导体专家一眼认可的专业级工业质感？",
    vision_p1_t1_title: "1. 机台工业特征模块解构",
    vision_p1_t1_desc:
      "告别单调长方体白模。通过轻量参数化组件，拼装出半导体设备的典型工业解构：",
    vision_p1_t1_i1: "<b>EFEM 微环境仓</b>：半透明防静电观察窗与 SCARA 机械臂",
    vision_p1_t1_i2: "<b>Load Ports</b>：2~4 个倾斜装载站台，带定位销与三色灯",
    vision_p1_t1_i3: "<b>Cluster Tool</b>：中央真空传输室与 4~6 个圆柱形反应腔",
    vision_p1_t1_i4:
      "<b>附件细节</b>：顶部排风法兰、悬臂操作屏与 SEMI E10 塔灯",
    vision_p1_t1_tag: "成本：极低（纯前端几何拼接） · 拟真度：跃升",

    vision_p1_t2_title: "2. 洁净室空间质感与立体层级",
    vision_p1_t2_desc: "营造半导体无尘车间标志性的空间氛围与纵深层次：",
    vision_p1_t2_i1: "<b>微孔防静电地板</b>：棋盘式 30% 开孔率通风板与下沉缝隙",
    vision_p1_t2_i2:
      "<b>天花 FFU 阵列</b>：满布规整百叶滤网与冷白高流明无影照明",
    vision_p1_t2_i3:
      "<b>黄光区琥珀氛围</b>：光刻 Bay 特有的 589nm 金黄琥珀色光晕",
    vision_p1_t2_i4: "<b>Subfab 工业色标管廊</b>：纯水蓝、特气橙、真空灰排布",
    vision_p1_t2_tag: "空间感：沉浸式 · 辨识度：极高",

    vision_p1_t3_title: "3. 机械传动“假动作”拟真",
    vision_p1_t3_desc:
      "即便没有后台调度算法，用纯前端时间轴编排具有说服力的机械动作：",
    vision_p1_t3_i1:
      "<b>天车取放动作</b>：天车停稳 $\\rightarrow$ 抓手垂直吊索下落 $\\rightarrow$ FOUP 放置",
    vision_p1_t3_i2:
      "<b>机械臂出入片</b>：Load Port 开启，机械手夹持 300mm 晶圆送入腔体",
    vision_p1_t3_i3:
      "<b>腔体发光</b>：刻蚀腔视窗亮起淡紫色等离子体辉光(Plasma Glow)",
    vision_p1_t3_i4:
      "<b>塔灯呼吸</b>：绿色工作恒亮，蓝色等待闪烁，黄色换批呼吸",
    vision_p1_t3_tag: "视觉信服力：顶级 · 观看体验：生动",

    vision_p1_t4_title: "4. “物理自洽”的伪遥测面板",
    vision_p1_t4_desc:
      "不接真实机台，但面板上的波形完全符合半导体制造物理特性：",
    vision_p1_t4_i1:
      "<b>刻蚀 RF 曲线</b>：抽真空陡降 $\\rightarrow$ 辉光点火峰值 $\\rightarrow$ 终点(EPD)阶跃",
    vision_p1_t4_i2:
      "<b>温度热滞后</b>：静电吸盘(Chuck)控温呈现经典的一阶惯性响应",
    vision_p1_t4_i3:
      "<b>休哈特控制图</b>：严格呈现 UCL/LCL 边界与偶尔触发的 Nelson 准则点",
    vision_p1_t4_i4:
      "<b>SEMI E10 OEE</b>：按运行比率实时滚动的 PR / Standby / Down 百分比",
    vision_p1_t4_tag: "专家审视：无破绽 · 工业严谨感：拉满",

    vision_p1_takeaway_title: "Phase 1 的核心价值：以轻资产打动产业与学术界",
    vision_p1_takeaway_desc:
      "先通过极致的“外在皮相与工业模块完整度”建立视觉认同与行业声量，让所有人直观看到数字孪生落地的最终图景；再在 Phase 2/3 中逐步填入真实的离散事件仿真（DES）与 GEM300 工业内核，步步为营。",
    vision_p1_takeaway_btn: "查看当前 Phase 1 原型",

    // Roadmap
    vision_roadmap_title: "四阶段演进路线图",
    vision_roadmap_sub: "从“外观模块形似”到“全闭环工业孪生”的务实演进路径。",
    vision_rm_completed: "✓ 已完成",
    vision_rm_p1_title: "形态与视觉高拟真",
    vision_rm_p1_desc:
      "模块看起来极其完整逼真。机台解构(EFEM/Chamber)、微孔地板、黄光区、Subfab管廊、OHT天车取放动作、拟真FDC波形。",
    vision_rm_p1_tag: "✓ 纯前端低成本高感知",
    vision_rm_p2_title: "离散事件与仿真流转",
    vision_rm_p2_desc:
      "引入真实 SimPy / Rust 离散事件仿真（DES）。实现重入式 Routing 工步流转、Q-Time 驻留时间窗口与天车路网防死锁调度。（已通过 MIMAC-2026 benchmark 与浏览器内仿真交付）",
    vision_rm_p2_tag: "→ 物流与节拍真实自洽",
    vision_rm_p3_title: "GEM300 与虚拟机台沙箱",
    vision_rm_p3_desc:
      "基于 secsgem 开源库实现虚拟 GEM300 设备服务端。支持 MES 远程命令下发、Recipe 参数设定与高频 EDA 遥测数据流。",
    vision_rm_p3_tag: "→ 工业协议互联互通",
    vision_rm_p4_title: "全闭环生态与开放基准",
    vision_rm_p4_desc:
      "集成 STDF/KLARF 工业流解析，发布开放 28nm 参考基准数据包；支持 Docker-Compose 本地单键拉起与开放 API 插件扩展。",
    vision_rm_p4_tag: "→ 开放生态持续演进",

    // Version Milestones
    vision_milestones_badge: "RELEASE MILESTONES",
    vision_milestones_title: "版本里程碑",
    vision_milestones_sub: "SemiconFab 从公开发布至今的持续迭代轨迹。",
    vision_ms_v1_0: "公开发布：121 条记录的设备目录、3D twin、纯静态网站",
    vision_ms_v1_1: "153 条记录，确定性 ID；二手设备市场数据并入",
    vision_ms_v1_2: "167 条记录，8 个真实比例 L1 模型",
    vision_ms_v1_3: "benchmark 可交互：浏览器内 Pyodide 派工仿真",
    vision_ms_v1_4: "Follow-a-wafer 路线动画；屋顶/HVAC 基础设施层",

    // Matrix
    vision_matrix_title: "商业巨头方案 vs 开源技术栈替代矩阵",
    vision_matrix_sub:
      "对标国际领先半导体制造软件，梳理各功能层的开放架构替代方案。",
    vision_matrix_th_layer: "架构层级",
    vision_matrix_th_std: "工业标准 / 协议",
    vision_matrix_th_comm: "商业垄断方案",
    vision_matrix_th_open: "Open Initiative 推荐栈",
    vision_matrix_th_val: "实现功能与价值",
    vision_mat_r1_layer: "空间与设备三维",
    vision_mat_r1_val: "轻量网页级 2D/3D 洁净室与机台多视角工程投影",
    vision_mat_r2_layer: "天车与产线仿真",
    vision_mat_r2_val: "重入式 Routing、FOUP 调度优化与防死锁天车网络流",
    vision_mat_r3_layer: "机台通讯与遥测",
    vision_mat_r3_val: "双向 S1F1 握手、S6F11 遥测事件及虚拟机台仿真器",
    vision_mat_r4_layer: "实时过程质量控制",
    vision_mat_r4_val: "休哈特控制图、Nelson 8 准则与腔体传感器异常检测",
    vision_mat_r5_layer: "良率与晶圆图管理",
    vision_mat_r5_val: "ATE 数据流解析、缺陷空间聚类与多工位共性溯源(RCA)",
    vision_mat_r6_layer: "工业数据中枢",
    vision_mat_r6_val: "毫秒级事件流吞吐、腔体时序与百亿级晶粒参数化分析",

    // CTA
    vision_cta_title: "共同构建半导体智能制造的开放未来",
    vision_cta_desc:
      "无论您是半导体工艺工程师、工业软件架构师、运筹优化算法学者，还是对芯片制造充满热情的高校师生，SemiconFab Open Initiative 期待您的加入。",
    vision_cta_btn_twin: "启动 3D 数字孪生系统",
    vision_cta_btn_contact: "联系倡议工作组",
    vision_footer_home: "首页",
    vision_footer_twin: "3D 数字孪生",
    vision_footer_license:
      "源码公开 · PolyForm Noncommercial 1.0.0 · 教育与个人使用免费 · 商业授权支持持续开发。",
  },
};

// Generate traditional Chinese (zh-TW), Japanese (ja), Korean (ko), German (de), French (fr), Italian (it), Spanish (es)
(function populateOtherLanguages() {
  const en = VISION_I18N["en"];
  const zh = VISION_I18N["zh-CN"];

  // Traditional Chinese (zh-TW)
  const tw = JSON.parse(JSON.stringify(zh));
  tw["vision_brand_sub"] = "半導體晶圓廠數位分身開放倡議";
  tw["vision_page_title"] =
    "Open Initiative 願景與 6 大核心支柱 — SemiconFab.org";
  tw["vision_hero_title_1"] = "開放半導體晶圓製造";
  tw["vision_hero_title_2"] = "數位分身全景願景白皮書";
  tw["vision_nav_pillars"] = "6 大核心支柱";
  tw["vision_nav_phase1"] = "Phase 1 方案";
  tw["vision_nav_roadmap"] = "演進路線圖";
  tw["vision_nav_stack"] = "開源替代矩陣";
  tw["vision_hero_cta_pillars"] = "深入探索 6 大核心支柱";
  tw["vision_hero_cta_phase1"] = "Phase 1 形態擬真方案";
  tw["vision_hero_cta_twin"] = "體驗 3D 無塵室原型";
  tw["vision_footer_home"] = "首頁";
  tw["vision_footer_twin"] = "3D 數位分身";
  VISION_I18N["zh-TW"] = tw;

  // Japanese (ja)
  const ja = JSON.parse(JSON.stringify(en));
  ja["vision_brand_sub"] = "半導体ファブ・デジタルツイン・オープン構想";
  ja["vision_page_title"] =
    "オープン構想ビジョンと6大コアピラー — SemiconFab.org";
  ja["vision_nav_pillars"] = "6大コアピラー";
  ja["vision_nav_phase1"] = "Phase 1 戦略";
  ja["vision_nav_roadmap"] = "ロードマップ";
  ja["vision_nav_stack"] = "スタックマトリクス";
  ja["vision_hero_badge"] =
    "OPEN INITIATIVE · ビジョン白書とアーキテクチャ設計図";
  ja["vision_hero_title_1"] = "オープンな半導体ファブ";
  ja["vision_hero_title_2"] = "デジタルツイン・ビジョン";
  ja["vision_hero_cta_pillars"] = "6大ピラーを詳しく見る";
  ja["vision_hero_cta_phase1"] = "Phase 1 高忠実度戦略";
  ja["vision_hero_cta_twin"] = "3D クリーンルームを体験";
  ja["vision_why_title"] = "なぜ半導体製造にオープン構想が必要なのか？";
  ja["vision_pillars_title"] = "フルスタック・デジタルツイン 6大コアピラー";
  ja["vision_roadmap_title"] = "4段階の進化ロードマップ";
  ja["vision_matrix_title"] =
    "商用大手スイート vs オープンソース代替マトリクス";
  ja["vision_cta_title"] = "半導体スマート製造のオープンな未来を共に創る";
  ja["vision_cta_btn_twin"] = "3D デジタルツインを起動";
  ja["vision_cta_btn_contact"] = "イニシアティブ連絡窓口";
  ja["vision_footer_home"] = "ホーム";
  ja["vision_footer_twin"] = "3D デジタルツイン";
  VISION_I18N["ja"] = ja;

  // Korean (ko)
  const ko = JSON.parse(JSON.stringify(en));
  ko["vision_brand_sub"] = "반도체 팹 디지털 트윈 오픈 이니셔티브";
  ko["vision_page_title"] =
    "오픈 이니셔티브 비전 및 6대 핵심 기둥 — SemiconFab.org";
  ko["vision_nav_pillars"] = "6대 핵심 기둥";
  ko["vision_nav_phase1"] = "Phase 1 전략";
  ko["vision_nav_roadmap"] = "로드맵";
  ko["vision_nav_stack"] = "스택 매트릭스";
  ko["vision_hero_badge"] = "OPEN INITIATIVE · 비전 백서 및 아키텍처 청사진";
  ko["vision_hero_title_1"] = "오픈 반도체 팹";
  ko["vision_hero_title_2"] = "디지털 트윈 비전";
  ko["vision_hero_cta_pillars"] = "6대 기둥 살펴보기";
  ko["vision_hero_cta_phase1"] = "Phase 1 형태 시뮬레이션";
  ko["vision_hero_cta_twin"] = "3D 클린룸 프로토타입 체험";
  ko["vision_why_title"] = "반도체 제조에 오픈 이니셔티브가 필요한 이유";
  ko["vision_pillars_title"] = "풀스택 디지털 트윈 6대 핵심 기둥";
  ko["vision_roadmap_title"] = "4단계 진화 로드맵";
  ko["vision_matrix_title"] = "상용 독점 솔루션 vs 오픈소스 대체 매트릭스";
  ko["vision_cta_title"] = "반도체 스마트 제조의 열린 미래를 함께 만듭니다";
  ko["vision_cta_btn_twin"] = "3D 디지털 트윈 시작";
  ko["vision_cta_btn_contact"] = "이니셔티브 문의하기";
  ko["vision_footer_home"] = "홈";
  ko["vision_footer_twin"] = "3D 디지털 트윈";
  VISION_I18N["ko"] = ko;

  // German (de)
  const de = JSON.parse(JSON.stringify(en));
  de["vision_brand_sub"] = "Open Fab Digital Twin Initiative";
  de["vision_page_title"] =
    "Open Initiative Vision & 6 Säulen — SemiconFab.org";
  de["vision_nav_pillars"] = "6 Kernsäulen";
  de["vision_nav_phase1"] = "Phase 1 Strategie";
  de["vision_nav_roadmap"] = "Roadmap";
  de["vision_nav_stack"] = "Stack-Matrix";
  de["vision_hero_badge"] =
    "DIE OPEN INITIATIVE · VISION WHITE-PAPER & ARCHITEKTUR";
  de["vision_hero_title_1"] = "Die Open Semiconductor";
  de["vision_hero_title_2"] = "Fab Digital Twin Vision";
  de["vision_hero_cta_pillars"] = "6 Kernsäulen erkunden";
  de["vision_hero_cta_phase1"] = "Phase 1 Morphologische Strategie";
  de["vision_hero_cta_twin"] = "3D-Reinraum-Prototyp testen";
  de["vision_why_title"] =
    "Warum braucht die Halbleiterfertigung eine Open Initiative?";
  de["vision_pillars_title"] = "Die 6 grundlegenden Digital-Twin-Säulen";
  de["vision_roadmap_title"] = "Vier-Phasen-Entwicklungs-Roadmap";
  de["vision_matrix_title"] = "Kommerzielle Suiten vs. Open-Source-Matrix";
  de["vision_cta_title"] =
    "Die offene Zukunft der Halbleiterfertigung gestalten";
  de["vision_cta_btn_twin"] = "3D Digital Twin starten";
  de["vision_cta_btn_contact"] = "Arbeitsgruppe kontaktieren";
  VISION_I18N["de"] = de;

  // French (fr)
  const fr = JSON.parse(JSON.stringify(en));
  fr["vision_brand_sub"] = "Initiative Ouverte pour le Jumeau Numérique de Fab";
  fr["vision_page_title"] =
    "Vision de l'Initiative Ouverte & 6 Piliers — SemiconFab.org";
  fr["vision_nav_pillars"] = "6 Piliers Fondamentaux";
  fr["vision_nav_phase1"] = "Stratégie Phase 1";
  fr["vision_nav_roadmap"] = "Feuille de Route";
  fr["vision_nav_stack"] = "Matrice des Stacks";
  fr["vision_hero_badge"] =
    "L'INITIATIVE OUVERTE · LIVRE BLANC & SCHÉMA ARCHITECTURAL";
  fr["vision_hero_title_1"] = "La Vision Ouverte du";
  fr["vision_hero_title_2"] = "Jumeau Numérique de Fab";
  fr["vision_hero_cta_pillars"] = "Explorer les 6 Piliers";
  fr["vision_hero_cta_phase1"] = "Stratégie Morphologique Phase 1";
  fr["vision_hero_cta_twin"] = "Tester le Prototype 3D";
  fr["vision_why_title"] =
    "Pourquoi la fabrication de puces a-t-elle besoin d'une initiative ouverte ?";
  fr["vision_pillars_title"] = "Les 6 Piliers Fondamentaux du Jumeau Numérique";
  fr["vision_roadmap_title"] = "Feuille de Route d'Évolution en 4 Phases";
  fr["vision_matrix_title"] = "Solutions Commerciales vs Matrice Open Source";
  fr["vision_cta_title"] =
    "Construire Ensemble l'Avenir Ouvert de la Microélectronique";
  fr["vision_cta_btn_twin"] = "Lancer le Jumeau 3D";
  fr["vision_cta_btn_contact"] = "Contacter le Groupe de Travail";
  VISION_I18N["fr"] = fr;

  // Italian (it), Spanish (es)
  const it = JSON.parse(JSON.stringify(en));
  it["vision_page_title"] =
    "Visione Open Initiative & 6 Pilastri — SemiconFab.org";
  it["vision_nav_pillars"] = "6 Pilastri Fondamentali";
  it["vision_nav_phase1"] = "Strategia Fase 1";
  it["vision_nav_roadmap"] = "Tabella di Marcia";
  it["vision_hero_cta_pillars"] = "Esplora i 6 Pilastri";
  it["vision_cta_btn_twin"] = "Avvia il Gemello 3D";
  VISION_I18N["it"] = it;

  const es = JSON.parse(JSON.stringify(en));
  es["vision_page_title"] =
    "Visión de la Iniciativa Abierta y 6 Pilares — SemiconFab.org";
  es["vision_nav_pillars"] = "6 Pilares Fundamentales";
  es["vision_nav_phase1"] = "Estrategia Fase 1";
  es["vision_nav_roadmap"] = "Hoja de Ruta";
  es["vision_hero_cta_pillars"] = "Explorar 6 Pilares";
  es["vision_cta_btn_twin"] = "Iniciar Gemelo 3D";
  VISION_I18N["es"] = es;
})();

// Automatically merge VISION_I18N into global or window I18N_DICTIONARY
(function mergeTranslations() {
  const target =
    typeof I18N_DICTIONARY !== "undefined"
      ? I18N_DICTIONARY
      : typeof window !== "undefined" && window.I18N_DICTIONARY
        ? window.I18N_DICTIONARY
        : null;
  if (target) {
    Object.keys(VISION_I18N).forEach((lang) => {
      if (!target[lang]) target[lang] = {};
      Object.assign(target[lang], VISION_I18N[lang]);
    });
  }
  if (typeof window !== "undefined") {
    window.VISION_I18N = VISION_I18N;
  }
})();
