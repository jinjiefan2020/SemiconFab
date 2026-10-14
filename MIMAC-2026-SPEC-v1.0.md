# MIMAC-2026: A Citable, Open Benchmark Testbed for 300mm Wafer Fab Scheduling, AMHS Routing, and Predictive Maintenance

**Version**: 1.0-Release  
**Date**: October 2026  
**Status**: Benchmark Specification & Technical Report  
**Working Group**: SemiconFab Benchmarking Consortium

---

## 1. Abstract

We present **MIMAC-2026**, an open, structurally realistic, and citable benchmark testbed for semiconductor manufacturing operations research and reinforcement learning. Three decades after the original Measurement and Improvement of Manufacturing Capacities (MIMAC) dataset established foundational testbeds for wafer fab scheduling, modern 300mm fabrication facilities face fundamentally different operational realities: fully automated material handling systems (AMHS), re-entrant product flows exceeding 100 process steps, strict SEMI E10 equipment reliability states, and sequence-dependent tool configurations. MIMAC-2026 defines a complete, multi-product 300mm logic fab comprising 18 tool groups and 217 parallel machines, driven by Poisson lot arrivals calibrated to operate the photolithography bottleneck at exactly 91.23% utilization. The benchmark formalizes three core operational tasks: dynamic lot dispatching (T1), overhead hoist transport (OHT) routing (T2), and opportunistic preventive maintenance scheduling (T3). Unlike legacy static datasets, MIMAC-2026 provides a standard Gymnasium-compatible Python API, rigorous statistical evaluation protocols, precise baseline implementations (FIFO, SPT, EDD, CR), and a streaming event architecture designed for real-time cleanroom digital twin visualization.

---

## 2. Fab Testbed Definition

### 2.1 Facility Overview & Scope

MIMAC-2026 models an advanced 300mm front-end-of-line (FEOL) and back-end-of-line (BEOL) logic manufacturing facility. The fab operates continuously (24 hours/day, 7 days/week, 365 days/year). Wafers move exclusively in Standard Mechanical Interface (SMIF) / Front Opening Unified Pods (FOUPs) of **25 wafers per lot**.

The facility contains **18 tool groups** with a total of **217 production machines**.

### 2.2 Tool Group Specifications

Table 1 details the machine counts, equipment classification, capacity limits, availability parameters, and setup matrices across all 18 tool groups.

#### Table 1: MIMAC-2026 Tool Group Master Table

| Tool Group ID     | Equipment Name                  | Machine Count ($N_g$) | Tool Class | Batch Size ($B_{\min}, B_{\max}$) | Availability ($A_g$) | MTBF (h) | MTTR (h) | Setup Family Structure                                      |
| ----------------- | ------------------------------- | :-------------------: | :--------: | :-------------------------------: | :------------------: | :------: | :------: | ----------------------------------------------------------- |
| `TG01_LITHO`      | Immersion ArF / DUV Scanner     |          38           |  `serial`  |               1, 1                |        0.900         |   90.0   |   10.0   | Reticle Family (4 families; 15 min setup across families)   |
| `TG02_TRACK`      | Track Coater & Developer        |          35           |  `serial`  |               1, 1                |        0.920         |   92.0   |   8.0    | None (coupled to litho inline)                              |
| `TG03_ETCH`       | High-Density Plasma Dry Etcher  |          30           |  `serial`  |               1, 1                |        0.910         |   91.0   |   9.0    | Chemistry Type (Fluorine / Chlorine; 20 min setup)          |
| `TG04_STRIP`      | Plasma Resist Strip & Ashing    |           9           |  `serial`  |               1, 1                |        0.940         |  141.0   |   9.0    | None                                                        |
| `TG05_CVD`        | Dielectric PECVD & ALD          |          20           |  `serial`  |               1, 1                |        0.910         |   91.0   |   9.0    | Film Type (Oxide / Nitride / Low-k; 30 min clean setup)     |
| `TG06_PVD`        | Metal Sputter PVD System        |           9           |  `serial`  |               1, 1                |        0.920         |  115.0   |   10.0   | Target Material (Cu / Ta / TiN; 25 min clean setup)         |
| `TG07_FURN_DIFF`  | Atmospheric Diffusion Furnace   |           9           |  `batch`   |               2, 4                |        0.920         |  115.0   |   10.0   | Thermal Profile (Drive-in / Oxidation; incompatible recipe) |
| `TG08_FURN_LPCVD` | Low-Pressure CVD Furnace        |           7           |  `batch`   |               2, 4                |        0.920         |  115.0   |   10.0   | Tube Gas Family (Poly-Si / Si3N4; incompatible recipe)      |
| `TG09_IMPL_MED`   | Medium-Current Ion Implanter    |           7           |  `serial`  |               1, 1                |        0.900         |   90.0   |   10.0   | Dopant Species (B / P / As; 30 min source change)           |
| `TG10_IMPL_HIGH`  | High-Current Ion Implanter      |           7           |  `serial`  |               1, 1                |        0.900         |   90.0   |   10.0   | Dopant Species (B / P / As; 35 min source change)           |
| `TG11_CMP_OX`     | Dielectric ILD/STI CMP Polisher |           7           |  `serial`  |               1, 1                |        0.930         |  133.0   |   10.0   | Pad & Slurry Type (Silica / Ceria; 15 min conditioning)     |
| `TG12_CMP_MET`    | Metal (W / Cu) CMP Polisher     |           7           |  `serial`  |               1, 1                |        0.930         |  133.0   |   10.0   | Metal Slurry Type (W slurry / Cu barrier; 20 min flush)     |
| `TG13_WET_BENCH`  | Automated Wet Chemical Bench    |           5           |  `batch`   |               2, 4                |        0.940         |  156.7   |   10.0   | Chemical Bath (RCA-1 / RCA-2 / DHF; incompatible)           |
| `TG14_WET_SINGLE` | Single-Wafer Clean & Dry        |           7           |  `serial`  |               1, 1                |        0.940         |  156.7   |   10.0   | None                                                        |
| `TG15_RTP`        | Rapid Thermal Processing (RTP)  |           5           |  `serial`  |               1, 1                |        0.930         |  133.0   |   10.0   | Temperature Window (Spike / Soak; 10 min recipe tune)       |
| `TG16_MET_CD`     | CD-SEM & Overlay Metrology      |           6           |  `serial`  |               1, 1                |        0.950         |  190.0   |   10.0   | Recipe alignment (5 min)                                    |
| `TG17_MET_THICK`  | Spectroscopic Ellipsometer      |           4           |  `serial`  |               1, 1                |        0.950         |  190.0   |   10.0   | Film optical model (5 min)                                  |
| `TG18_INSPECT`    | Darkfield Optical Defect Tool   |           5           |  `serial`  |               1, 1                |        0.950         |  190.0   |   10.0   | Inspection threshold profile (5 min)                        |
| **Total**         | —                               |        **217**        |     —      |                 —                 |          —           |    —     |    —     | —                                                           |

### 2.3 Product Portfolio & Product Mix

The fab concurrently manufactures three distinct integrated circuit products:

1. **Product A (Logic-HighVolume)**: High-performance computing microprocessor.
   - Product Mix: $P_A = 60\%$ of total starts.
   - Route Length: **120 process steps**.
   - Lithography Visits: **28 visits** (re-entrant factor = 28).
2. **Product B (Logic-MediumVolume)**: Mobile system-on-chip (SoC).
   - Product Mix: $P_B = 30\%$ of total starts.
   - Route Length: **104 process steps**.
   - Lithography Visits: **24 visits** (re-entrant factor = 24).
3. **Product C (Logic-LowVolume / Embedded Derivative)**: Mixed-signal / automotive microcontroller.
   - Product Mix: $P_C = 10\%$ of total starts.
   - Route Length: **92 process steps**.
   - Lithography Visits: **20 visits** (re-entrant factor = 20).

### 2.4 Operation Sequence & Re-Entrant Process Routes

All product routes exhibit severe re-entrancy, visiting `TG01_LITHO`, `TG03_ETCH`, and `TG05_CVD` repeatedly across multiple metal and interconnect layers.

#### Table 2: Route Operation Summary by Tool Group

| Tool Group ID      | Product A Visits (120 ops) | Product B Visits (104 ops) | Product C Visits (92 ops) |     Weighted Visits per Lot ($\bar{V}_g$)     | Nominal Step Time $\bar{t}_g$ (h) |
| ------------------ | :------------------------: | :------------------------: | :-----------------------: | :-------------------------------------------: | :-------------------------------: |
| `TG01_LITHO`       |             28             |             24             |            20             | $0.6(28) + 0.3(24) + 0.1(20) = \mathbf{26.0}$ |         0.50 h (30.0 min)         |
| `TG02_TRACK`       |             28             |             24             |            20             | $0.6(28) + 0.3(24) + 0.1(20) = \mathbf{26.0}$ |         0.44 h (26.4 min)         |
| `TG03_ETCH`        |             16             |             14             |            12             | $0.6(16) + 0.3(14) + 0.1(12) = \mathbf{15.0}$ |         0.62 h (37.2 min)         |
| `TG04_STRIP`       |             6              |             5              |             5             |   $0.6(6) + 0.3(5) + 0.1(5) = \mathbf{5.6}$   |         0.35 h (21.0 min)         |
| `TG05_CVD`         |             8              |             7              |             7             |   $0.6(8) + 0.3(7) + 0.1(7) = \mathbf{7.6}$   |         0.72 h (43.2 min)         |
| `TG06_PVD`         |             4              |             3              |             3             |   $0.6(4) + 0.3(3) + 0.1(3) = \mathbf{3.6}$   |         0.55 h (33.0 min)         |
| `TG07_FURN_DIFF`   |             2              |             2              |             2             |   $0.6(2) + 0.3(2) + 0.1(2) = \mathbf{2.0}$   |        3.20 h (batch of 3)        |
| `TG08_FURN_LPCVD`  |             2              |             2              |             2             |   $0.6(2) + 0.3(2) + 0.1(2) = \mathbf{2.0}$   |        2.80 h (batch of 3)        |
| `TG09_IMPL_MED`    |             3              |             2              |             2             |   $0.6(3) + 0.3(2) + 0.1(2) = \mathbf{2.6}$   |         0.60 h (36.0 min)         |
| `TG10_IMPL_HIGH`   |             2              |             2              |             2             |   $0.6(2) + 0.3(2) + 0.1(2) = \mathbf{2.0}$   |         0.75 h (45.0 min)         |
| `TG11_CMP_OX`      |             3              |             3              |             2             |   $0.6(3) + 0.3(3) + 0.1(2) = \mathbf{2.9}$   |         0.45 h (27.0 min)         |
| `TG12_CMP_MET`     |             3              |             2              |             2             |   $0.6(3) + 0.3(2) + 0.1(2) = \mathbf{2.6}$   |         0.50 h (30.0 min)         |
| `TG13_WET_BENCH`   |             2              |             2              |             2             |   $0.6(2) + 0.3(2) + 0.1(2) = \mathbf{2.0}$   |        1.10 h (batch of 3)        |
| `TG14_WET_SINGLE`  |             4              |             3              |             3             |   $0.6(4) + 0.3(3) + 0.1(3) = \mathbf{3.6}$   |         0.38 h (22.8 min)         |
| `TG15_RTP`         |             2              |             2              |             2             |   $0.6(2) + 0.3(2) + 0.1(2) = \mathbf{2.0}$   |         0.32 h (19.2 min)         |
| `TG16_MET_CD`      |             3              |             3              |             2             |   $0.6(3) + 0.3(3) + 0.1(2) = \mathbf{2.9}$   |         0.35 h (21.0 min)         |
| `TG17_MET_THICK`   |             2              |             2              |             2             |   $0.6(2) + 0.3(2) + 0.1(2) = \mathbf{2.0}$   |         0.30 h (18.0 min)         |
| `TG18_INSPECT`     |             2              |             2              |             2             |   $0.6(2) + 0.3(2) + 0.1(2) = \mathbf{2.0}$   |         0.42 h (25.2 min)         |
| **Sum Operations** |          **120**           |          **104**           |          **92**           |                       —                       |                 —                 |

_Note on Metrology Sampling_: Operations mapped to `TG16_MET_CD`, `TG17_MET_THICK`, and `TG18_INSPECT` reflect post-sampling effective visits. While 100% of lots visit lithography, only critical gate, contact, and metal layers undergo full defect inspection and ellipsometry.

### 2.5 Processing Time Distribution Family

Process times follow a 2-parameter **Lognormal distribution** $T \sim \text{Lognormal}(\mu_{\log}, \sigma_{\log})$. The distribution family is specified once globally. For an operation with mean duration $\bar{t}_g$ and coefficient of variation $CV = \sigma_{\text{raw}} / \bar{t}_g$:
$$\sigma_{\log} = \sqrt{\ln(1 + CV^2)}, \quad \mu_{\log} = \ln(\bar{t}_g) - \frac{1}{2}\sigma_{\log}^2$$

- For all **serial tools** (`TG01`–`TG06`, `TG09`–`TG12`, `TG14`–`TG18`), $CV = 0.15$ ($\sigma_{\log} \approx 0.1492$).
- For all **batch furnaces & wet clean benches** (`TG07`, `TG08`, `TG13`), $CV = 0.08$ ($\sigma_{\log} \approx 0.0798$).

### 2.6 Lot Arrival Process & Utilization Arithmetic (Verification)

Lots arrive according to a homogeneous Poisson process with constant rate $\lambda$.

#### Mathematical Derivation of Bottleneck Utilization:

Let:

- $\lambda$: Lot arrival rate (lots per hour).
- $\bar{V}_g$: Expected number of visits to tool group $g$ per arriving lot across the product mix.
- $\bar{t}_g$: Nominal machine processing time per run (hours).
- $B_g$: Nominal batch size (for serial tools $B_g = 1$; for batch tools $B_g = 3$).
- $N_g$: Number of physical machines in group $g$.
- $A_g$: SEMI E10 equipment availability factor: $A_g = \frac{\text{MTBF}_g}{\text{MTBF}_g + \text{MTTR}_g}$.

The effective machine processing workload per arriving lot is:
$$W_g = \bar{V}_g \cdot \frac{\bar{t}_g}{B_g} \quad [\text{hours/lot}]$$

The effective production capacity of tool group $g$ is:
$$C_g = N_g \cdot A_g \quad [\text{machine-hours/hour}]$$

The long-term stationary utilization $U_g$ is:
$$U_g = \frac{\lambda \cdot W_g}{C_g} = \frac{\lambda \cdot \bar{V}_g \cdot (\bar{t}_g / B_g)}{N_g \cdot A_g}$$

#### Calibration to 88%–93% Bottleneck Band:

The bottleneck group is photolithography (`TG01_LITHO`):

- $N_{\text{litho}} = 38$ machines.
- $\text{MTBF} = 90.0\text{ h}$, $\text{MTTR} = 10.0\text{ h} \implies A_{\text{litho}} = \frac{90.0}{90.0 + 10.0} = 0.900$.
- $C_{\text{litho}} = 38 \times 0.900 = \mathbf{34.20}\text{ machine-hours/hour}$.
- Weighted visits: $\bar{V}_{\text{litho}} = 0.60(28) + 0.30(24) + 0.10(20) = \mathbf{26.0}\text{ visits/lot}$.
- Nominal lot processing time: $\bar{t}_{\text{litho}} = 0.50\text{ h}$ (including reticle setup overhead).
- Workload per lot: $W_{\text{litho}} = 26.0 \times 0.50 = \mathbf{13.00}\text{ h/lot}$.

We set the lot arrival rate to:
$$\lambda = \mathbf{2.40}\text{ lots/hour} \quad (= 57.6\text{ lots/day} = 1,440\text{ wafers/day})$$

Substituting into the utilization formula:
$$U_{\text{litho}} = \frac{2.40 \times 13.00}{34.20} = \frac{31.20}{34.20} = \mathbf{91.23\%}$$

$91.23\%$ falls strictly within the required $[88.0\%, 93.0\%]$ utilization band.

#### Table 3: Complete Fab Utilization Spectrum

| Tool Group ID             | Machines ($N_g$) | Availability ($A_g$) | Workload $W_g$ (h/lot) | Effective Capacity $C_g$ | Stationary Utilization $U_g$ |
| ------------------------- | :--------------: | :------------------: | :--------------------: | :----------------------: | :--------------------------: |
| `TG01_LITHO` (Bottleneck) |        38        |        0.900         |         13.00          |          34.20           |          **91.23%**          |
| `TG02_TRACK`              |        35        |        0.920         |         11.44          |          32.20           |          **85.27%**          |
| `TG03_ETCH`               |        30        |        0.910         |          9.30          |          27.30           |          **81.76%**          |
| `TG04_STRIP`              |        9         |        0.940         |          1.96          |           8.46           |          **55.60%**          |
| `TG05_CVD`                |        20        |        0.910         |          5.47          |          18.20           |          **72.16%**          |
| `TG06_PVD`                |        9         |        0.920         |          1.98          |           8.28           |          **57.39%**          |
| `TG07_FURN_DIFF`          |        9         |        0.920         |          2.13          |           8.28           |          **61.84%**          |
| `TG08_FURN_LPCVD`         |        7         |        0.920         |          1.87          |           6.44           |          **69.57%**          |
| `TG09_IMPL_MED`           |        7         |        0.900         |          1.56          |           6.30           |          **59.43%**          |
| `TG10_IMPL_HIGH`          |        7         |        0.900         |          1.50          |           6.30           |          **57.14%**          |
| `TG11_CMP_OX`             |        7         |        0.930         |          1.30          |           6.51           |          **48.11%**          |
| `TG12_CMP_MET`            |        7         |        0.930         |          1.30          |           6.51           |          **47.93%**          |
| `TG13_WET_BENCH`          |        5         |        0.940         |          0.73          |           4.70           |          **37.45%**          |
| `TG14_WET_SINGLE`         |        7         |        0.940         |          1.37          |           6.58           |          **49.90%**          |
| `TG15_RTP`                |        5         |        0.930         |          0.64          |           4.65           |          **33.03%**          |
| `TG16_MET_CD`             |        6         |        0.950         |          1.01          |           5.70           |          **42.74%**          |
| `TG17_MET_THICK`          |        4         |        0.950         |          0.60          |           3.80           |          **37.89%**          |
| `TG18_INSPECT`            |        5         |        0.950         |          0.84          |           4.75           |          **42.44%**          |

All non-bottleneck groups operate between 33% and 86% utilization, ensuring physical stability under steady-state operation.

### 2.7 Equipment Downtimes & Preventive Maintenance (PM)

Equipment reliability strictly follows the **SEMI E10 standard**:

- **Unscheduled Downtime (UDT)**: Failure events follow an Exponential distribution with mean $\text{MTBF}_g$. Repair durations follow an Exponential distribution with mean $\text{MTTR}_g$ (Table 1).
- **Scheduled Downtime (SDT / PM)**: Pre-emptive maintenance windows are scheduled for key tool groups:
  1. `TG01_LITHO`: Optical lens cleaning & laser calibration every $168.0\text{ h}$ (7 days); downtime duration $8.0\text{ h}$.
  2. `TG03_ETCH`: Plasma chamber wet strip & seasoning every $120.0\text{ h}$ (5 days); downtime duration $6.0\text{ h}$.
  3. `TG05_CVD`: Showerhead clean & particle qualification every $168.0\text{ h}$ (7 days); downtime duration $6.0\text{ h}$.

### 2.8 Quality Deviations: Rework Loops & Scrap Probabilities

- **Rework Loops**:
  - _Gate Litho Rework_: At Step 28 (`TG01_LITHO`), post-exposure CD metrology identifies critical defect with probability $p_{\text{rework}} = 0.025$ (2.5%). Rework route: Strip resist (`TG04`) $\to$ Clean (`TG14`) $\to$ Recoat & Re-expose (`TG02`/`TG01`). Loop length = 3 steps.
  - _Metal 1 CMP Rework_: At Step 64 (`TG11_CMP_OX`), thickness metrology detects under-polish with probability $p_{\text{rework}} = 0.015$ (1.5%). Rework route: Touch-up buff (`TG11`) $\to$ Clean (`TG14`). Loop length = 2 steps.
- **Scrap Rates**: Every single operation carries a small Bernoulli scrap probability $p_{\text{scrap}} = 0.0004$ (0.04% per operation). Over a 120-operation route, the lot completion yield is $(1 - 0.0004)^{120} = 95.31\%$.

---

## 3. Benchmark Tasks (T1, T2, T3)

### Task 1 (T1) — Dynamic Real-Time Lot Dispatching

- **Context**: When any machine $m \in \mathcal{M}_g$ finishes processing and becomes idle, the scheduler must select the next lot (or batch of lots) from the queue of waiting lots $Q_g$.
- **Decision Variable**: Index of the lot(s) $l^* \in Q_g$ assigned to machine $m$ at decision time $t$.
- **Constraints**:
  1. Lot must be currently resident in the tool buffer or load port.
  2. For batch tools (`TG07`, `TG08`, `TG13`), batch size must satisfy $B_{\min} \le |B| \le B_{\max}$, and all lots in the batch must share compatible thermal/chemical recipes.
  3. Reticle and dopant setup sequence constraints: consecutive lots of different families incur fixed setup changeover penalties.
- **Primary Metric**: Mean Cycle Time (Flow Time) $\bar{C} = \frac{1}{|L_{\text{comp}}|} \sum_{l \in L_{\text{comp}}} (C_l - r_l)$, where $r_l$ is arrival time and $C_l$ is completion time.
- **Secondary Metrics**: Cycle Time Standard Deviation $\sigma_C$, 95th Percentile Tardiness $\max(0, C_l - d_l)$, Fab Total Work-in-Process (WIP).

### Task 2 (T2) — Automated Material Handling System (AMHS) OHT Routing

- **Context**: FOUPs are transported between tool bays via an Overhead Hoist Transport (OHT) track network consisting of 8 inter-bay loops and 18 local intra-bay spurs, populated by 60 automated OHT vehicles.
- **Decision Variable**: Vehicle dispatch assignment (which idle vehicle picks up FOUP $l$) and route path (sequence of track segment switches).
- **Constraints**: Single-track vehicle headway distance (no passing), collision avoidance, bay transfer bypass capacities.
- **Primary Metric**: Mean FOUP Delivery Time $\bar{T}_{\text{delivery}} = \bar{T}_{\text{wait\_pickup}} + \bar{T}_{\text{transit}}$.
- **Secondary Metrics**: Vehicle empty transit ratio $\frac{D_{\text{empty}}}{D_{\text{total}}}$, track congestion delay hours.

### Task 3 (T3) — Opportunistic Preventive Maintenance (PM) Scheduling

- **Context**: Scheduled maintenance for `TG01`, `TG03`, and `TG05` must be carried out within a floating window $[T_{\text{due}} - \Delta_{\text{slack}}, T_{\text{due}} + \Delta_{\text{slack}}]$ where $\Delta_{\text{slack}} = 24.0\text{ hours}$.
- **Decision Variable**: Specific initiation timestamp $t_{\text{start}}$ for tool PM.
- **Objective**: Synchronize PM downtime with tool starvation or upstream supply disruptions, avoiding simultaneous shutdown of parallel bottleneck tools.
- **Primary Metric**: Effective Production Rate (lots completed per day during high-utilization steady state).
- **Secondary Metric**: Avoidable Starvation Hours induced by PM overlap.

---

## 4. Evaluation Protocol

To ensure reproducible scientific comparisons across dispatching algorithms, machine learning agents, and commercial solvers:

1. **Warm-up Period**: **60.0 simulated days** (1,440.0 hours). All lots started during warm-up are tracked for system stabilization but excluded from performance metric accumulation.
2. **Run Length**: **365.0 simulated days** (8,760.0 hours) post warm-up.
3. **Replication Strategy**: **30 independent replications** ($R = 30$) initialized with distinct master pseudo-random seeds ($S_1, \dots, S_{30}$).
4. **Variance Reduction**: Evaluation across competing policies **must employ Common Random Numbers (CRN)**. The exact sequence of lot arrivals, processing time draws, failure occurrences, and rework determinations must be identical across comparisons.
5. **Statistical Reporting**:
   - Report mean metric value $\hat{\mu} = \frac{1}{R}\sum_{r=1}^R X_r$ with 95% Confidence Intervals:
     $$\text{CI}_{95\%} = \left[ \hat{\mu} - 2.045 \frac{S}{\sqrt{R}}, \; \hat{\mu} + 2.045 \frac{S}{\sqrt{R}} \right]$$
   - Hypotheses tests comparing candidate policies against baselines must use a **paired two-tailed Student's $t$-test** (or Wilcoxon signed-rank test if normality is rejected) at significance level $\alpha = 0.05$.

---

## 5. Standard Baseline Dispatching Rules

The benchmark specifies explicit mathematical formulations for dispatching baselines to prevent ambiguous implementations:

### 5.1 First-In, First-Out (FIFO)

At decision time $t$, select lot $l^*$ from queue $Q_g$ that arrived earliest at the current queue:
$$l^* = \arg\min_{l \in Q_g} \{ t_{\text{queue\_enter}}(l) \}$$
_Tie-breaker_: Lowest unique `lot_id`.

### 5.2 Shortest Processing Time (SPT)

Select the lot with the lowest expected processing time for the pending step:
$$l^* = \arg\min_{l \in Q_g} \{ \bar{t}_{l, \text{current\_step}} \}$$
_Tie-breaker_: Earliest queue entry time (FIFO).

### 5.3 Earliest Due Date (EDD)

Each lot carries due date $d_l = r_l + k \cdot \sum_{s=1}^{S_l} \bar{t}_{l, s}$, where $k = 3.0$ (due date factor).
$$l^* = \arg\min_{l \in Q_g} \{ d_l \}$$
_Tie-breaker_: Earliest queue entry time (FIFO).

### 5.4 Critical Ratio (CR)

At decision time $t$, define the Critical Ratio for lot $l$:
$$\text{CR}_l(t) = \frac{d_l - t}{\sum_{s \in \text{remaining}(l)} \bar{t}_{l, s}}$$
$$\text{Priority Rule}: \quad l^* = \arg\min_{l \in Q_g} \{ \text{CR}_l(t) \}$$
If $\text{CR}_l(t) < 0$, the lot is already late and receives strict priority over positive CR lots.
_Tie-breaker_: Earliest due date (EDD).

### 5.5 Batch Tool Formation Policy (Common Across All Baselines)

For batch tool groups (`TG07`, `TG08`, `TG13`):
A batch initiates immediately if $|Q_g^{\text{compat}}| \ge B_{\max} = 4$. If $B_{\min} \le |Q_g^{\text{compat}}| < B_{\max}$, the batch is held up to a **maximum batch timeout** $\tau_{\text{timeout}} = 2.0\text{ hours}$. If the oldest waiting lot in the compatible set has waited $\ge 2.0\text{ hours}$, the machine starts with the available batch size ($\ge B_{\min} = 2$). If fewer than $B_{\min}$ lots exist, the machine remains idle.

### 5.6 AMHS Nearest-Idle Baseline (T2)

When FOUP transport is requested, query all idle OHT vehicles and assign:
$$v^* = \arg\min_{v \in \mathcal{V}_{\text{idle}}} \{ \text{DijkstraDistance}(\text{location}(v), \text{pickup\_location}) \}$$

### 5.7 Fixed-Interval Periodic PM Baseline (T3)

Trigger equipment maintenance exactly at nominal intervals:
$$t_{\text{PM\_start}} = k \cdot T_{\text{interval}}, \quad k \in \{1, 2, \dots\}$$
ignoring buffer occupancy or upstream starvation.

---

## 6. Behavioral Validation Criteria (Smoke & Sanity Gates)

Any compliant simulator implementation must satisfy four behavioral validation gates before deployment:

### Criterion 1: Bottleneck Utilization Conformance

- **Test**: Run baseline FIFO simulation for 365 days post warm-up. Measure cumulative busy time divided by available time for `TG01_LITHO`.
- **Pass Threshold**: $88.0\% \le \bar{U}_{\text{litho}} \le 93.0\%$ (Target design: $91.23\% \pm 1.5\%$).

### Criterion 2: Superlinear WIP Growth Under Traffic Escalation

- **Test**: Increase arrival rate $\lambda$ by $+5.0\%$ (from $2.40$ to $2.52\text{ lots/h}$, pushing nominal bottleneck load to $\approx 95.8\%$).
- **Pass Threshold**: Average fab WIP must increase by **$\ge 35.0\%$** relative to baseline (validating Kingman's heavy-traffic nonlinear queue explosion).

### Criterion 3: Directional Superiority of Due-Date Dispatching

- **Test**: Compare FIFO vs CR over 30 paired replications using Common Random Numbers.
- **Pass Threshold**: Mean tardiness under CR must be strictly lower than FIFO:
  $$\bar{T}_{\text{CR}} < \bar{T}_{\text{FIFO}} \quad \text{with } p\text{-value} < 0.01$$

### Criterion 4: System Stability & Absence of Deadlocks

- **Test**: Continuous 365-day execution across all 30 random seeds without manual intervention.
- **Pass Threshold**: Zero simulation deadlocks (e.g. mutual block on single-track OHT or circular wafer buffer dependencies) and bounded maximum queue sizes across all tool buffers.

---

## 7. Gymnasium Reinforcement Learning API (Task 1)

MIMAC-2026 provides a standard Gymnasium-compatible Python interface for RL researchers:

```python
import gymnasium as gym
from gymnasium import spaces

class MimacFabEnv(gym.Env):
    """MIMAC-2026 Reinforcement Learning Environment for Task 1 (Dispatching)."""
    metadata = {"render_modes": ["json_stream", "twin_websocket"], "version": "1.0.0"}

    def __init__(self, config: dict = None):
        super().__init__()
        # Observation: Per-tool buffer state vector (normalized)
        # Features per waiting lot: [remaining_ops, due_date_slack_h, current_wait_h, setup_match]
        self.max_queue_len = 32
        self.lot_features = 4
        self.observation_space = spaces.Dict({
            "tool_group_id": spaces.Discrete(18),
            "machine_id": spaces.Discrete(38),
            "current_setup_family": spaces.Discrete(4),
            "queue_length": spaces.Discrete(self.max_queue_len + 1),
            "queue_matrix": spaces.Box(
                low=-100.0, high=1000.0, shape=(self.max_queue_len, self.lot_features), dtype=np.float32
            )
        })

        # Action: Select lot index from 0 to max_queue_len - 1 (or 0 for FIFO fallback)
        self.action_space = spaces.Discrete(self.max_queue_len)

    def reset(self, seed: int = None, options: dict = None) -> tuple[dict, dict]:
        """Reset the simulation environment to initial state."""
        super().reset(seed=seed)
        # Initializes SimPy event loop, warms up to Day 60, returns first decision state
        ...
        return obs, info

    def step(self, action: int) -> tuple[dict, float, bool, bool, dict]:
        """
        Assign selected lot to the idle machine, advance simulation clock
        to the next decision epoch, and return transition tuple.
        """
        ...
        # Reward: Negative weighted cycle time & tardiness step increment
        reward = -(step_cycle_time_penalty + 2.0 * step_tardiness_penalty)
        return obs, reward, terminated, truncated, info
```

---

## 8. Digital Twin Event Stream Schema

To power the 3D Cleanroom Digital Twin (`semiconfab.org/twin`), MIMAC-2026 emits real-time JSON event packets. The stream conforms to the following schema:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "MIMAC-2026 Twin Event Packet",
  "type": "object",
  "required": ["timestamp_sec", "event_type", "payload"],
  "properties": {
    "timestamp_sec": {
      "type": "number",
      "description": "Simulation elapsed time in seconds"
    },
    "event_type": {
      "type": "string",
      "enum": [
        "lot_spawned",
        "lot_step_start",
        "lot_step_complete",
        "tool_state_change",
        "oht_transfer_start",
        "oht_transfer_complete",
        "wip_sample"
      ]
    },
    "payload": {
      "type": "object",
      "properties": {
        "lot_id": { "type": "string" },
        "product": { "type": "string", "enum": ["A", "B", "C"] },
        "tool_group_id": { "type": "string" },
        "machine_id": { "type": "string" },
        "semi_e10_state": {
          "type": "string",
          "enum": [
            "PR_productive",
            "SBY_standby",
            "ENG_engineering",
            "UDT_unscheduled_down",
            "SDT_scheduled_down"
          ]
        },
        "step_index": { "type": "integer" },
        "oht_vehicle_id": { "type": "string" },
        "wip_count": { "type": "integer" }
      }
    }
  }
}
```

---

## 9. Parameter Provenance & Honesty Tiers

In accordance with the SemiconFab specification integrity rules, Table 4 explicitly documents the source provenance tier for every parameter family in MIMAC-2026. **Zero parameters are claimed as `vendor_confirmed`**, maintaining complete academic and industrial integrity.

#### Table 4: Benchmark Parameter Provenance Registry

| Parameter Cluster                                        | Assigned Provenance Tier | Reference / Methodological Rationale                                                 |
| -------------------------------------------------------- | :----------------------: | ------------------------------------------------------------------------------------ |
| Equipment Topology & Machine Counts ($N_g=217$)          |       `synthetic`        | Calibrated to represent modern 40k–50k WSPM 300mm logic megafab scale.               |
| Tool Classifications & Batch Sizes                       |        `inferred`        | Inferred from standard semiconductor process literature (SEMI E72, Uzsoy et al.).    |
| SEMI E10 RAM Reliability Parameters (MTBF/MTTR)          |        `inferred`        | Scaled from SEMI E10 equipment reliability survey distributions.                     |
| Process Route Steps (120, 104, 92 ops)                   |       `synthetic`        | Synthesized to capture re-entrancy without disclosing proprietary foundry recipes.   |
| Lithography Re-entrant Pass Counts (28, 24, 20)          |        `inferred`        | Inferred from published advanced FEOL/BEOL logic metallization layer counts.         |
| Lognormal Processing Time Parameters ($\bar{t}_g$, $CV$) |       `synthetic`        | Calibrated to ensure clean bottleneck utilization at $\lambda = 2.40\text{ lots/h}$. |
| Rework Loop Rates ($2.5\%$, $1.5\%$)                     |        `inferred`        | Typical gate lithography and CMP touch-up rates documented in fab surveys.           |
| Scrap Rate ($0.04\%$/step)                               |        `inferred`        | Consistent with modern world-class foundry overall line yield ($\approx 95\%$).      |
| OHT Network Topology (8 loops, 60 vehicles)              |       `synthetic`        | Stylized dual-loop cleanroom inter-bay layout for 3D twin visualization.             |

---

## 10. Versioning, Governance & References

### 10.1 Versioning & Changelog

- **v1.0 (2026-10-11)**: Initial comprehensive public release specification. Defined 18 tool groups, 217 machines, 3 product routes, exact bottleneck utilization derivation (91.23%), 3 tasks, evaluation protocol, and Gym API.

### 10.2 Governance & Citation

When referencing this benchmark in scientific publications, cite as:

> SemiconFab Consortium. _MIMAC-2026: An Open, Watchable Benchmark Testbed for Semiconductor Fab Operations Research and Reinforcement Learning_. SemiconFab Technical Report SF-TR-2026-01, arXiv:2610.MIMAC [VERIFY], 2026.

### 10.3 References

1. **Fowler, J. W., & Robinson, J. K.** (1995). _Measurement and Improvement of Manufacturing Capacities (MIMAC): Final Report_. SEMATECH Technology Transfer #95062861A-TR, Austin, TX.
2. **Uzsoy, R., Lee, C. Y., & Martin-Vega, L. A.** (1992). A review of production planning and scheduling models in the semiconductor manufacturing industry—part I: system characteristics, performance evaluation and extreme problem formulations. _IIE Transactions_, 24(4), 47–60.
3. **Uzsoy, R., Lee, C. Y., & Martin-Vega, L. A.** (1994). A review of production planning and scheduling models in the semiconductor manufacturing industry—part II: shop-floor scheduling. _IIE Transactions_, 26(5), 44–55.
4. **Wein, L. M.** (1988). Scheduling semiconductor wafer fabrication. _IEEE Transactions on Semiconductor Manufacturing_, 1(3), 115–130.
5. **Rose, O.** (2007). The WIP versus cycle time relationship in semiconductor wafer fabrication. _Proceedings of the 2007 Winter Simulation Conference_, 1689–1697.
6. **SEMI Standard E10-0304** (2004). _Specification for Definition and Measurement of Equipment Reliability, Availability, and Maintainability (RAM)_. Semiconductor Equipment and Materials International, San Jose, CA.
7. **SEMI Standard E72-0600** (2000). _Specification for Equipment Footprint, Height, and Weight_. Semiconductor Equipment and Materials International.
8. **Kingman, J. F. C.** (1961). The single server queue in heavy traffic. _Mathematical Proceedings of the Cambridge Philosophical Society_, 57(4), 902–904.
9. **Kempf, K. G., Uzsoy, R., & Smith, J. S.** (Eds.) (2011). _Planning Production and Inventories in the Extended Enterprise: A State of the Art Handbook_. Springer Science & Business Media.
10. **Pinedo, M. L.** (2016). _Scheduling: Theory, Algorithms, and Systems_ (5th ed.). Springer.
