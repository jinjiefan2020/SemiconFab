// ==========================================
// SemiconFab.org — Fab Construction Cost Bilingual Dictionary
// Model & Report: "Building a Fab: Where the Money Goes Beyond the Equipment"
// ==========================================

const FAB_COST_I18N = {
  en: {
    fab_cost_page_title:
      "Fab Construction Costs: What's Beyond the Equipment — SemiconFab.org",
    fab_cost_h1: "Building a Fab: Where the Money Goes Beyond the Equipment",
    fab_cost_lede:
      'Process tools account for 70–80% of the total investment in an advanced fab. The remaining 20–30% — building, cleanroom, ultrapure water, power, gases, wastewater, AMHS, land, and engineering design — is the so-called "construction cost". This page brings together the shares, unit prices, and reference projects that can be found in public sources into a parametric model that estimates cost by <strong>process node × capacity (WSPM)</strong>, and states plainly which figures come from official sources, which are triangulated across multiple sources, and which cannot be found at all.',
    fab_cost_meta_line:
      "Sources: public web research conducted on 2026-10-18 (trade media, practitioner interviews, analyst estimates, and company announcements). All amounts are in US dollars. No institution (SEMI / McKinsey / BCG / SIA) has ever published a complete cost breakdown in public channels — the breakdown below is triangulated across multiple sources and is the weakest link in this data; read it with that caveat.",

    // 4 Key Stats
    fab_cost_stat1_num: "70–80%",
    fab_cost_stat1_lbl: "Process tools as a share of total cost",
    fab_cost_stat1_src:
      "New advanced fab · construction-physics, 2024; lithography alone is ~20% of total cost",
    fab_cost_stat2_num: "$4–6B",
    fab_cost_stat2_lbl: "Facility portion (building + cleanroom + utilities)",
    fab_cost_stat2_src:
      "For a large fab with total investment >$20B · Exyte/M+W practitioner Blaschitz, 2025",
    fab_cost_stat3_num: "≈ 2/3",
    fab_cost_stat3_lbl: 'MEP & utilities share of "construction" cost',
    fab_cost_stat3_src:
      "The remaining ~1/3 is cleanroom fit-out and building structure · construction-physics, 2024",
    fab_cost_stat4_num: "$6B / $11B",
    fab_cost_stat4_lbl: "Samsung Taylor official split",
    fab_cost_stat4_src:
      "Of the $17B total: building $6B (35%) / equipment $11B (65%) · Samsung official announcement, Nov 2021",

    // Estimator
    fab_cost_calc_title: "Parametric Estimator",
    fab_cost_calc_note:
      "Method: total investment = cost per 1k WSPM (process anchor) × capacity; non-equipment construction cost = total investment × facility share. All anchors are published figures from the \"Node scaling\" table below; the facility share uses the report's 20–30% range (the upper bound can be relaxed to Samsung Taylor's official 35% building share). This is a rough model, not a quotation.",
    fab_cost_calc_lbl_node:
      "Process anchor (total-cost basis, incl. equipment)",
    fab_cost_opt_mature28:
      "28nm-class mature — $156M / 1k WSPM (Kumamoto Fab 1 actual)",
    fab_cost_opt_node3: "3nm — $375–500M / 1k WSPM (IBS)",
    fab_cost_opt_node2samsung:
      "2nm — $340M / 1k WSPM (Samsung Taylor published figure)",
    fab_cost_opt_node2ibs: "2nm — $560M / 1k WSPM (IBS)",
    fab_cost_opt_node5early:
      "5nm early — $600M / 1k WSPM (TSMC Arizona 2020 announcement basis)",
    fab_cost_opt_dram: "Advanced DRAM — $69M / 1k WSPM (SK hynix Yongin Y2)",
    fab_cost_calc_node_hint:
      "The report gives no per-1k-WSPM cost anchor for 7nm, so no 7nm option is offered — do not fabricate data by interpolation. IBS figures are considered high by SemiWiki practitioners; for the same 2nm node there is also Samsung's published $340M figure, listed side by side for comparison.",
    fab_cost_calc_lbl_wspm: "Capacity, WSPM (wafer starts per month)",
    fab_cost_calc_wspm_hint:
      "Actual scale of the anchor projects: Kumamoto Fab 1 55k, IBS's 2nm model 50k, Yongin Y2 up to 360k at full build-out (six phases).",
    fab_cost_calc_lbl_share:
      "Facility (non-equipment) share of total investment",
    fab_cost_calc_share_lo: "20% (report range low end)",
    fab_cost_calc_share_hi: "35% (Samsung official building share)",
    fab_cost_calc_share_hint:
      "20–30% is the reported range for large advanced fabs (facilities $4–6B / total investment >$20B); 35% corresponds to Samsung Taylor's official building share. Mature-node fabs have a lower equipment share (in IMARC's split of an Indian mature fab, equipment is only 45%), so the facility share would be correspondingly higher — this slider's upper bound does not cover that case; judge such results separately.",
    fab_cost_calc_lbl_region:
      "Construction region (affects timeline display only)",
    fab_cost_calc_reg_asia: "Asia",
    fab_cost_calc_reg_us: "US",
    fab_cost_calc_reg_eu: "Europe",
    fab_cost_calc_reg_hint:
      "Timeline basis: permitting + design → first wafer out (Blaschitz, 2025). The report gives no credible regional cost multiplier, so region does not enter the cost calculation; what is known is that building a fab in the US costs 30% (Intel basis) to 4× (TSMC basis) more than in Taiwan, and much of the premium comes from the longer schedule itself.",

    // Estimator Results
    fab_cost_res_build_lbl:
      "Estimated non-equipment construction cost (building + cleanroom + utilities, etc.)",
    fab_cost_res_build_sub_tmpl: "Total investment × {share}% facility share",
    fab_cost_res_total_lbl: "Total investment (incl. equipment)",
    fab_cost_res_equip_lbl: "Of which: process tools",
    fab_cost_res_equip_sub: "Total investment minus construction cost",
    fab_cost_res_services_lbl: "Within construction: MEP & utility services",
    fab_cost_res_services_sub:
      "≈ 2/3 of construction cost: HVAC, UPW, power, exhaust, gas and chemical systems, etc. (construction-physics)",
    fab_cost_res_shell_lbl:
      "Within construction: cleanroom fit-out & building structure",
    fab_cost_res_shell_sub: "≈ 1/3 of construction cost (construction-physics)",
    fab_cost_res_amhs_lbl:
      "Of which: AMHS (overhead transport / stocker systems), order-of-magnitude estimate",
    fab_cost_res_amhs_sub:
      "5–10% of construction cost (market-research basis, 2025–26); another basis is 3–5% of equipment investment",
    fab_cost_res_time_lbl:
      "Reference timeline: permitting + design → first wafer out",
    fab_cost_legend_equip: "Process tools",
    fab_cost_legend_services: "MEP & utilities",
    fab_cost_legend_shell: "Cleanroom fit-out & building structure",
    fab_cost_calc_foot:
      "Model limitations (from the report): ① No parametric capacity curve (cost ∝ WSPM<sup>x</sup>) exists in public sources; this model extrapolates total cost linearly with capacity — but the facility portion actually scales sub-linearly (a UPW plant, substation, or CUB does not double with capacity), so the facility share will be underestimated for small fabs and overestimated for large ones; a phase-2 fab on the same campus shares infrastructure and costs significantly less. ② Land (~3–5%, $20M–200M, 100–500 acres; weak source quality) and engineering / permitting / commissioning (~3–8%) are not itemized separately and are contained within the uncertainty range of the facility share. ③ The ~+30% per-node rule of thumb (construction-physics) is driven mainly by more expensive tools and more mask / process steps, and lands on the equipment side.",

    // Cost Breakdown Table
    fab_cost_split_title: "Total Cost Breakdown",
    fab_cost_split_note:
      'The table below is stitched together from multiple sources, and the bases are not consistent across rows (some are shares of total project cost, others of the construction budget) — cite any figure together with its note. A table on civilstructures.in lists "manufacturing equipment" at 35–50%, but its line items sum to over 100% and it describes a construction / installation budget, not total project cost; this page does not adopt it on a total-cost basis, citing it only where no better source exists for a facility line item, with a flag.',
    fab_cost_th_component: "Component",
    fab_cost_th_share: "Share of total cost",
    fab_cost_th_notes: "Notes",
    fab_cost_th_source: "Source",
    fab_cost_split_a_comp: "(a) Process tools",
    fab_cost_split_a_share: "70–80%",
    fab_cost_split_a_notes:
      "Advanced-node basis. Samsung Taylor's official announcement was 65% ($11B / $17B); IMARC's split for a mature fab (India) is only 45%. The equipment share has risen over time: mid-1980s DRAM fabs were roughly 50/50, and equipment has dominated since the late 1990s. Lithography alone is ~20% of total cost.",
    fab_cost_split_a_src:
      "construction-physics (2024); Samsung official announcement (Nov 2021); imarcgroup.com",
    fab_cost_split_b_comp: "(b) Building + cleanroom",
    fab_cost_split_b_share: "~10–15%",
    fab_cost_split_b_notes:
      'An implied value backed out by subtracting the utilities portion from "total facilities 20–30%", not a directly published figure. Samsung Taylor\'s $6B (35%) is the official figure for building + site (incl. cleanroom), not fully comparable in basis.',
    fab_cost_split_b_src:
      "Exyte/M+W practitioner via TechSpot (2025); Samsung official (2021)",
    fab_cost_split_c_comp:
      "(c) Utilities (UPW, power, HVAC, gases, chemicals, wastewater)",
    fab_cost_split_c_share: "~8–15%",
    fab_cost_split_c_notes:
      'Another basis: ~2/3 of total construction cost. In IMARC\'s split, utilities are 8% and cleanroom infrastructure (HVAC) 15% (mature-node basis). See the "Facility line items" table below for unit prices.',
    fab_cost_split_c_src: "construction-physics (2024); imarcgroup.com",
    fab_cost_split_d_comp: "(d) Land",
    fab_cost_split_d_share: "3–5%",
    fab_cost_split_d_notes:
      "Roughly $20M–200M, 100–500 acres. Cases such as Kumamoto and Boise show land itself is a small share; site development is counted separately.",
    fab_cost_split_d_src: "civilstructures.in (2026)",
    fab_cost_split_e_comp:
      "(e) Other (engineering design, permitting, commissioning)",
    fab_cost_split_e_share: "~3–8%",
    fab_cost_split_e_notes:
      "civilstructures basis: design 5–10%, test / commissioning 3%; IMARC basis: IT / security / compliance 5%. This is the weakest line item, with no strong industry source.",
    fab_cost_split_e_src: "civilstructures.in; imarcgroup.com",

    // Node Scaling
    fab_cost_node_title: "Node Scaling: Total Cost per 1k WSPM",
    fab_cost_node_note:
      "On a consistent basis (total investment incl. equipment), node is the second-largest variable — the largest is actually <strong>logic vs. memory</strong>: advanced DRAM costs less than half per 1k WSPM ($69M) of mature 28nm logic ($156M). Rule of thumb: each node advance adds ~30% to total cost.",
    fab_cost_chart_aria:
      "Bar chart: total cost per 1k WSPM — DRAM 69, 28nm 156, 2nm Samsung basis 340, 3nm range 375 to 500, 2nm IBS basis 560, 5nm early 600, in millions of dollars",
    fab_cost_chart_note:
      "Units: millions of dollars per 1k WSPM. The 3nm figure is the range IBS gives ($15–20B @ 40k WSPM), shown as a range bar; the rest are single-point anchors. The early 5nm figure (TSMC Arizona 2020 announcement, $12B / 20k) includes a first-fab premium and does not represent mature 5nm levels.",
    fab_cost_th_node: "Node",
    fab_cost_th_wspm_cost: "$/1k WSPM",
    fab_cost_th_basis: "Basis",
    fab_cost_node_r1_name: "Advanced DRAM",
    fab_cost_node_r1_cost: "~$69M",
    fab_cost_node_r1_basis:
      "SK hynix Yongin Y2: $24.8B / 360k WSPM (full build-out, six phases)",
    fab_cost_node_r1_src: "fool.com / techtimes (2026)",
    fab_cost_node_r2_name: "28nm-class (mature)",
    fab_cost_node_r2_cost: "~$156M",
    fab_cost_node_r2_basis:
      "TSMC Kumamoto Fab 1 (22/28nm, 12/16nm): $8.6B / 55k WSPM, incl. $3.2B Japanese government subsidy",
    fab_cost_node_r2_src: "semiwiki / trendforce (2024–25)",
    fab_cost_node_r3_name: "28–90nm (mature, general)",
    fab_cost_node_r3_cost: "~$125–275M",
    fab_cost_node_r3_basis: "India target fabs: $5–11B each",
    fab_cost_node_r3_src: "fabs.pranaykotas.com India tracker (2026)",
    fab_cost_node_r4_name: "Mature specialty",
    fab_cost_node_r4_cost: "~$133M",
    fab_cost_node_r4_basis:
      "GlobalFoundries Malta phase 1: $10B / ~75k WSPM (900k wafers / year)",
    fab_cost_node_r4_src: "medium / tai-semicon (2026)",
    fab_cost_node_r5_name: "3nm",
    fab_cost_node_r5_cost: "$375–500M",
    fab_cost_node_r5_basis: "IBS: $15–20B @ 40k WSPM",
    fab_cost_node_r5_src: "IBS via semiwiki / techspot (2014/2023)",
    fab_cost_node_r6_name: "2nm (published basis)",
    fab_cost_node_r6_cost: "~$340M",
    fab_cost_node_r6_basis:
      "Samsung Taylor: $17B / ~50k WSPM (announced in 2021 as 5nm; now 2nm GAA)",
    fab_cost_node_r6_src: "dmc-education / sammyguru",
    fab_cost_node_r7_name: "2nm (IBS basis)",
    fab_cost_node_r7_cost: "$560M",
    fab_cost_node_r7_basis: "IBS: $28B @ 50k WSPM",
    fab_cost_node_r7_src: "techspot.com (Dec 2023)",
    fab_cost_node_r8_name: "5nm (early adopter)",
    fab_cost_node_r8_cost: "~$600M",
    fab_cost_node_r8_basis: "TSMC Arizona 2020 announcement: $12B / 20k WSPM",
    fab_cost_node_r8_src: "nasdaq.com (2020)",
    fab_cost_node_r9_name: "3nm (small fab)",
    fab_cost_node_r9_cost: "~$1.1B",
    fab_cost_node_r9_basis:
      'Kumamoto Fab 2: $17B / 15k WSPM Small fabs have markedly higher unit facility costs — see "Capacity scaling"',
    fab_cost_node_r9_src:
      "datacenterdynamics citing Japanese local media (2026)",

    // Facility Line Items
    fab_cost_fac_title: "Facility Line Items (the Core of Non-Equipment Cost)",
    fab_cost_fac_note:
      'Below are the line-item anchors found in the report. Note the enormous spread in cleanroom unit prices: base fit-out and "tool-ready" state differ by more than 4×, and EUV lithography bays double again — a unit price without a state condition is meaningless.',
    fab_cost_th_item: "Line item",
    fab_cost_th_price_scale: "Price / scale",
    fab_cost_fac_r1_name: "Cleanroom (ISO Class 1–3 ballroom)",
    fab_cost_fac_r1_price:
      "Fit-out + hardware $1,200–2,500/m²; tool-ready $5,000–10,000/m²; EUV bays $20,000+/m²; another ISO Class 3 basis cites >$700/ft² (≈$7,500/m²)",
    fab_cost_fac_r1_notes:
      "Large fabs can have 500k–1M sq ft of cleanroom; a typical large fab is ~430k sq ft with 2,000 tools (Blaschitz)",
    fab_cost_fac_r1_src:
      "civilstructures.in (2026); sst.semiconductor-digest.com; asianometry via construction-physics",
    fab_cost_fac_r2_name: "Ultrapure water (UPW) system",
    fab_cost_fac_r2_price:
      "Advanced node, 100k WSPM: $200–500M, capacity 10–20 MGD, ~2,000–5,000 gallons of water per wafer start, reuse systems add another $50–150M; mature node: $50–150M, 2–8 MGD",
    fab_cost_fac_r2_notes:
      "Hard anchor: Veolia's contract for Intel Chandler Fabs 52+62 was $120M, 6 MGD total, 18.2 MΩ·cm (Sep 2023)",
    fab_cost_fac_r2_src:
      "semiconductorx.com; emergenresearch (Veolia contract)",
    fab_cost_fac_r3_name: "Power",
    fab_cost_fac_r3_price:
      "A large advanced fab draws on the order of 100 MW; TSMC Arizona at full build-out ~200 MW; 2nm uses 3.5× the energy of 28nm",
    fab_cost_fac_r3_notes:
      "Electrical infrastructure total $500M–2B (weak source quality); <strong>no standalone substation cost found</strong>. TSMC power intensity per wafer·mask-layer: 27.7 kW in 2022 → 40.5 kW in the 3nm ramp period (S&P basis; units as in the original source)",
    fab_cost_fac_r3_src:
      "construction-physics (2024); sanieinstitute (2025); Deloitte; datacenterdynamics",
    fab_cost_fac_r4_name: "HVAC / cleanroom air handling",
    fab_cost_fac_r4_price:
      'No standalone unit price: included within "MEP services ≈ 2/3 of construction cost"; in small cleanroom projects HVAC can be 30–50%',
    fab_cost_fac_r4_notes:
      "Cleanroom air recirculates hundreds of times per hour, making HVAC one of the main drivers of facility energy use and cost",
    fab_cost_fac_r4_src: "construction-physics (2024); crestmontcapital.com",
    fab_cost_fac_r5_name: "Bulk gases (N₂/O₂/Ar)",
    fab_cost_fac_r5_price:
      "On-site air separation unit (ASU): large cryogenic plants $50–300M; >500 t/day class $200–350M",
    fab_cost_fac_r5_notes:
      "Hard anchor: Linde's $1B Phoenix gas complex (2 new ASUs serving two other fabs, Jul 2026). A large logic fab uses ~50,000 Nm³/h of nitrogen",
    fab_cost_fac_r5_src:
      "dataintelo (2026); openpr (Linde announcement); construction-physics",
    fab_cost_fac_r6_name: "Chemicals + wastewater / exhaust treatment",
    fab_cost_fac_r6_price:
      "<strong>No standalone cost found</strong>; only a combined water + wastewater basis of $200M–1B (incl. UPW)",
    fab_cost_fac_r6_notes:
      "TSMC Arizona has committed to 100% water reuse (semiconductorx)",
    fab_cost_fac_r6_src: "civilstructures.in (envelope basis, weak quality)",
    fab_cost_fac_r7_name: "AMHS (overhead transport + stockers)",
    fab_cost_fac_r7_price:
      "5–10% of construction cost; or 3–5% of equipment investment — i.e., ~$0.2–0.8B for a $20B fab",
    fab_cost_fac_r7_notes:
      "Both bases come from market research firms, not project disclosures",
    fab_cost_fac_r7_src: "snsinsider.com; indexbox.io (2025–26)",
    fab_cost_fac_r8_name:
      "Buildings (fab + subfab + CUB central utility building)",
    fab_cost_fac_r8_price:
      "Total facilities $4–6B (for a fab with total investment >$20B, incl. cleanroom and utilities); Samsung Taylor building $6B / total $17B",
    fab_cost_fac_r8_notes:
      "Construction inputs for one large fab, order of magnitude: 30–40M labor-hours, 83,000 tons of steel, 785,000 cubic yards of concrete (Blaschitz)",
    fab_cost_fac_r8_src:
      "Blaschitz/Exyte via TechSpot (2025); Samsung official (2021)",

    // Reference Projects
    fab_cost_proj_title: "Reference Projects (Published Figures)",
    fab_cost_proj_note:
      'All totals in this table are <strong>total investment including equipment</strong> — "building-only" figures are almost never disclosed, and Samsung Taylor\'s $6B building figure is the only clean official anchor. Projects without disclosed capacity are marked as such; nothing is inferred.',
    fab_cost_th_project: "Project",
    fab_cost_th_capacity: "Capacity (WSPM)",
    fab_cost_th_pub_invest: "Published total investment",
    fab_cost_th_year_ann: "Year announced",
    fab_cost_proj_r1_name: "Samsung Taylor, Texas",
    fab_cost_proj_r1_node: "2nm GAA (Fab 1; announced as 5nm)",
    fab_cost_proj_r1_cap: "~50k (trade reporting)",
    fab_cost_proj_r1_inv: "$17B",
    fab_cost_proj_r1_yr: "2021",
    fab_cost_proj_r1_src:
      "dmc-education.com (official breakdown); actual regional spend including R&D and Austin ~$37B",
    fab_cost_proj_r2_name: "TSMC Kumamoto Fab 1 (JASM)",
    fab_cost_proj_r2_node: "22/28nm, 12/16nm",
    fab_cost_proj_r2_cap: "55k",
    fab_cost_proj_r2_inv: "$8.6B",
    fab_cost_proj_r2_yr: "2021",
    fab_cost_proj_r2_src:
      "semiwiki.com; trendforce.com (incl. $3.2B Japanese subsidy)",
    fab_cost_proj_r3_name: "TSMC Kumamoto, both fabs",
    fab_cost_proj_r3_node: "40/22/28/12/16/6/7nm; Fab 2 moving to 3nm",
    fab_cost_proj_r3_cap: ">100k combined; Fab 2 15k @3nm",
    fab_cost_proj_r3_inv: ">$20B",
    fab_cost_proj_r3_yr: "2024",
    fab_cost_proj_r3_src:
      'ejinsight.com; datacenterdynamics.com; Fab 2\'s "$17B" is a local-media figure',
    fab_cost_proj_r4_name: "TSMC Arizona (all phases)",
    fab_cost_proj_r4_node: "Phase 1 4nm, Phase 2 3nm, Phase 3 1.6/2nm",
    fab_cost_proj_r4_cap: "Phase 1 10k → planned 30k; Phases 2–3 not disclosed",
    fab_cost_proj_r4_inv:
      "$12B → $40B → $65B → $165B → $265B (successive increases)",
    fab_cost_proj_r4_yr: "2020 / 2022 / 2024 / Mar 2025 / Jul 2026",
    fab_cost_proj_r4_src:
      'en.wikipedia.org/wiki/TSMC_Arizona; the $265B figure and "600k capacity by 2030" come from earnings-call reporting and low-quality aggregators',
    fab_cost_proj_r5_name: "Intel Ohio One (two fabs)",
    fab_cost_proj_r5_node: "Advanced logic (node not disclosed)",
    fab_cost_proj_r5_cap: "Not disclosed",
    fab_cost_proj_r5_inv: "$20B → $28B",
    fab_cost_proj_r5_yr: "2022; raised Mar 2024",
    fab_cost_proj_r5_src: "sdxcentral.com (2025); ~$5–7B spent so far",
    fab_cost_proj_r6_name: "SK hynix Yongin Y2",
    fab_cost_proj_r6_node: "Advanced DRAM / HBM",
    fab_cost_proj_r6_cap: "360k (full, 6 phases × 60k)",
    fab_cost_proj_r6_inv: "₩35.2T ≈ $24.8B",
    fab_cost_proj_r6_yr: "Aug 2026 (board approval)",
    fab_cost_proj_r6_src: "fool.com; siliconangle.com; techtimes.com",
    fab_cost_proj_r7_name: "SK hynix Cheongju M17",
    fab_cost_proj_r7_node: "NAND",
    fab_cost_proj_r7_cap: "Not disclosed",
    fab_cost_proj_r7_inv: "₩19.1T ≈ $13.5B",
    fab_cost_proj_r7_yr: "2026",
    fab_cost_proj_r7_src: "fool.com",
    fab_cost_proj_r8_name: "Micron Boise (two DRAM fabs)",
    fab_cost_proj_r8_node: "Advanced DRAM",
    fab_cost_proj_r8_cap: "Not disclosed",
    fab_cost_proj_r8_inv: "$50B (~$25B each)",
    fab_cost_proj_r8_yr: "2022–2026",
    fab_cost_proj_r8_src: "intellectia.ai; industrialinfo.com",
    fab_cost_proj_r9_name: "Micron Hiroshima expansion",
    fab_cost_proj_r9_node: "DRAM / HBM",
    fab_cost_proj_r9_cap: "Not disclosed",
    fab_cost_proj_r9_inv: "$9.3B (¥1.5T)",
    fab_cost_proj_r9_yr: "2026",
    fab_cost_proj_r9_src: "zerohedge.com (citing Bloomberg)",
    fab_cost_proj_r10_name: "Micron Clay, New York (four DRAM fabs)",
    fab_cost_proj_r10_node: "DRAM",
    fab_cost_proj_r10_cap: "Not disclosed",
    fab_cost_proj_r10_inv: "$100B (~20 years)",
    fab_cost_proj_r10_yr: "Jan 2026 (groundbreaking)",
    fab_cost_proj_r10_src: "techtimes.com",

    // Flags
    fab_cost_flag_weak: "Weak source",
    fab_cost_flag_ibs_high: "IBS figures considered high by practitioners",
    fab_cost_flag_unconfirmed_tsmc: "Not confirmed by TSMC",
    fab_cost_flag_treat_caution: "Treat with caution",

    // Capacity Scaling + OSAT
    fab_cost_scale_title: "Capacity Scaling and Back-End (OSAT)",
    fab_cost_scale_left_h: "Capacity: equipment linear, facilities sub-linear",
    fab_cost_scale_l1:
      "<strong>Equipment</strong> scales roughly in proportion to wafer starts at a given node (double the capacity ≈ double the equipment), so the 70–80% equipment share broadly holds across fab sizes.",
    fab_cost_scale_l2:
      "<strong>Facilities</strong> show real but limited economies of scale: a UPW plant, ASU, substation, and CUB do not double with WSPM. Indirect evidence: Kumamoto Fab 1 at $156M per 1k WSPM, versus the unconfirmed Fab 2 at ~$1.1B/1k — small fabs carry far higher unit facility costs.",
    fab_cost_scale_l3:
      "<strong>A phase-2 fab on the same campus</strong> is significantly cheaper: shared power, water, logistics, permits, and talent pool (GF Malta case; both Kumamoto Fab 2 and Samsung Taylor Fab 2 sit on existing campuses).",
    fab_cost_scale_l4:
      "Part of the driver of giant fabs has nothing to do with cost: utilization headroom, fewer managers, faster yield learning, fewer financing rounds (chiphistory.org).",
    fab_cost_scale_l5:
      "Modeling suggestion: total cost = campus fixed items (land, substation, UPW, CUB — sub-linear) + cleanroom / facility items linear in WSPM + equipment (linear). <strong>No parametric curve (e.g., cost ∝ WSPM<sup>0.x</sup>) has ever been published in public sources — this is an explicit data gap.</strong>",
    fab_cost_scale_right_h: "OSAT / back-end packaging & test plants",
    fab_cost_scale_r1:
      "Reference anchor: Amkor's Arizona advanced packaging campus grew from a $2B plan to <strong>$7B</strong> (before the first building produced; broke ground 2025, production early 2028), covering advanced packaging + test, not traditional packaging alone (3dincites.com, Oct 2026).",
    fab_cost_scale_r2:
      "Cost drivers: high-end testers cost several million dollars each (wevolver.com); fine-pitch RDL lithography and precision bonding are the other two major capital items. 2025 bonding equipment market structure: wire bonding 38.5% ($3.54B), die bonding 31.2% (dataintelo).",
    fab_cost_scale_r3:
      "Equipment share is higher than in front-end fabs: ASE's 2025 ATM revenue mix was packaging 81%, test 18.5% (dataintelo), and test is precisely the capital-intensive bottleneck.",
    fab_cost_scale_r4:
      "Scale reference: Taiwan test house Sigurd raised 2025 capex to NT$8.8B (~$270M) for test capacity expansion, including a new plant (asiadaily.org).",
    fab_cost_scale_r5:
      'Model magnitudes: traditional packaging/test plant $0.5–2B; advanced packaging (CoWoS / fan-out) campus $2–7B. <strong>"Equipment ≈ 60–75% of OSAT capex" is an estimate backed out from cost drivers, not a directly sourced figure — cite it as such.</strong> No unit-capacity cost found (e.g., dollars per million units / month).',

    // Timeline
    fab_cost_time_title: "Timeline: Time Itself Is Cost",
    fab_cost_time_note:
      'Typical durations for permitting + design → first wafer out (Blaschitz / Exyte·M+W, via TechSpot, 2025). Building a fab in the US costs 30% (Intel basis) to 4× (TSMC basis) more than in Taiwan, with a schedule roughly twice as long; a substantial part of the premium is "time-driven" — labor, extended site management costs, a ~12,000-person construction workforce (TSMC Arizona). Kumamoto Fab 1 compressed its schedule with 24/7 construction, but <strong>no public source quantifies the expediting premium (dollars per month saved) — not found</strong>.',
    fab_cost_tl_asia_num: "~20 months",
    fab_cost_tl_asia_lbl: "Asia (Taiwan basis)",
    fab_cost_tl_asia_sub: "Permitting + design → first wafer out",
    fab_cost_tl_us_num: "~38 months",
    fab_cost_tl_us_lbl: "US",
    fab_cost_tl_us_sub:
      "Permitting + design → first wafer out; groundbreaking → first wafer is typically 2.5–3+ years (2010s US average 900+ days vs. Asia 600–700 days)",
    fab_cost_tl_eu_num: "~34 months",
    fab_cost_tl_eu_lbl: "Europe",
    fab_cost_tl_eu_sub: "Permitting + design → first wafer out",
    fab_cost_time_later_h: "Later stages",
    fab_cost_time_later_1:
      "Tool install → acceptable yield: a further <strong>6–12 months</strong> of ramp (construction-physics, 2024).",
    fab_cost_time_later_2:
      "First wafer out → volume production: a further <strong>6–18 months</strong>, depending on node maturity (e.g., VSMC risk production Sep 2026 → volume production Q1 2027).",
    fab_cost_time_later_3:
      "A large fab typically needs <strong>2–5 years</strong> from groundbreaking to full capacity (e.g., SK hynix Y2 planned groundbreaking Jul 2027 → first cleanroom ready Jun 2029).",
    fab_cost_time_gap_h: "Where the regional gap actually is",
    fab_cost_time_gap_p:
      "SK hynix's schedule (groundbreaking → first cleanroom in just 23 months) shows cleanroom shell construction speeds are similar across regions; the US gap lies mainly in <strong>permitting, labor supply, and the tool-install / qualification ecosystem</strong>, not in pouring concrete. In other words, the first lever for lowering US fab costs is process and ecosystem, not building unit prices.",

    // Gaps
    fab_cost_gap_title: "Unverified / Gaps in the Public Data",
    fab_cost_gap_intro:
      "The following questions have <strong>no reliable public answer</strong> from this round of research. Any model claiming to answer them precisely should be asked for its sources.",
    fab_cost_gap_1:
      '<strong>No authoritative breakdown table (in public channels):</strong> no SEMI / McKinsey / BCG / SIA table of "equipment / building / facilities / land / other" percentages was found; this page\'s breakdown is triangulated from second-hand sources of uneven quality.',
    fab_cost_gap_2:
      "<strong>Capacity undisclosed by several makers:</strong> WSPM for Intel Ohio and Micron Boise / Hiroshima / New York is not published, so unit-capacity costs cannot be computed.",
    fab_cost_gap_3:
      "<strong>No parametric capacity curve:</strong> no published cost ∝ WSPM<sup>x</sup> curve exists — only qualitative evidence.",
    fab_cost_gap_4:
      "<strong>Standalone substation cost; standalone chemicals / wastewater cost:</strong> no standalone figures found for either — only combined bases.",
    fab_cost_gap_5:
      "<strong>OSAT unit-capacity cost</strong> (e.g., dollars per million units / month): not found.",
    fab_cost_gap_6:
      "<strong>Expediting premium</strong> (dollars per month saved): not found.",
    fab_cost_gap_7:
      "<strong>Official equipment-vs-building splits have nearly vanished:</strong> treated as company secrets; Samsung Taylor's $6B / $11B is the only official announced split.",
    fab_cost_gap_8:
      "<strong>Some 2026 news figures come from low-quality aggregators</strong> (e.g., TSMC's $265B total, Samsung's $37B regional spend): flagged in the tables above — treat with caution; the core anchors (Wikipedia, company announcements, practitioner interviews, IBS) are relatively stronger.",

    // Key Sources
    fab_cost_src_title: "Key Sources",
    fab_cost_src_1:
      "<strong>construction-physics.com — How to build a $20 billion semiconductor fab</strong>: cost structure, equipment 70–80%, MEP ≈ 2/3 of construction cost, +30% per node, timelines",
    fab_cost_src_2:
      "<strong>TechSpot — Building fabs in the US takes twice as long and costs twice as much (Blaschitz / Exyte)</strong>: facilities $4–6B / total >$20B; 20/38/34-month timelines; construction inputs",
    fab_cost_src_3: "<strong>TechSpot — IBS 2nm $28B / 50k WSPM</strong>",
    fab_cost_src_4:
      "<strong>SemiWiki forum — IBS 3nm $15–20B / 40k WSPM</strong> (incl. practitioner pushback that IBS runs high)",
    fab_cost_src_5:
      "<strong>Wikipedia — TSMC Arizona</strong>: capacity and investment by phase, CHIPS Act support",
    fab_cost_src_6:
      "<strong>dmc-education.com — Samsung Taylor $6B / $11B official split</strong>",
    fab_cost_src_7:
      "<strong>semiconductorx.com — Fab water use and UPW benchmarks</strong>",
    fab_cost_src_8:
      "<strong>emergenresearch — Veolia's $120M UPW contract for Intel</strong>",
    fab_cost_src_9_a: "<strong>SNS Insider — AMHS market report</strong>",
    fab_cost_src_9_b: "<strong>IndexBox — AMHS share basis</strong>",
    fab_cost_src_10:
      "<strong>DataCenterDynamics — TSMC power intensity (S&P basis)</strong>",
    fab_cost_src_11:
      "<strong>Deloitte — 2nm uses 3.5× the energy of 28nm</strong>",
    fab_cost_src_12:
      "<strong>openPR — Linde's $1B Phoenix gas complex</strong>",
    fab_cost_src_13_a: "<strong>dataintelo — ASU costs $50–300M</strong>",
    fab_cost_src_13_b:
      "<strong>dataintelo — OSAT market and revenue structure</strong>",
    fab_cost_src_14:
      "<strong>3DInCites — Amkor advanced packaging campus $2B → $7B</strong>",
    fab_cost_src_15_a: "<strong>SemiWiki — TSMC Kumamoto</strong>",
    fab_cost_src_15_b:
      "<strong>TrendForce — Kumamoto enters volume production</strong>",
    fab_cost_src_15_c: "<strong>DCD — Kumamoto Fab 2 to run 3nm</strong>",
    fab_cost_src_16_a:
      "<strong>Motley Fool — SK hynix approves new memory fabs</strong>",
    fab_cost_src_16_b: "<strong>TechTimes — Yongin 360k WSPM roadmap</strong>",
    fab_cost_src_17: "<strong>SDxCentral — Intel Ohio $28B</strong>",
    fab_cost_src_18: "<strong>IMARC — Mature-node fab cost breakdown</strong>",
    fab_cost_src_19:
      "<strong>civilstructures.in — Semiconductor fab construction</strong> (weak quality; cited only where no better source exists, and flagged)",

    // Footer
    fab_cost_footer:
      'All figures on this page come from the public sources listed above (researched 2026-10-18). Anything flagged "unverified / weak quality / estimate" must not be cited alone as a basis for decisions. The estimator is a rough model based on published anchors; actual project costs vary enormously by region, subsidies, exchange rates, and schedule.',

    fab_cost_split_c_notes_sub:
      "UPW, power, HVAC, gases, chemicals, wastewater",
    fab_cost_split_e_notes_sub: "engineering design, permitting, commissioning",
    fab_cost_node_r9_basis_note:
      'Small fabs have markedly higher unit facility costs — see "Capacity scaling"',
    fab_cost_fac_r1_sub: "ISO Class 1–3 ballroom",
    fab_cost_src_1_sub:
      "cost structure, equipment 70–80%, MEP ≈ 2/3 of construction cost, +30% per node, timelines",
    fab_cost_src_2_sub:
      "facilities $4–6B / total >$20B; 20/38/34-month timelines; construction inputs",
    fab_cost_src_4_sub: "(incl. practitioner pushback that IBS runs high)",
    fab_cost_src_5_sub: "capacity and investment by phase, CHIPS Act support",
    fab_cost_src_19_sub:
      "(weak quality; cited only where no better source exists, and flagged)",

    // Table Mobile Cell Labels
    fab_cost_lbl_component: "Component",
    fab_cost_lbl_share: "Share of total cost",
    fab_cost_lbl_notes: "Notes",
    fab_cost_lbl_source: "Source",
    fab_cost_lbl_node: "Node",
    fab_cost_lbl_wspm_cost: "$/1k WSPM",
    fab_cost_lbl_basis: "Basis",
    fab_cost_lbl_line_item: "Line item",
    fab_cost_lbl_price_scale: "Price / scale",
    fab_cost_lbl_project: "Project",
    fab_cost_lbl_capacity: "Capacity (WSPM)",
    fab_cost_lbl_pub_invest: "Published total investment",
    fab_cost_lbl_year_ann: "Year announced",
  },
  "zh-CN": {
    fab_cost_page_title: "Fab 建设成本：设备之外的构成 — SemiconFab.org",
    fab_cost_h1: "建一座 Fab：设备之外的钱花在哪",
    fab_cost_lede:
      '在一座先进制程 Fab 的总投资中，工艺设备占 70–80%。剩下的 20–30%——厂房、洁净室、超纯水、电力、气体、废水、AMHS、土地与工程设计——就是所谓的"建设成本"。本页把公开来源中能查到的占比、单项价格与参考项目汇总成一个按 <strong>制程节点 × 产能（WSPM）</strong> 估算成本的参数化模型，并明确标注：哪些数字来自官方来源，哪些是多源三角推算，哪些根本查不到。',
    fab_cost_meta_line:
      "来源：2026-10-18 的公开网络调研（行业媒体、从业者访谈、分析师估算与公司公告）。金额均为美元。迄今没有任何机构（SEMI / McKinsey / BCG / SIA）在公开渠道发布过完整的成本拆分表——下文的拆分是跨多个来源三角推算的结果，是这份数据里最薄弱的一环，阅读时请带着这一保留。",

    // 4 Key Stats
    fab_cost_stat1_num: "70–80%",
    fab_cost_stat1_lbl: "工艺设备占总成本的比例",
    fab_cost_stat1_src:
      "新建先进制程 Fab · construction-physics，2024；仅光刻一项就约占总成本的 20%",
    fab_cost_stat2_num: "$4–6B",
    fab_cost_stat2_lbl: "设施部分（厂房 + 洁净室 + 公用设施）",
    fab_cost_stat2_src:
      "以总投资 >$20B 的大型 Fab 计 · Exyte/M+W 从业者 Blaschitz，2025",
    fab_cost_stat3_num: "≈ 2/3",
    fab_cost_stat3_lbl: '机电与公用设施占"建设"成本的比例',
    fab_cost_stat3_src:
      "其余约 1/3 为洁净室配套与建筑结构 · construction-physics，2024",
    fab_cost_stat4_num: "$6B / $11B",
    fab_cost_stat4_lbl: "三星 Taylor 官方拆分",
    fab_cost_stat4_src:
      "$17B 总投资中：建筑 $6B（35%）/ 设备 $11B（65%）· 三星官方公告，2021 年 11 月",

    // Estimator
    fab_cost_calc_title: "参数化估算器",
    fab_cost_calc_note:
      '方法：总投资 = 每 1k WSPM 成本（制程锚点）× 产能；非设备建设成本 = 总投资 × 设施占比。所有锚点均取自下文"制程缩放"表中的已发表数字，设施占比采用报告给出的 20–30% 区间（上限可放宽至三星 Taylor 官方的 35% 建筑占比）。这是粗估模型，不是报价。',
    fab_cost_calc_lbl_node: "制程锚点（总成本口径，含设备）",
    fab_cost_opt_mature28:
      "28nm 级成熟制程 — $156M / 1k WSPM（熊本一厂实际值）",
    fab_cost_opt_node3: "3nm — $375–500M / 1k WSPM（IBS）",
    fab_cost_opt_node2samsung: "2nm — $340M / 1k WSPM（三星 Taylor 公布数字）",
    fab_cost_opt_node2ibs: "2nm — $560M / 1k WSPM（IBS）",
    fab_cost_opt_node5early:
      "5nm 早期 — $600M / 1k WSPM（TSMC 亚利桑那 2020 年公告口径）",
    fab_cost_opt_dram: "先进 DRAM — $69M / 1k WSPM（SK hynix 龙仁 Y2）",
    fab_cost_calc_node_hint:
      "报告没有给出 7nm 的每 1k WSPM 成本锚点，因此不提供 7nm 选项——不要用插值伪造数据。IBS 的数字被 SemiWiki 从业者认为偏高；同一 2nm 节点另有三星公布的 $340M 数字，两者并列供对比。",
    fab_cost_calc_lbl_wspm: "产能，WSPM（每月晶圆投片量）",
    fab_cost_calc_wspm_hint:
      "锚点项目的实际规模：熊本一厂 55k，IBS 的 2nm 模型 50k，龙仁 Y2 满产达 360k（分六期建设）。",
    fab_cost_calc_lbl_share: "设施（非设备）占总投资的比例",
    fab_cost_calc_share_lo: "20%（报告区间下限）",
    fab_cost_calc_share_hi: "35%（三星官方建筑占比）",
    fab_cost_calc_share_hint:
      "20–30% 是大型先进制程 Fab 的报告区间（设施 $4–6B / 总投资 >$20B）；35% 对应三星 Taylor 官方的建筑占比。成熟制程的设备占比更低（IMARC 对印度一座成熟制程 Fab 的拆分中设备仅占 45%），设施占比会相应更高——本滑杆的上限不覆盖这种情况，相关结果请另行判断。",
    fab_cost_calc_lbl_region: "建设地区（仅影响工期显示）",
    fab_cost_calc_reg_asia: "亚洲",
    fab_cost_calc_reg_us: "美国",
    fab_cost_calc_reg_eu: "欧洲",
    fab_cost_calc_reg_hint:
      "工期口径：许可 + 设计 → 首片晶圆出片（Blaschitz，2025）。报告没有给出可信的地区成本乘数，因此地区不进入成本计算；目前只知道美国建 Fab 比台湾贵 30%（Intel 口径）到 4 倍（TSMC 口径），且溢价的很大一部分来自工期本身更长。",

    // Estimator Results
    fab_cost_res_build_lbl: "非设备建设成本估算（厂房 + 洁净室 + 公用设施等）",
    fab_cost_res_build_sub_tmpl: "总投资 × {share}% 设施占比",
    fab_cost_res_total_lbl: "总投资（含设备）",
    fab_cost_res_equip_lbl: "其中：工艺设备",
    fab_cost_res_equip_sub: "总投资减去建设成本",
    fab_cost_res_services_lbl: "建设成本内：机电与公用设施服务",
    fab_cost_res_services_sub:
      "≈ 建设成本的 2/3：暖通、超纯水、电力、排气、气体与化学品系统等（construction-physics）",
    fab_cost_res_shell_lbl: "建设成本内：洁净室配套与建筑结构",
    fab_cost_res_shell_sub: "≈ 建设成本的 1/3（construction-physics）",
    fab_cost_res_amhs_lbl: "其中：AMHS（天车搬运 / 储片系统），量级估算",
    fab_cost_res_amhs_sub:
      "建设成本的 5–10%（市场研究口径，2025–26）；另一口径为设备投资的 3–5%",
    fab_cost_res_time_lbl: "参考工期：许可 + 设计 → 首片出片",
    fab_cost_legend_equip: "工艺设备",
    fab_cost_legend_services: "机电与公用设施",
    fab_cost_legend_shell: "洁净室配套与建筑结构",
    fab_cost_calc_foot:
      "模型局限（来自报告）：① 公开来源中不存在参数化的产能曲线（成本 ∝ WSPM<sup>x</sup>）；本模型按产能线性外推总成本——但设施部分实际上是次线性缩放的（UPW 厂、变电站、CUB 不会随产能翻倍），因此小 Fab 的设施占比会被低估、大 Fab 会被高估；同园区二期 Fab 共享基础设施，成本显著更低。② 土地（约 3–5%，$20M–200M，100–500 英亩；来源质量弱）与工程 / 许可 / 调试验收（约 3–8%）未单列，包含在设施占比的不确定区间内。③ 每代制程约 +30% 的经验法则（construction-physics）主要由更贵的设备和更多的掩模 / 工艺步骤驱动，落在设备一侧。",

    // Cost Breakdown Table
    fab_cost_split_title: "总成本拆分",
    fab_cost_split_note:
      '下表由多个来源拼接而成，各行的口径并不一致（有的占总项目成本，有的占建设预算）——引用任何数字时请连同备注一起看。civilstructures.in 的一张表把"制造设备"列为 35–50%，但其分项加总超过 100%，且描述的是建设 / 安装预算而非总项目成本；本页不按总成本口径采用它，仅在设施分项无更好来源时引用，并作标注。',
    fab_cost_th_component: "构成",
    fab_cost_th_share: "占总成本比例",
    fab_cost_th_notes: "备注",
    fab_cost_th_source: "来源",
    fab_cost_split_a_comp: "(a) 工艺设备",
    fab_cost_split_a_share: "70–80%",
    fab_cost_split_a_notes:
      "先进制程口径。三星 Taylor 官方公告为 65%（$11B / $17B）；IMARC 对成熟制程（印度 Fab）的拆分仅为 45%。设备占比随时间推移而上升：1980 年代中期的 DRAM 厂大致五五开，1990 年代末起设备占主导。仅光刻一项就约占总成本的 20%。",
    fab_cost_split_a_src:
      "construction-physics (2024); Samsung official announcement (Nov 2021); imarcgroup.com",
    fab_cost_split_b_comp: "(b) 厂房 + 洁净室",
    fab_cost_split_b_share: "~10–15%",
    fab_cost_split_b_notes:
      '由"设施总计 20–30%"减去公用设施部分反推的隐含值，并非直接公布的数字。三星 Taylor 的 $6B（35%）是建筑 + 场地（含洁净室）的官方数字，口径不完全可比。',
    fab_cost_split_b_src:
      "Exyte/M+W practitioner via TechSpot (2025); Samsung official (2021)",
    fab_cost_split_c_comp:
      "(c) 公用设施（UPW、电力、暖通、气体、化学品、废水）",
    fab_cost_split_c_share: "~8–15%",
    fab_cost_split_c_notes:
      '另一口径：约占建设总成本的 2/3。IMARC 的拆分中，公用设施占 8%、洁净室基础设施（暖通）占 15%（成熟制程口径）。单项价格见下文"设施分项明细"表。',
    fab_cost_split_c_src: "construction-physics (2024); imarcgroup.com",
    fab_cost_split_d_comp: "(d) 土地",
    fab_cost_split_d_share: "3–5%",
    fab_cost_split_d_notes:
      "约 $20M–200M，100–500 英亩。熊本、Boise 等案例显示土地本身占比很小；场地开发另行计入。",
    fab_cost_split_d_src: "civilstructures.in (2026)",
    fab_cost_split_e_comp: "(e) 其他（工程设计、许可、调试验收）",
    fab_cost_split_e_share: "~3–8%",
    fab_cost_split_e_notes:
      "civilstructures 口径：设计 5–10%、测试 / 调试 3%；IMARC 口径：IT / 安防 / 合规 5%。这是最弱的一项，没有强的行业来源。",
    fab_cost_split_e_src: "civilstructures.in; imarcgroup.com",

    // Node Scaling
    fab_cost_node_title: "制程缩放：每 1k WSPM 的总成本",
    fab_cost_node_note:
      "在统一口径（总投资含设备）下，制程是第二大的变量——最大的其实是 <strong>逻辑 vs 存储</strong>：先进 DRAM 每 1k WSPM 的成本（$69M）不到成熟 28nm 逻辑（$156M）的一半。经验法则：每推进一代制程，总成本约增加 30%。",
    fab_cost_chart_aria:
      "柱状图：每 1k WSPM 总成本——DRAM 69、28nm 156、2nm 三星口径 340、3nm 区间 375 至 500、2nm IBS 口径 560、5nm 早期 600，单位为百万美元",
    fab_cost_chart_note:
      "单位：每 1k WSPM 的百万美元数。3nm 数字为 IBS 给出的区间（$15–20B @ 40k WSPM），以区间条显示；其余为单点锚点。5nm 早期数字（TSMC 亚利桑那 2020 年公告，$12B / 20k）包含首座 Fab 的溢价，不代表成熟 5nm 的水平。",
    fab_cost_th_node: "制程",
    fab_cost_th_wspm_cost: "$/1k WSPM",
    fab_cost_th_basis: "依据",
    fab_cost_node_r1_name: "先进 DRAM",
    fab_cost_node_r1_cost: "~$69M",
    fab_cost_node_r1_basis:
      "SK hynix 龙仁 Y2：$24.8B / 360k WSPM（满产，分六期）",
    fab_cost_node_r1_src: "fool.com / techtimes (2026)",
    fab_cost_node_r2_name: "28nm 级（成熟）",
    fab_cost_node_r2_cost: "~$156M",
    fab_cost_node_r2_basis:
      "TSMC 熊本一厂（22/28nm、12/16nm）：$8.6B / 55k WSPM，含日本政府 $3.2B 补贴",
    fab_cost_node_r2_src: "semiwiki / trendforce (2024–25)",
    fab_cost_node_r3_name: "28–90nm（成熟，通用）",
    fab_cost_node_r3_cost: "~$125–275M",
    fab_cost_node_r3_basis: "印度目标 Fab：每座 $5–11B",
    fab_cost_node_r3_src: "fabs.pranaykotas.com India tracker (2026)",
    fab_cost_node_r4_name: "成熟特色工艺",
    fab_cost_node_r4_cost: "~$133M",
    fab_cost_node_r4_basis:
      "GlobalFoundries Malta 一期：$10B / 约 75k WSPM（90 万片 / 年）",
    fab_cost_node_r4_src: "medium / tai-semicon (2026)",
    fab_cost_node_r5_name: "3nm",
    fab_cost_node_r5_cost: "$375–500M",
    fab_cost_node_r5_basis: "IBS：$15–20B @ 40k WSPM",
    fab_cost_node_r5_src: "IBS via semiwiki / techspot (2014/2023)",
    fab_cost_node_r6_name: "2nm（公布口径）",
    fab_cost_node_r6_cost: "~$340M",
    fab_cost_node_r6_basis:
      "三星 Taylor：$17B / 约 50k WSPM（2021 年以 5nm 名义公布，现为 2nm GAA）",
    fab_cost_node_r6_src: "dmc-education / sammyguru",
    fab_cost_node_r7_name: "2nm（IBS 口径）",
    fab_cost_node_r7_cost: "$560M",
    fab_cost_node_r7_basis: "IBS：$28B @ 50k WSPM",
    fab_cost_node_r7_src: "techspot.com (Dec 2023)",
    fab_cost_node_r8_name: "5nm（早期采用者）",
    fab_cost_node_r8_cost: "~$600M",
    fab_cost_node_r8_basis: "TSMC 亚利桑那 2020 年公告：$12B / 20k WSPM",
    fab_cost_node_r8_src: "nasdaq.com (2020)",
    fab_cost_node_r9_name: "3nm（小型 Fab）",
    fab_cost_node_r9_cost: "~$1.1B",
    fab_cost_node_r9_basis:
      '熊本二厂：$17B / 15k WSPM 小型 Fab 的单位设施成本明显更高——见"产能缩放"',
    fab_cost_node_r9_src:
      "datacenterdynamics citing Japanese local media (2026)",

    // Facility Line Items
    fab_cost_fac_title: "设施分项明细（非设备成本的核心）",
    fab_cost_fac_note:
      '以下是报告中找到的分项锚点。注意洁净室单价的跨度极大：基础装修与"可装机"状态相差 4 倍以上，EUV 光刻区还要再翻倍——不带状态条件的单价没有意义。',
    fab_cost_th_item: "分项",
    fab_cost_th_price_scale: "价格 / 规模",
    fab_cost_fac_r1_name: "洁净室（ISO Class 1–3 大开间）",
    fab_cost_fac_r1_price:
      "装修 + 硬件 $1,200–2,500/m²；可装机状态 $5,000–10,000/m²；EUV 区 $20,000+/m²；另有 ISO Class 3 口径 >$700/ft²（≈$7,500/m²）的说法",
    fab_cost_fac_r1_notes:
      "大型 Fab 的洁净室可达 50 万–100 万平方英尺；典型大型 Fab 约 43 万平方英尺、2,000 台设备（Blaschitz）",
    fab_cost_fac_r1_src:
      "civilstructures.in (2026); sst.semiconductor-digest.com; asianometry via construction-physics",
    fab_cost_fac_r2_name: "超纯水（UPW）系统",
    fab_cost_fac_r2_price:
      "先进制程、100k WSPM：$200–500M，产能 10–20 MGD，每片晶圆投片用水约 2,000–5,000 加仑，回用系统另加 $50–150M；成熟制程：$50–150M，2–8 MGD",
    fab_cost_fac_r2_notes:
      "硬锚点：Veolia 为 Intel Chandler Fab 52+62 签订的合同为 $120M，合计 6 MGD、18.2 MΩ·cm（2023 年 9 月）",
    fab_cost_fac_r2_src:
      "semiconductorx.com; emergenresearch (Veolia contract)",
    fab_cost_fac_r3_name: "电力",
    fab_cost_fac_r3_price:
      "大型先进 Fab 用电量级约 100 MW；TSMC 亚利桑那满产约 200 MW；2nm 的能耗是 28nm 的 3.5 倍",
    fab_cost_fac_r3_notes:
      "电气基础设施总计 $500M–2B（来源质量弱）；<strong>未找到独立变电站的单独成本</strong>。TSMC 每晶圆·掩模层的电力强度：2022 年 27.7 kW → 3nm 量产期 40.5 kW（S&P 口径；单位按原始来源）",
    fab_cost_fac_r3_src:
      "construction-physics (2024); sanieinstitute (2025); Deloitte; datacenterdynamics",
    fab_cost_fac_r4_name: "暖通 / 洁净室空气处理",
    fab_cost_fac_r4_price:
      '无独立单价：包含在"机电服务 ≈ 建设成本的 2/3"之内；在小型洁净室项目中暖通可占 30–50%',
    fab_cost_fac_r4_notes:
      "洁净室空气每小时循环数百次，使暖通成为设施能耗与成本的主要驱动之一",
    fab_cost_fac_r4_src: "construction-physics (2024); crestmontcapital.com",
    fab_cost_fac_r5_name: "大宗气体（N₂/O₂/Ar）",
    fab_cost_fac_r5_price:
      "现场空分装置（ASU）：大型深冷装置 $50–300M；>500 吨 / 天级 $200–350M",
    fab_cost_fac_r5_notes:
      "硬锚点：Linde 凤凰城 $1B 气体综合体（2 座新 ASU，服务另外两座 Fab，2026 年 7 月）。大型逻辑 Fab 的氮气用量约 50,000 Nm³/h",
    fab_cost_fac_r5_src:
      "dataintelo (2026); openpr (Linde announcement); construction-physics",
    fab_cost_fac_r6_name: "化学品 + 废水 / 废气处理",
    fab_cost_fac_r6_price:
      "<strong>未找到独立成本</strong>；仅有水 + 废水合计 $200M–1B 的口径（含 UPW）",
    fab_cost_fac_r6_notes: "TSMC 亚利桑那已承诺 100% 水回用（semiconductorx）",
    fab_cost_fac_r6_src: "civilstructures.in (envelope basis, weak quality)",
    fab_cost_fac_r7_name: "AMHS（天车搬运 + 储片系统）",
    fab_cost_fac_r7_price:
      "建设成本的 5–10%；或设备投资的 3–5%——即一座 $20B Fab 约 $0.2–0.8B",
    fab_cost_fac_r7_notes: "两种口径均来自市场研究机构，而非项目披露",
    fab_cost_fac_r7_src: "snsinsider.com; indexbox.io (2025–26)",
    fab_cost_fac_r8_name: "建筑物（Fab + Subfab + CUB 中央公用设施楼）",
    fab_cost_fac_r8_price:
      "设施总计 $4–6B（以总投资 >$20B 的 Fab 计，含洁净室与公用设施）；三星 Taylor 建筑 $6B / 总投资 $17B",
    fab_cost_fac_r8_notes:
      "一座大型 Fab 的建设投入量级：3,000–4,000 万工时、83,000 吨钢材、785,000 立方码混凝土（Blaschitz）",
    fab_cost_fac_r8_src:
      "Blaschitz/Exyte via TechSpot (2025); Samsung official (2021)",

    // Reference Projects
    fab_cost_proj_title: "参考项目（公布数字）",
    fab_cost_proj_note:
      '下表所有总额均为 <strong>含设备的总投资</strong>——"仅建筑"的数字几乎从不披露，三星 Taylor 的 $6B 建筑额是唯一干净的官方锚点。未披露产能的项目已如实标注，不做推断。',
    fab_cost_th_project: "项目",
    fab_cost_th_capacity: "产能（WSPM）",
    fab_cost_th_pub_invest: "公布总投资",
    fab_cost_th_year_ann: "公布年份",
    fab_cost_proj_r1_name: "三星 Taylor，得州",
    fab_cost_proj_r1_node: "2nm GAA（一厂；以 5nm 名义公布）",
    fab_cost_proj_r1_cap: "约 50k（行业报道）",
    fab_cost_proj_r1_inv: "$17B",
    fab_cost_proj_r1_yr: "2021",
    fab_cost_proj_r1_src:
      "dmc-education.com (official breakdown); actual regional spend including R&D and Austin ~$37B",
    fab_cost_proj_r2_name: "TSMC 熊本一厂（JASM）",
    fab_cost_proj_r2_node: "22/28nm、12/16nm",
    fab_cost_proj_r2_cap: "55k",
    fab_cost_proj_r2_inv: "$8.6B",
    fab_cost_proj_r2_yr: "2021",
    fab_cost_proj_r2_src:
      "semiwiki.com; trendforce.com (incl. $3.2B Japanese subsidy)",
    fab_cost_proj_r3_name: "TSMC 熊本两厂合计",
    fab_cost_proj_r3_node: "40/22/28/12/16/6/7nm；二厂转向 3nm",
    fab_cost_proj_r3_cap: "合计 >100k；二厂 15k @3nm",
    fab_cost_proj_r3_inv: ">$20B",
    fab_cost_proj_r3_yr: "2024",
    fab_cost_proj_r3_src:
      'ejinsight.com; datacenterdynamics.com; Fab 2\'s "$17B" is a local-media figure',
    fab_cost_proj_r4_name: "TSMC 亚利桑那（全部期数）",
    fab_cost_proj_r4_node: "一期 4nm，二期 3nm，三期 1.6/2nm",
    fab_cost_proj_r4_cap: "一期 10k → 计划 30k；二、三期未披露",
    fab_cost_proj_r4_inv: "$12B → $40B → $65B → $165B → $265B（历次上调）",
    fab_cost_proj_r4_yr: "2020 / 2022 / 2024 / 2025 年 3 月 / 2026 年 7 月",
    fab_cost_proj_r4_src:
      'en.wikipedia.org/wiki/TSMC_Arizona; the $265B figure and "600k capacity by 2030" come from earnings-call reporting and low-quality aggregators',
    fab_cost_proj_r5_name: "Intel 俄亥俄 One（两座 Fab）",
    fab_cost_proj_r5_node: "先进逻辑（制程未披露）",
    fab_cost_proj_r5_cap: "未披露",
    fab_cost_proj_r5_inv: "$20B → $28B",
    fab_cost_proj_r5_yr: "2022；2024 年 3 月上调",
    fab_cost_proj_r5_src: "sdxcentral.com (2025); ~$5–7B spent so far",
    fab_cost_proj_r6_name: "SK hynix 龙仁 Y2",
    fab_cost_proj_r6_node: "先进 DRAM / HBM",
    fab_cost_proj_r6_cap: "360k（满产，6 期 × 60k）",
    fab_cost_proj_r6_inv: "35.2 万亿韩元 ≈ $24.8B",
    fab_cost_proj_r6_yr: "2026 年 8 月（董事会批准）",
    fab_cost_proj_r6_src: "fool.com; siliconangle.com; techtimes.com",
    fab_cost_proj_r7_name: "SK hynix 清州 M17",
    fab_cost_proj_r7_node: "NAND",
    fab_cost_proj_r7_cap: "未披露",
    fab_cost_proj_r7_inv: "19.1 万亿韩元 ≈ $13.5B",
    fab_cost_proj_r7_yr: "2026",
    fab_cost_proj_r7_src: "fool.com",
    fab_cost_proj_r8_name: "Micron 博伊西（两座 DRAM Fab）",
    fab_cost_proj_r8_node: "先进 DRAM",
    fab_cost_proj_r8_cap: "未披露",
    fab_cost_proj_r8_inv: "$50B（每座约 $25B）",
    fab_cost_proj_r8_yr: "2022–2026",
    fab_cost_proj_r8_src: "intellectia.ai; industrialinfo.com",
    fab_cost_proj_r9_name: "Micron 广岛扩建",
    fab_cost_proj_r9_node: "DRAM / HBM",
    fab_cost_proj_r9_cap: "未披露",
    fab_cost_proj_r9_inv: "$9.3B（¥1.5T）",
    fab_cost_proj_r9_yr: "2026",
    fab_cost_proj_r9_src: "zerohedge.com (citing Bloomberg)",
    fab_cost_proj_r10_name: "Micron 纽约州 Clay（四座 DRAM Fab）",
    fab_cost_proj_r10_node: "DRAM",
    fab_cost_proj_r10_cap: "未披露",
    fab_cost_proj_r10_inv: "$100B（约 20 年）",
    fab_cost_proj_r10_yr: "2026 年 1 月（动工）",
    fab_cost_proj_r10_src: "techtimes.com",

    // Flags
    fab_cost_flag_weak: "来源较弱",
    fab_cost_flag_ibs_high: "IBS 数字被从业者认为偏高",
    fab_cost_flag_unconfirmed_tsmc: "未经 TSMC 证实",
    fab_cost_flag_treat_caution: "请谨慎看待",

    // Capacity Scaling + OSAT
    fab_cost_scale_title: "产能缩放与后端（OSAT）",
    fab_cost_scale_left_h: "产能：设备线性，设施次线性",
    fab_cost_scale_l1:
      "<strong>设备</strong>在给定制程下与晶圆投片量近似成正比（产能翻倍 ≈ 设备翻倍），因此 70–80% 的设备占比在不同 Fab 规模下大体成立。",
    fab_cost_scale_l2:
      "<strong>设施</strong>存在真实但有限的规模效应：UPW 厂、空分装置、变电站与 CUB 不会随 WSPM 翻倍。间接证据：熊本一厂每 1k WSPM $156M，而未经证实的二厂约 $1.1B/1k——小型 Fab 的单位设施成本高得多。",
    fab_cost_scale_l3:
      "<strong>同园区二期 Fab</strong> 显著更便宜：共享电力、水、物流、许可与人才（GF Malta 案例；熊本二厂与三星 Taylor 二厂都在既有园区内）。",
    fab_cost_scale_l4:
      "巨型 Fab 的部分动因与成本无关：产能利用率余量、更少的管理者、更快的良率学习、更少的融资轮次（chiphistory.org）。",
    fab_cost_scale_l5:
      "建模建议：总成本 = 园区固定项（土地、变电站、UPW、CUB——次线性）+ 随 WSPM 线性的洁净室 / 设施项 + 设备（线性）。<strong>公开来源中从未发表过参数化曲线（如成本 ∝ WSPM<sup>0.x</sup>）——这是一个明确的数据缺口。</strong>",
    fab_cost_scale_right_h: "OSAT / 后端封测厂",
    fab_cost_scale_r1:
      "参考锚点：Amkor 亚利桑那先进封装园区从 $2B 的计划涨到 <strong>$7B</strong>（第一栋厂房投产之前；2025 年动工，2028 年初量产），涵盖先进封装 + 测试，而非仅传统封装（3dincites.com，2026 年 10 月）。",
    fab_cost_scale_r2:
      "成本驱动：高端测试机单台数百万美元（wevolver.com）；细间距 RDL 光刻与精密键合是另外两大资本项。2025 年键合设备市场结构：引线键合 38.5%（$3.54B），芯片键合 31.2%（dataintelo）。",
    fab_cost_scale_r3:
      "设备占比比前端 Fab 更高：ASE 2025 年 ATM 收入构成为封装 81%、测试 18.5%（dataintelo），而测试正是资本密集的瓶颈。",
    fab_cost_scale_r4:
      "规模参考：台湾测试厂 Sigurd 将 2025 年资本开支上调至 88 亿新台币（约 $270M）用于测试产能扩张，含一座新厂（asiadaily.org）。",
    fab_cost_scale_r5:
      '模型量级：传统封测厂 $0.5–2B；先进封装（CoWoS / 扇出型）园区 $2–7B。<strong>"设备 ≈ OSAT 资本开支的 60–75%"是由成本驱动反推的估计，并非直接来源的数字——引用时请如此标注。</strong>未找到单位产能成本（如每百万颗 / 月的美元数）。',

    // Timeline
    fab_cost_time_title: "工期：时间本身就是成本",
    fab_cost_time_note:
      '许可 + 设计 → 首片出片的典型时长（Blaschitz / Exyte·M+W，经 TechSpot，2025）。美国建 Fab 比台湾贵 30%（Intel 口径）到 4 倍（TSMC 口径），工期约为两倍；溢价的相当一部分是"时间驱动"的——人工、延长的现场管理成本、约 12,000 人的工地 workforce（TSMC 亚利桑那）。熊本一厂以 24/7 施工压缩了工期，但 <strong>没有任何公开来源量化赶工溢价（每提前一个月的美元数）——未找到</strong>。',
    fab_cost_tl_asia_num: "约 20 个月",
    fab_cost_tl_asia_lbl: "亚洲（台湾口径）",
    fab_cost_tl_asia_sub: "许可 + 设计 → 首片出片",
    fab_cost_tl_us_num: "约 38 个月",
    fab_cost_tl_us_lbl: "美国",
    fab_cost_tl_us_sub:
      "许可 + 设计 → 首片出片；动工 → 首片出片通常 2.5–3+ 年（2010 年代美国平均 900+ 天 vs 亚洲 600–700 天）",
    fab_cost_tl_eu_num: "约 34 个月",
    fab_cost_tl_eu_lbl: "欧洲",
    fab_cost_tl_eu_sub: "许可 + 设计 → 首片出片",
    fab_cost_time_later_h: "后续阶段",
    fab_cost_time_later_1:
      "设备安装 → 达到可接受良率：再需 <strong>6–12 个月</strong> 的爬坡（construction-physics，2024）。",
    fab_cost_time_later_2:
      "首片出片 → 量产：再需 <strong>6–18 个月</strong>，取决于制程成熟度（如 VSMC 2026 年 9 月风险试产 → 2027 年一季度量产）。",
    fab_cost_time_later_3:
      "大型 Fab 从动工到满产通常需 <strong>2–5 年</strong>（如 SK hynix Y2 计划 2027 年 7 月动工 → 2029 年 6 月首间洁净室就绪）。",
    fab_cost_time_gap_h: "地区差距到底在哪里",
    fab_cost_time_gap_p:
      "SK hynix 的工期（动工 → 首间洁净室仅 23 个月）表明洁净室壳体的建设速度在各地区相近；美国的差距主要在 <strong>许可、用工供给，以及设备安装 / 认证的生态系统</strong>，而不是浇混凝土。换言之，降低美国 Fab 成本的第一个杠杆是流程与生态，而非建筑单价。",

    // Gaps
    fab_cost_gap_title: "未证实 / 公开数据的缺口",
    fab_cost_gap_intro:
      "以下问题在本轮调研中 <strong>没有可靠的公开答案</strong>。任何声称能精确回答这些问题的模型，都应被追问其来源。",
    fab_cost_gap_1:
      '<strong>不存在权威拆分表（公开渠道）：</strong>未找到 SEMI / McKinsey / BCG / SIA 公布的"设备 / 建筑 / 设施 / 土地 / 其他"百分比表；本页的拆分由质量不一的二手来源三角推算。',
    fab_cost_gap_2:
      "<strong>多家厂商未披露产能：</strong>Intel 俄亥俄与 Micron 博伊西 / 广岛 / 纽约的 WSPM 未公布，单位产能成本无法计算。",
    fab_cost_gap_3:
      "<strong>无参数化产能曲线：</strong>不存在已发表的成本 ∝ WSPM<sup>x</sup> 曲线——只有定性证据。",
    fab_cost_gap_4:
      "<strong>独立变电站成本；独立化学品 / 废水成本：</strong>均未找到独立数字——只有合并的口径。",
    fab_cost_gap_5:
      "<strong>OSAT 单位产能成本</strong>（如每百万颗 / 月的美元数）：未找到。",
    fab_cost_gap_6:
      "<strong>赶工溢价</strong>（每提前一个月的美元数）：未找到。",
    fab_cost_gap_7:
      "<strong>官方的设备 vs 建筑拆分几近绝迹：</strong>被视为公司机密；三星 Taylor 的 $6B / $11B 是唯一的官方公告拆分。",
    fab_cost_gap_8:
      "<strong>部分 2026 年新闻数字来自低质量聚合站</strong>（如 TSMC 的 $265B 总额、三星的 $37B 地区总支出）：已在上表中标注——请谨慎看待；核心锚点（Wikipedia、公司公告、从业者访谈、IBS）相对更强。",

    // Key Sources
    fab_cost_src_title: "主要来源",
    fab_cost_src_1:
      "<strong>construction-physics.com — 如何建造一座 $20B 的半导体 Fab</strong>：成本结构、设备 70–80%、机电 ≈ 建设成本的 2/3、每代 +30%、工期",
    fab_cost_src_2:
      "<strong>TechSpot — 在美国建 Fab 时间翻倍、成本翻倍（Blaschitz / Exyte）</strong>：设施 $4–6B / 总投资 >$20B；20/38/34 个月工期；建设投入",
    fab_cost_src_3: "<strong>TechSpot — IBS 2nm $28B / 50k WSPM</strong>",
    fab_cost_src_4:
      "<strong>SemiWiki 论坛 — IBS 3nm $15–20B / 40k WSPM</strong>（含从业者对 IBS 偏高的质疑）",
    fab_cost_src_5:
      "<strong>Wikipedia — TSMC 亚利桑那</strong>：各期产能与投资、CHIPS 法案支持",
    fab_cost_src_6:
      "<strong>dmc-education.com — 三星 Taylor $6B / $11B 官方拆分</strong>",
    fab_cost_src_7: "<strong>semiconductorx.com — Fab 用水与 UPW 基准</strong>",
    fab_cost_src_8:
      "<strong>emergenresearch — Veolia 为 Intel 签订的 $120M UPW 合同</strong>",
    fab_cost_src_9_a: "<strong>SNS Insider — AMHS 市场报告</strong>",
    fab_cost_src_9_b: "<strong>IndexBox — AMHS 占比口径</strong>",
    fab_cost_src_10:
      "<strong>DataCenterDynamics — TSMC 电力强度（S&P 口径）</strong>",
    fab_cost_src_11: "<strong>Deloitte — 2nm 能耗是 28nm 的 3.5 倍</strong>",
    fab_cost_src_12: "<strong>openPR — Linde 凤凰城 $1B 气体综合体</strong>",
    fab_cost_src_13_a: "<strong>dataintelo — 空分装置成本 $50–300M</strong>",
    fab_cost_src_13_b: "<strong>dataintelo — OSAT 市场与收入结构</strong>",
    fab_cost_src_14:
      "<strong>3DInCites — Amkor 先进封装园区 $2B → $7B</strong>",
    fab_cost_src_15_a: "<strong>SemiWiki — TSMC 熊本</strong>",
    fab_cost_src_15_b: "<strong>TrendForce — 熊本进入量产</strong>",
    fab_cost_src_15_c: "<strong>DCD — 熊本二厂将运行 3nm</strong>",
    fab_cost_src_16_a: "<strong>Motley Fool — SK hynix 批准新存储 Fab</strong>",
    fab_cost_src_16_b: "<strong>TechTimes — 龙仁 360k WSPM 路线图</strong>",
    fab_cost_src_17: "<strong>SDxCentral — Intel 俄亥俄 $28B</strong>",
    fab_cost_src_18: "<strong>IMARC — 成熟制程 Fab 成本拆分</strong>",
    fab_cost_src_19:
      "<strong>civilstructures.in — 半导体 Fab 建设</strong>（质量弱；仅在无更好来源处引用，并已标注）",

    // Footer
    fab_cost_footer:
      '本页所有数字均来自上列公开来源（调研于 2026-10-18）。凡标注"未证实 / 质量弱 / 估计"者，不应单独作为决策依据引用。估算器是基于已发表锚点的粗略模型；实际项目成本因地区、补贴、汇率与工期差异巨大。',

    fab_cost_split_c_notes_sub: "UPW、电力、暖通、气体、化学品、废水",
    fab_cost_split_e_notes_sub: "工程设计、许可、调试验收",
    fab_cost_node_r9_basis_note:
      '小型 Fab 的单位设施成本明显更高——见"产能缩放"',
    fab_cost_fac_r1_sub: "ISO Class 1–3 大开间",
    fab_cost_src_1_sub:
      "成本结构、设备 70–80%、机电 ≈ 建设成本的 2/3、每代 +30%、工期",
    fab_cost_src_2_sub:
      "设施 $4–6B / 总投资 >$20B；20/38/34 个月工期；建设投入",
    fab_cost_src_4_sub: "（含从业者对 IBS 偏高的质疑）",
    fab_cost_src_5_sub: "各期产能与投资、CHIPS 法案支持",
    fab_cost_src_19_sub: "（质量弱；仅在无更好来源处引用，并已标注）",

    // Table Mobile Cell Labels
    fab_cost_lbl_component: "构成",
    fab_cost_lbl_share: "占总成本比例",
    fab_cost_lbl_notes: "备注",
    fab_cost_lbl_source: "来源",
    fab_cost_lbl_node: "制程",
    fab_cost_lbl_wspm_cost: "$/1k WSPM",
    fab_cost_lbl_basis: "依据",
    fab_cost_lbl_line_item: "分项",
    fab_cost_lbl_price_scale: "价格 / 规模",
    fab_cost_lbl_project: "项目",
    fab_cost_lbl_capacity: "产能（WSPM）",
    fab_cost_lbl_pub_invest: "公布总投资",
    fab_cost_lbl_year_ann: "公布年份",
  },
};

// Automatically merge FAB_COST_I18N into global or window I18N_DICTIONARY
(function mergeTranslations() {
  const target =
    typeof I18N_DICTIONARY !== "undefined"
      ? I18N_DICTIONARY
      : typeof window !== "undefined" && window.I18N_DICTIONARY
        ? window.I18N_DICTIONARY
        : null;
  if (target) {
    Object.keys(FAB_COST_I18N).forEach((lang) => {
      if (!target[lang]) target[lang] = {};
      Object.assign(target[lang], FAB_COST_I18N[lang]);
    });
  }
  if (typeof window !== "undefined") {
    window.FAB_COST_I18N = FAB_COST_I18N;
  }
})();
