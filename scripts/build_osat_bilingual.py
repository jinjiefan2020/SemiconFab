#!/usr/bin/env python3
"""
Bilingual OSAT specifications and provenance notes builder.
Generates English and Chinese specs/notes for all 86 OSAT equipment records,
and synchronizes data/osat-86-ground-truth.json and twin-osat.html.
"""

import json
import re

OSAT_BILINGUAL_MAP = {
  # --- Bay 1: Dicing (15 models) ---
  ("DISCO", "DFD6361"): {
    "specs_en": "Max workpiece Φ300mm; X-axis cutting range 310mm @ 0.1–600mm/s; Dual spindle 1.2kW standard (1.8/2.2kW optional); Positioning accuracy within 0.002/310mm",
    "specs_zh": "最大工件 Φ300mm；X 向切割范围 310mm @ 0.1–600mm/s；双主轴 1.2kW 标准（1.8/2.2kW 可选）；定位精度 0.002/310mm 以内",
    "notes_en": "[source note] Specifications from DISCO brochure data; prior-gen model with large installed base",
    "notes_zh": "[source note] 规格表转载 DISCO 手册数据；上一代机型，装机量仍大"
  },
  ("DISCO", "DFD6362"): {
    "specs_en": "Fully automated dual-spindle dicing saw; 300mm wafer FOUP/cassette handling (per Micron configuration datasheet)",
    "specs_zh": "全自动双主轴划片机；300mm 晶圆盒处理（按 Micron 配置机数据表）",
    "notes_en": "[source note] 2010s Micron configuration equipment datasheet",
    "notes_zh": "[source note] 2010 年代 Micron 配置机设备数据表"
  },
  ("DISCO", "DFD6340"): {
    "specs_en": "Max wafer size 8\" (200mm); Dual spindle 1.2kW @ 60,000 rpm; 2\" blades; Auto-alignment + kerf check",
    "specs_zh": "最大晶圆 8 英寸；双主轴 1.2kW @ 60,000rpm；2 英寸刀片；自动对准 + 切口检测",
    "notes_en": "[source note] Secondary market dealer equipment specifications",
    "notes_zh": "[source note] 二手设备商规格表"
  },
  ("DISCO", "DAD3241"): {
    "specs_en": "Single-spindle dicing saw; 8\" substrate; X-axis cutting 210mm @ 0.1–800mm/s; Y-axis indexing 0.0001mm",
    "specs_zh": "单主轴划片机；8 英寸基板；X 向切割 210mm @ 0.1–800mm/s；Y 向步进 0.0001mm",
    "notes_en": "[source note] DTU University cleanroom laboratory tool sheet (compared with DAD321)",
    "notes_zh": "[source note] DTU 大学实验室设备页（与 DAD321 对比）"
  },
  ("DISCO", "DAD321"): {
    "specs_en": "6\" substrate; X-axis cutting 192mm @ 0.1–300mm/s; Synchronous spindle 1000W",
    "specs_zh": "6 英寸基板；X 向切割 192mm @ 0.1–300mm/s；同步主轴 1000W",
    "notes_en": "[source note] Legacy generation tool (recorded listing year 2000)",
    "notes_zh": "[source note] 较老代际（2000 年挂牌记录）"
  },
  ("Accretech", "AD3000T-PLUS"): {
    "specs_en": "Fully automated dicing saw; Dual opposing spindles; Φ300mm wafers; HC variant for half-cut process",
    "specs_zh": "全自动划片机；双面对置双轴主轴；Φ300mm 晶圆；HC 变体为半切工艺",
    "notes_en": "[source note] ACCRETECH official product guide",
    "notes_zh": "[source note] 出自 ACCRETECH 官方产品指南"
  },
  ("Accretech", "AD3000TW"): {
    "specs_en": "Fully automated dual-spindle dicing saw; Supports large packaging substrates up to 360×360mm",
    "specs_zh": "全自动双主轴划片机；支持最大 360×360mm 大型封装基板",
    "notes_en": "[source note] Official product guide new release",
    "notes_zh": "[source note] 官方指南标注为新品"
  },
  ("Accretech", "AD2000T/S"): {
    "specs_en": "Fully automated dicing saw; T = dual spindle / S = single spindle; Φ200mm",
    "specs_zh": "全自动划片机；T = 双主轴 / S = 单主轴；Φ200mm",
    "notes_en": "[source note] ACCRETECH official product guide",
    "notes_zh": "[source note] 出自官方产品指南"
  },
  ("Accretech", "SS20"): {
    "specs_en": "Semi-automatic dicing saw; Max workpiece Φ8\"/250mm; Standard spindle 60,000 rpm 1.8kW (opt. 80,000 rpm or 2.2kW); X-cut 260mm @ up to 800mm/s; Accuracy 0.002/260mm",
    "specs_zh": "半自动划片机；最大工件 Φ8″/250mm；主轴标准 60,000rpm 1.8kW（可选 80,000rpm 或 2.2kW）；X 向切割 260mm @ 最高 800mm/s；精度 0.002/260mm",
    "notes_en": "[source note] Official datasheet; SS20 PLUS variant also available",
    "notes_zh": "[source note] 官方规格表；另有 SS20 PLUS 变体"
  },
  ("Accretech", "SS30"): {
    "specs_en": "Semi-automatic single-spindle dicing saw for Φ200mm wafers",
    "specs_zh": "半自动单主轴划片机，面向 Φ200mm 晶圆",
    "notes_en": "[source note] Official product guide; SS30 PLUS variant also available",
    "notes_zh": "[source note] 另有 SS30 PLUS 变体"
  },
  ("DISCO", "DFL7340"): {
    "specs_en": "Stealth Dicing laser saw; Internal IR laser modified layer formation; Zero kerf width loss; Tape expansion separation",
    "specs_zh": "隐形切割（Stealth Dicing）激光划片机；红外激光在晶圆内部形成改质层；零切口损耗；扩膜分离",
    "notes_en": "[source note] University of Tokyo laboratory verification; cited on photonics.com",
    "notes_zh": "[source note] 存在性经东京大学使用报告确认；photonics.com 亦有引用"
  },
  ("DISCO", "DFL7360"): {
    "specs_en": "Next-gen Stealth Dicing laser saw platform (advanced successor to DFL7340)",
    "specs_zh": "隐形切割激光划片机（比 DFL7340 更新一代）",
    "notes_en": "[source note] Photonics Spectra article citation for DISCO Stealth Dicing systems",
    "notes_zh": "[source note] Photonics Spectra 文章引用为 DISCO 隐形切割机"
  },
  ("DISCO", "DFL7161"): {
    "specs_en": "Laser grooving and ablation dicing saw for scribing and cutting",
    "specs_zh": "激光锯/划片机，用于划线与切割（烧蚀式）",
    "notes_en": "[source note] Component listing verification; FX variant",
    "notes_zh": "[source note] 存在性经零部件挂牌确认；FX 变体"
  },
  ("Accretech", "AL3000"): {
    "specs_en": "Fully automated laser dicing system with integrated laser grooving engine",
    "specs_zh": "全自动激光划片机，带激光开槽引擎",
    "notes_en": "[source note] ACCRETECH official product guide",
    "notes_zh": "[source note] 出自官方产品指南"
  },
  ("Accretech", "ML3200FH"): {
    "specs_en": "Laser dicing system; Triple station dual-head configuration; Internal laser stealth processing (focus inside Si)",
    "specs_zh": "激光划片机；三工位双头配置；隐形切割式加工（激光在 Si 内部聚焦）",
    "notes_en": "[source note] Official product line; smaller ML2200 variant also available",
    "notes_zh": "[source note] 另有较小变体 ML2200"
  },

  # --- Bay 2: Die Attach (4 models) ---
  ("ASMPT", "INFINITE"): {
    "specs_en": "Up to 18,500 UPH; Placement accuracy ±20µm @ 3σ (high-accuracy mode ±12.5µm @ 3σ); Die size 0.2×0.2–9×9mm, thickness 0.075–1mm; Bond force 0.196–29.43N; Max substrate 300×100mm",
    "specs_zh": "最高 18,500 UPH；贴装精度 ±20µm @ 3σ（高精度模式 ±12.5µm @ 3σ）；芯片 0.2×0.2–9×9mm、厚 0.075–1mm；键合力 0.196–29.43N；最大基板 300×100mm",
    "notes_en": "[source note] Flagship die attach system released May 2025",
    "notes_zh": "[source note] 旗舰固晶机，2025 年 5 月发布"
  },
  ("ASMPT", "AD8312"): {
    "specs_en": "Die bonder; Placement accuracy ±0.002mm (±2µm); Floating die pick-up mechanism",
    "specs_zh": "固晶机；贴装精度 ±0.002mm；浮动式芯片拾取机构",
    "notes_en": "[source note] High-precision die attach model; 2013 listing record",
    "notes_zh": "[source note] 较老高精度型号；2013 年挂牌记录"
  },
  ("ASMPT", "AD830 Plus"): {
    "specs_en": "Cycle time 163ms; Die size 6×6–200×200 mil; Wafer handling up to 8\" (200mm); Leadframe width 12–102mm",
    "specs_zh": "周期时间 163ms；芯片 6×6–200×200 mil；晶圆处理至 8 英寸；引线框架宽 12–102mm",
    "notes_en": "[source note] Secondary equipment market specification summary",
    "notes_zh": "[source note] 二手设备规格摘要"
  },
  ("Besi", "Datacon 8800 (die attach platform)"): {
    "specs_en": "Datacon 8800 multi-module die attach platform; FC Quantum advX variant: 4µm @ 3σ; Up to 10k UPH; Die size 0.3–40mm; Substrate strips up to 8\"/200mm",
    "specs_zh": "8800 平台覆盖固晶；FC Quantum advX 变体：4µm @ 3σ；最高 10k UPH；芯片 0.3–40mm；条带 8″/200mm",
    "notes_en": "[source note] Besi Datacon 8800 platform covering die attach and flip chip; specs reflect FC Quantum advX variant",
    "notes_zh": "[source note] Besi 以 8800 平台同时覆盖固晶与倒装；所引规格为 FC Quantum advX 变体"
  },

  # --- Bay 3: Wire Bonding (5 models) ---
  ("ASMPT", "AERO PRO"): {
    "specs_en": "Ball bonder; Wire diameter 0.5–2.0 mil (12.7–50.8µm); X-POWER 2.0 transducer for uniform 22µm bonded balls; Substrate up to 105×300mm; AI process monitoring (AERO EYE / Diagnostics / Predictive)",
    "specs_zh": "球焊机；线径 0.5–2.0 mil（12.7–50.8µm）；X-POWER 2.0 换能器实现均匀 22µm 焊球；基板最大 105×300mm；AI 工艺监控（AERO EYE / Diagnostics / Predictive）",
    "notes_en": "[source note] Released in 2025; Targeted for fine-pitch SiP, MCM, BGA, and LGA",
    "notes_zh": "[source note] 2025 年发布；面向细间距 SiP/MCM/BGA/LGA"
  },
  ("Kulicke & Soffa", "RAPID Pro"): {
    "specs_en": "GEN-S series ball bonder; 35µm inline pad pitch; 0.6–2.5 mil Cu/Ag/Au wire; Placement accuracy 2.0µm @ 3σ; Leadframe length 90–300mm",
    "specs_zh": "GEN-S 系列球焊机；35µm 在线焊盘间距；0.6–2.5 mil Cu/Ag/Au 线；键合定位精度 2.0µm @ 3σ；引线框架长 90–300mm",
    "notes_en": "[source note] K&S brochure (distributor hosted); Industry 4.0 ready",
    "notes_zh": "[source note] K&S 手册（经销商托管）；支持工业 4.0"
  },
  ("Kulicke & Soffa", "Asterion"): {
    "specs_en": "Hybrid wedge bonder; Bond area 300×300mm; Repeatability ±3.0µm @ 3σ; Wire diameter 25–75µm; Supports Al/Cu wire and PowerRibbon",
    "specs_zh": "混合楔焊机；键合区 300×300mm；重复精度 ±3.0µm @ 3σ；线径 25–75µm；支持 Al/Cu 线与 PowerRibbon 带材",
    "notes_en": "[source note] K&S official brochure (distributor hosted); press release on investor.kns.com",
    "notes_zh": "[source note] K&S 手册（经销商托管）；发布新闻稿在 investor.kns.com"
  },
  ("Kulicke & Soffa", "Asterion EV"): {
    "specs_en": "Extended-area wedge bonder; Bond area 300×800mm; Dual/triple lane transport for battery and power modules",
    "specs_zh": "扩展区楔焊机；键合区 300×800mm；双/三通道输送，面向电池与功率模块",
    "notes_en": "[source note] Designed for large EV power modules and battery interconnects",
    "notes_zh": "[source note] 面向大型功率模块/电池包"
  },
  ("Kulicke & Soffa", "PowerFusion"): {
    "specs_en": "Wedge bonder family (TL/HL/HLx); HLx handles up to 105mm wide leadframes; Configurable from single-head to 6-head",
    "specs_zh": "楔焊机家族（TL/HL/HLx）；HLx 处理最宽 105mm 引线框架；单头至 6 头配置",
    "notes_en": "[source note] Dedicated for discrete and power semiconductor packaging",
    "notes_zh": "[source note] 功率半导体封装"
  },

  # --- Bay 4: Flip Chip & Advanced Packaging (12 models) ---
  ("Besi", "Datacon 8800 FC QUANTUM advX"): {
    "specs_en": "Accuracy 4µm @ 3σ; Throughput up to 10k UPH; Die size 0.3–40mm; Substrate strips/carriers/panels up to 8\"/200mm",
    "specs_zh": "精度 4µm @ 3σ；产能最高 10k UPH；芯片 0.3–40mm；条带/载具/面板 8″/200mm",
    "notes_en": "[source note] Mass reflow C2S (FC-BGA, FC-CSP, DRAM, Fan-out)",
    "notes_zh": "[source note] 批量回流 C2S（FC-BGA/FC-CSP/DRAM/扇出）"
  },
  ("Besi", "Datacon 8800 TC advanced"): {
    "specs_en": "Thermal Compression Bonding (TCB); 2µm @ 3σ; 7-axis bond head; 250N bond force; Optional 300mm/340mm FO-WLP carrier",
    "specs_zh": "热压键合（TCB）；2µm @ 3σ；7 轴键合头；250N 压力；可选 300mm/340mm FO-WLP 载具",
    "notes_en": "[source note] Besi technical documentation (trade exhibition hosted)",
    "notes_zh": "[source note] Besi 文档（展会站托管）"
  },
  ("Besi", "Datacon 8800 CHAMEO ultra plus"): {
    "specs_en": "Direct hybrid bonding; 200nm alignment accuracy; 1µm interconnect pitch; Up to 2,000 UPH",
    "specs_zh": "混合键合；200nm 对准精度；1µm 互连间距；最高 2,000 颗/小时",
    "notes_en": "[source note] Reported December 2025: world first unit installed at NHanced in Morrisville, NC",
    "notes_zh": "[source note] 据 2025 年 12 月报道，全球首台已在 NHanced（美国 Morrisville）投产"
  },
  ("ASMPT", "AMICRA NOVA"): {
    "specs_en": "Die and flip-chip bonder; ±1.0µm placement accuracy; Multi-die capability; Modular platform architecture",
    "specs_zh": "芯片 + 倒装键合机；±1.0µm 精度；多芯片能力；模块化设计",
    "notes_en": "[source note] ASMPT AMICRA official product brochure",
    "notes_zh": "[source note] ASMPT AMICRA 官方产品说明书"
  },
  ("ASMPT", "AMICRA NANO"): {
    "specs_en": "Ultra-precision die & flip chip bonder; ±0.2µm (200nm) @ 3σ; Bond force 0.1–20N; 200–400 UPH",
    "specs_zh": "超精密芯片/倒装键合机；±0.2µm @ 3σ；键合力 0.1–20N；200–400 件/小时",
    "notes_en": "[source note] Co-packaged optics (CPO) and hybrid bonding; high-mix low-volume production",
    "notes_zh": "[source note] 共封装光学 / 混合键合；高混低量产"
  },
  ("ASMPT", "MEGA"): {
    "specs_en": "Multi-die bonder; ±2µm accuracy; Bond line thickness control ±5µm; Throughput up to 12K UPH",
    "specs_zh": "多芯片键合机；±2µm 精度；键合线厚度控制 ±5µm；最高 12K UPH",
    "notes_en": "[source note] Designed for AI/HPC multi-chip modules; debuted at NEPCON Japan",
    "notes_zh": "[source note] 面向 AI/HPC 多芯片模块；NEPCON Japan 首发"
  },
  ("Shibaura Mechatronics", "TFC-6500"): {
    "specs_en": "Multi-process flip-chip bonder; Leading market share in high-end 2.5D packaging (Shibaura disclosure)",
    "specs_zh": "多工艺键合机；高端 2.5D 封装份额最大（Shibaura 口径）",
    "notes_en": "[source note] Shibaura Mechatronics semiconductor product portfolio",
    "notes_zh": "[source note] 芝浦机电半导体设备产品线"
  },
  ("Shibaura Mechatronics", "TFC-6600"): {
    "specs_en": "Advanced wafer-level packaging bonder; Face-up bonding for higher accuracy and throughput in FO-WLP",
    "specs_zh": "高端晶圆级封装键合机；正面朝上键合，面向 FO-WLP 的更高精度/产能",
    "notes_en": "[source note] Shibaura Mechatronics official product guide",
    "notes_zh": "[source note] 芝浦机电官方产品指南"
  },
  ("Shibaura Mechatronics", "TFC-6700 / TFC-6800"): {
    "specs_en": "Hybrid bonder for chip-to-wafer (C2W) direct hybrid bonding and fusion bonding; Ultra-high accuracy",
    "specs_zh": "混合键合机，面向芯粒-晶圆（C2W）混合键合与熔融工艺；超高精度",
    "notes_en": "[source note] Shibaura Mechatronics advanced packaging roadmap",
    "notes_zh": "[source note] 芝浦机电先进封装路线图"
  },
  ("Shibaura Mechatronics", "TFC-9300"): {
    "specs_en": "Fan-out panel-level packaging (FO-PLP) bonder; Industry-leading PLP market share (Shibaura disclosure)",
    "specs_zh": "扇出面板级封装键合机；FO-PLP 份额最大（Shibaura 口径）",
    "notes_en": "[source note] Shibaura product portfolio; TFC-9000 is the FO-WLP wafer counterpart",
    "notes_zh": "[source note] TFC-9000 为 FO-WLP 变体"
  },
  ("Toray Engineering", "FC3000W series"): {
    "specs_en": "Substrate 8\"/12\"; Die size 3–20mm; Cycle time 2.0s/die; Alignment ±2µm @ 3σ; Ceramic heater head RT–450°C",
    "specs_zh": "基板 8″/12″；芯片 3–20mm；周期 2.0s/颗；对准 ±2µm @ 3σ；陶瓷加热头 RT–450°C",
    "notes_en": "[source note] Specification sheet from Toray Engineering; includes FC3000WS (R&D) / W / WL (full auto) variants",
    "notes_zh": "[source note] 挂牌信息转载 Toray 规格表；FC3000WS（半自动研发）/ W / WL（全自动）变体"
  },
  ("Toray Engineering", "UC5000"): {
    "specs_en": "Panel-level bonder; ±0.8µm accuracy; TCB on 515×510mm and 600×600mm (SEMI) panels, including glass substrates",
    "specs_zh": "面板级封装键合机；±0.8µm 精度；在 515×510mm 与 600×600mm（SEMI）面板上做 TCB，含玻璃面板",
    "notes_en": "[source note] Released April 2025; Engineered for AI server panel-level packaging",
    "notes_zh": "[source note] 2025 年 4 月发布；面向 AI 服务器 PLP"
  },

  # --- Bay 5: Molding (1 model) ---
  ("TOWA", "(型号未公开)"): {
    "specs_en": "Vendor confirmed product lines: Transfer molding (multi-plunger, fully automatic) and compression molding, including Flow Compression Molding (FCM) / Vacuum Compression; ~2/3 global market share in chip molding equipment",
    "specs_zh": "厂商确认的产品线：传递模塑（多柱塞、全自动）与压缩模塑，含流动压缩模塑（FCM）/ 真空压缩；约占全球芯片塑封设备 2/3 份额（行业报道口径）",
    "notes_en": "[source note] TOWA discloses technical specifications only, withholding explicit model names. Honest gap row.",
    "notes_zh": "[source note] TOWA 官网只公开技术说明、不公开型号命名——型号无法核实，本行即缺口标注"
  },

  # --- Bay 6: ATE Test (13 models) ---
  ("Advantest", "V93000 EXA Scale"): {
    "specs_en": "SoC test system; Pin Scale 5000: 256 channels/card @ 5Gb/s scan, deep vector memory; XPS256 DPS; Xtreme Link card-to-card interconnect",
    "specs_zh": "SoC 测试系统；Pin Scale 5000：256 通道/卡 @ 5Gb/s 扫描、深向量存储；XPS256 电源；Xtreme Link 卡间通信",
    "notes_en": "[source note] Flagship SoC test platform; broad backward compatibility across instrument generations",
    "notes_zh": "[source note] 旗舰 SoC 平台（2000 年推出）；跨代向后兼容"
  },
  ("Advantest", "T2000"): {
    "specs_en": "SoC test system; Up to 8,192 digital channels; Modular open architecture; Multi-site concurrent testing",
    "specs_zh": "SoC 测试系统；最高 8,192 数字通道；模块化仪器架构；并发测试",
    "notes_en": "[source note] T2000 AiR2X (2025): Air-cooled, 2x resources of AiR, up to 12 modules, automotive DC up to 320V",
    "notes_zh": "[source note] T2000 AiR2X（2025）：风冷、资源 2 倍于 AiR、最高 12 个测量模块、车载 DC 至 320V"
  },
  ("Advantest", "T5503HS2"): {
    "specs_en": "DRAM memory test system; High-speed parallel testing up to 8 Gbps for high-bandwidth memory and mobile DRAM",
    "specs_zh": "存储器测试系统（DRAM），Advantest 官方产品线在列",
    "notes_en": "[source note] Official Advantest memory line; related to T5833 and T5801 (GDDR7/LPDDR6/DDR6)",
    "notes_zh": "[source note] 同线还有 T5833 与 T5801（超高速 DRAM，GDDR7/LPDDR6/DDR6）"
  },
  ("Teradyne", "UltraFLEXplus"): {
    "specs_en": "SoC tester; UltraPort-PCIe6: 64Gb/s PAM4 × 32 channels; UltraPHY 224G (112Gb/s NRZ / 224Gb/s PAM4); UltraVS64-HP: 1,280A single instrument",
    "specs_zh": "SoC 测试机；UltraPort-PCIe6：64Gb/s PAM4 × 32 通道；UltraPHY 224G（112Gb/s NRZ / 224Gb/s PAM4）；UltraVS64-HP：单仪器 1,280A",
    "notes_en": "[source note] Built for advanced AI/HPC processors and cloud datacenter silicon; IG-XL operating software",
    "notes_zh": "[source note] 面向 AI/HPC SoC；IG-XL 软件"
  },
  ("Teradyne", "J750"): {
    "specs_en": "Low-cost microcontroller and digital/mixed-signal SoC tester family; Highly parallel multi-site testing",
    "specs_zh": "数字/混合信号 SoC 测试家族；多站点配置",
    "notes_en": "[source note] Teradyne official website listed as product family (>6,000 installed systems)",
    "notes_zh": "[source note] 官网以产品家族列示；未找到型号专属页"
  },
  ("Teradyne", "Magnum 7"): {
    "specs_en": "High-density NAND flash memory tester; Up to 18,432 I/O channels @ 5.28Gbps; Up to 1,024 devices in parallel",
    "specs_zh": "NAND 闪存测试机；最高 18,432 I/O 通道 @ 5.28Gbps；最高 1,024 颗并行",
    "notes_en": "[source note] Teradyne memory test systems portfolio for 3D NAND and mass storage",
    "notes_zh": "[source note] 泰瑞达 3D NAND 与大容量存储器测试系统"
  },
  ("Teradyne", "Magnum 7H"): {
    "specs_en": "Dedicated HBM memory tester; HBM3/3E and HBM4/4E up to 4.5Gbps; 9,216 digital pins + 2,560 DPS power pins",
    "specs_zh": "HBM 存储器测试机；HBM3/3E 与 HBM4/4E 最高 4.5Gbps；9,216 数字针 + 2,560 电源针",
    "notes_en": "[source note] Released in 2025; Tests Known Good Stacked Die (KGSD) and pre-stack HBM wafers",
    "notes_zh": "[source note] 2025 年发布；亦可测 KGSD / 预切割 HBM"
  },
  ("Teradyne", "Magnum E2"): {
    "specs_en": "Next-gen memory test system; LPDDR6/DDR6/GDDR7/NAND; NRZ/PAM3/PAM4 signaling; Up to 64 sites, 24.5K high-speed I/O pins",
    "specs_zh": "新一代存储器测试机；LPDDR6/DDR6/GDDR7/NAND；NRZ/PAM3/PAM4；最高 64 测试站点、24.5K 高速 I/O 针",
    "notes_en": "[source note] Announced September 2026; Features Near-DUT Test architecture",
    "notes_zh": "[source note] 2026 年 9 月发布；Near-DUT Test 架构"
  },
  ("Teradyne", "Magnum V"): {
    "specs_en": "Memory test system; Up to 20,480 digital channels @ 1600Mbps; Available in EV/SSV/GV configurations",
    "specs_zh": "存储器测试机；最高 20,480 数字通道 @ 1600Mbps；EV/SSV/GV 配置",
    "notes_en": "[source note] Covers eMMC, Toggle NAND, ONFI, and legacy LPDDR memory test",
    "notes_zh": "[source note] 覆盖 eMMC / Toggle NAND / ONFI / LPDDR2/3"
  },
  ("Teradyne", "ETS-364"): {
    "specs_en": "Analog/power discrete tester; DPU-16: 16 digital I/O @ 132MHz, 8M vector memory; HPU-100: ±100A; QMS 12/16-bit measurement",
    "specs_zh": "模拟/功率测试；DPU-16：16 路数字 I/O @ 132MHz、8M 向量；HPU-100：±100A；QMS 12/16 位仪表",
    "notes_en": "[source note] Automotive power and smart power IC testing",
    "notes_zh": "[source note] 车载/功率市场"
  },
  ("Cohu", "Diamondx"): {
    "specs_en": "Universal mixed-signal platform; RedDragon RF (5G NR FR1/FR2, Wi-Fi 6/6E/7); PD1x/PD2x display drivers; Multiwave mixed-signal; VI100 DPS",
    "specs_zh": "通用混合信号平台；RedDragon RF（5G NR FR1/FR2、Wi-Fi 6/6E/7）；PD1x/PD2x 显示驱动；Multiwave 混合信号；VI100",
    "notes_en": "[source note] Low-cost-of-test platform for mobile, automotive, and IoT",
    "notes_zh": "[source note] 低测试成本平台，面向 IoT/移动/汽车"
  },
  ("Cohu", "Diamondx DxV"): {
    "specs_en": "Desktop engineering ATE; 5 Diamondx-compatible slots; 192 digital channels; 6.4Gbps serial; <50 lbs, air-cooled",
    "specs_zh": "桌面/工程版 ATE；5 个 Diamondx 兼容槽位；192 通道数字；6.4Gbps 串行；<50 lbs、风冷",
    "notes_en": "[source note] First-silicon validation and low-volume pilot test",
    "notes_zh": "[source note] 硅片验证 / 初期量产"
  },
  ("Cohu", "PAx"): {
    "specs_en": "RF production tester for power amplifiers (PA) and front-end modules (FEM) across 5G, Wi-Fi 6, BT, and IoT",
    "specs_zh": "RF 测试机，面向功率放大器与前端模块（5G、Wi-Fi 6、BT、IoT）",
    "notes_en": "[source note] Leading test platform for RF PA and FEM devices (Cohu disclosure)",
    "notes_zh": "[source note] RF PA/FEM 系统市场领先（Cohu 口径）"
  },

  # --- Bay 7: Test Handler (9 models) ---
  ("Advantest", "M4872"): {
    "specs_en": "Pick-and-place SoC handler; Up to 15,000 UPH; Vision alignment; Active Thermal Control (ATC); Universal conversion kits",
    "specs_zh": "取放式 SoC 分选机；最高 15,000 UPH；视觉对位；主动热控（ATC）；通用换型套件",
    "notes_en": "[source note] 2kW Active Thermal Control option for high-power AI/HPC packages",
    "notes_zh": "[source note] ATC 2kW 选件面向 AI/HPC 封装"
  },
  ("Advantest", "M4841"): {
    "specs_en": "Up to 32 devices in parallel; Throughput up to 18,500 UPH; Dynamic temperature control",
    "specs_zh": "最高 32 颗并行测试；18,500 UPH",
    "notes_en": "[source note] Analyst product listings; M6242 memory handler (42,200 UPH) from same series",
    "notes_zh": "[source note] 经分析师产品列表；同源还列有 M6242 存储器分选机（42,200 UPH）"
  },
  ("Advantest", "HA1200"): {
    "specs_en": "Die-level test handler for V93000; Tests singulated/pre-packaged dies; ATC for 2.5D/3D AI/HPC chiplet devices",
    "specs_zh": "面向 V93000 的裸片级分选机；测试切割后/半组装芯片；ATC 面向 2.5D/3D AI/HPC 器件",
    "notes_en": "[source note] Mitigates yield loss in multi-chip advanced packaging",
    "notes_zh": "[source note] 降低多芯片封装的终测良率损失"
  },
  ("Cohu", "MT9510"): {
    "specs_en": "Pick-and-place test handler; DI-Core data intelligence suite; Tri-temp capability up to +175°C",
    "specs_zh": "取放式测试分选机；DI-Core 数据智能；最高 +175°C",
    "notes_en": "[source note] Supports MEMS sensor and automotive test applications",
    "notes_zh": "[source note] 支持 MEMS"
  },
  ("Cohu", "Ismeca NY32"): {
    "specs_en": "32-station turret platform integrating test, optical inspection, and taping/packaging; NV-Core vision inspection",
    "specs_zh": "32 工位转塔平台，集测试/检测/封装；NV-Core 视觉选件",
    "notes_en": "[source note] NY32W variant for wafer-level packaging on film frames; NY20 variant has 20 stations",
    "notes_zh": "[source note] NY32W 变体面向薄膜框架晶圆介质（WLP）；NY20 为 20 工位"
  },
  ("Cohu", "Delta mTRiX"): {
    "specs_en": "Pick-and-place handler; 16,000 UPH; Up to ×32 test sites; Packages 3×3–51×51mm; Chamberless Active Thermal Control",
    "specs_zh": "取放式分选机；16,000 UPH；最高 ×32 站点；封装 3×3–51×51mm；无腔体 ATC",
    "notes_en": "[source note] Cohu technical datasheet (distributor hosted)",
    "notes_zh": "[source note] 经销商托管的 Cohu 手册"
  },
  ("Chroma", "3180"): {
    "specs_en": "Octal-site final test handler; Up to 9,000 UPH; Packages 3×3–50×50mm; Ambient to 150°C; Auto-retest and retry logic",
    "specs_zh": "八站点终测分选机；最高 9,000 UPH；封装 3×3–50×50mm；常温–150°C；自动复测/重试",
    "notes_en": "[source note] Chroma official brochure (distributor hosted)",
    "notes_zh": "[source note] 经销商托管的 Chroma 手册"
  },
  ("Chroma", "3210"): {
    "specs_en": "Single-site System-Level Test (SLT) handler; Devices 2×2–120×120mm; -40°C to 150°C; Thermal dissipation up to 2.9kW",
    "specs_zh": "单站点 SLT 分选机；器件 2×2–120×120mm；-40–150°C；最高 2.9kW 热耗散",
    "notes_en": "[source note] Chroma official datasheet; compact engineering and SLT test handler",
    "notes_zh": "[source note] Chroma 官方手册；紧凑型工程分选机"
  },
  ("Hontech", "HT-9040S"): {
    "specs_en": "Pick-and-place handler with robotic vision; ATE docking interface; ISO cleanroom compatible",
    "specs_zh": "带视觉机器人的分选机；可集成 ATE；洁净室兼容",
    "notes_en": "[source note] Product existence verified via industrial directory",
    "notes_zh": "[source note] 仅确认存在；详细规格未核实"
  },

  # --- Bay 8: Wafer Prober (8 models) ---
  ("Tokyo Seimitsu (Accretech)", "UF2000"): {
    "specs_en": "High-precision 300mm wafer prober; Flagship model in ACCRETECH product guide",
    "specs_zh": "高精度 300mm 晶圆探针机；指南中的旗舰型号",
    "notes_en": "[source note] ACCRETECH product guide; UF200R / UF190R variants also listed",
    "notes_zh": "[source note] 另有 UF200R / UF190R 变体"
  },
  ("Tokyo Seimitsu (Accretech)", "AP3000"): {
    "specs_en": "Flagship 300mm prober; High-rigidity stage supporting heavy test heads and Panel-Level Packaging (PLP)",
    "specs_zh": "旗舰 300mm 探针机；大测试头 + PLP 支持",
    "notes_en": "[source note] Official catalog; AP3000W/e/eW variants supported",
    "notes_zh": "[source note] AP3000W/e/eW 变体在列"
  },
  ("Tokyo Seimitsu (Accretech)", "FP3000W"): {
    "specs_en": "Prober for diced wafer ring frames; Inspects CSP, WLP, and PLP devices mounted on dicing film",
    "specs_zh": "支持固定在切割框架上的 CSP/WLP/PLP 器件",
    "notes_en": "[source note] ACCRETECH guide; FP2000 (200mm) also listed",
    "notes_zh": "[source note] FP2000（200mm）亦在列"
  },
  ("FormFactor", "CM300xi"): {
    "specs_en": "Semi/fully-automated 300mm probe station; X-Y stage accuracy ≤10µm; 305mm PureLine chuck",
    "specs_zh": "半自动/全自动 300mm 探针系统；X-Y 精度 ≤10µm；305mm 卡盘",
    "notes_en": "[source note] FormFactor datasheet; Ultra-Low Noise (ULN) and Silicon Photonics variants",
    "notes_zh": "[source note] 有 ULN（超低噪声）与 SiPh 变体"
  },
  ("FormFactor", "SUMMIT200"): {
    "specs_en": "200mm semi-automatic and fully-automated probe station for precision device characterization",
    "specs_zh": "200mm 半自动/全自动探针系统",
    "notes_en": "[source note] FormFactor official product portfolio",
    "notes_zh": "[source note] 官网产品线在列"
  },
  ("FormFactor", "TESLA300"): {
    "specs_en": "300mm high-power on-wafer characterization probe system; Rated up to 10kV / 600A",
    "specs_zh": "300mm 晶圆上功率器件表征系统",
    "notes_en": "[source note] FormFactor high-power semiconductor test line",
    "notes_zh": "[source note] 官网产品线在列"
  },
  ("MPI", "TS3000"): {
    "specs_en": "Automated probe system; 310mm chuck; Planarity ±5µm; X-Y accuracy ≤5µm; Film frame probe support",
    "specs_zh": "自动探针系统；310mm 卡盘；平面度 ±5µm；X-Y 精度 ≤5µm；支持薄膜框架探测",
    "notes_en": "[source note] MPI official datasheet; TS3000-IFE thermal variant: -60°C to +300°C",
    "notes_zh": "[source note] TS3000-IFE 变体：-60 至 +300°C"
  },
  ("MPI", "TS300"): {
    "specs_en": "Manual 300mm probe system for DC, CV, and RF device testing; 330×395mm X-Y stage travel",
    "specs_zh": "手动探针系统，面向 DC/CV/RF；330×395mm XY 行程",
    "notes_en": "[source note] MPI Corporation official datasheet",
    "notes_zh": "[source note] 官方数据表"
  },

  # --- Bay 9: Inspection & Metrology (15 models) ---
  ("Camtek", "EagleT-i"): {
    "specs_en": "2D defect inspection; Detects surface defects down to 0.2µm; Fan-out RDL down to 2µm; Handles warped wafers and panels",
    "specs_zh": "2D 检测；可检出小至 0.2µm 表面缺陷；扇出 RDL 至 2µm；面板 + 翘曲晶圆处理",
    "notes_en": "[source note] Camtek official product brochure",
    "notes_zh": "[source note] 康特克官方产品说明书"
  },
  ("Camtek", "EagleT-i Plus"): {
    "specs_en": "Leading-edge 2D inspection; Brightfield 0.42µm / Darkfield 0.3µm sensitivity; Post-dicing subsurface crack inspection",
    "specs_zh": "领先 2D 检测；明场 0.42µm / 暗场 0.3µm 灵敏度；切割后内裂纹检测",
    "notes_en": "[source note] Camtek inspection systems datasheet",
    "notes_zh": "[source note] 康特克晶圆检测系统说明书"
  },
  ("Camtek", "Eagle-AP"): {
    "specs_en": "Integrated 2D and 3D inspection & metrology on a single platform for advanced packaging and micro-bumps",
    "specs_zh": "单一平台集成 2D + 3D 量测与检测",
    "notes_en": "[source note] Widely deployed across Tier-1 OSATs (Camtek disclosure)",
    "notes_zh": "[source note] 被头部 OSAT 采用（Camtek 口径）"
  },
  ("Camtek", "Golden Eagle"): {
    "specs_en": "Panel-level defect inspection and metrology; Accommodates panels up to 650×650mm",
    "specs_zh": "面板检测与量测；标准面板最大 650×650mm",
    "notes_en": "[source note] Dedicated for Fan-Out Panel-Level Packaging (FO-PLP)",
    "notes_zh": "[source note] FO-PLP 应用"
  },
  ("Camtek", "Hawk"): {
    "specs_en": "Next-gen advanced packaging inspection; HBM, chiplets, and hybrid bonding; Inspects wafers with >500 million micro-bumps",
    "specs_zh": "先进封装平台；HBM/芯粒/混合键合；可检测带 5 亿微凸点的晶圆",
    "notes_en": "[source note] Debuted at SEMICON Korea February 2025; product page on camtek.com",
    "notes_zh": "[source note] SEMICON Korea 2025 年 2 月发布；camtek.com 有官方产品页"
  },
  ("KLA", "ICOS T890"): {
    "specs_en": "Packaged IC and diced substrate inspection/metrology; 6-sided automated visual inspection (AVI); 3D metrology; 4 parallel inspection stations",
    "specs_zh": "封装 IC + 切割后基板检测/量测；六面 AVI；3D 量测；4 个并行检测工位",
    "notes_en": "[source note] Broad package coverage: BGA, CSP, WLP, QFN, LGA, and QFP",
    "notes_zh": "[source note] 覆盖 TQFP/QFP/BGA/CSP/WLP/QFN/BCC/LGA"
  },
  ("KLA", "ICOS T3/T7"): {
    "specs_en": "Outgoing quality control (OQC) for packaged ICs; JEDEC tray (T3) or tape-and-reel (T7) output; AI deep learning defect binning; 3D metrology",
    "specs_zh": "封装 IC 出厂质检（OQC）；托盘（T3）/ 编带（T7）输出；AI 深度学习分选；3D 量测",
    "notes_en": "[source note] Reconfigurable output between tray and tape-and-reel",
    "notes_zh": "[source note] 托盘↔编带可重构"
  },
  ("KLA", "ICOS F160XP"): {
    "specs_en": "Post-dicing inspection and die sorting; IR2.0 module (optical + true IR sidewall inspection); Detects laser grooves, hairline cracks, and sidewall defects",
    "specs_zh": "切割后检测 + 芯片分选；IR2.0 模块（光学 + 真红外侧面检测）；激光开槽/发丝裂纹/侧壁裂纹检测",
    "notes_en": "[source note] KLA packaging metrology suite; F260 variant also available",
    "notes_zh": "[source note] 另有 F260 变体"
  },
  ("KLA", "Kronos 1190"): {
    "specs_en": "Wafer-level packaging defect inspection; High-resolution optics; Powered by AI DefectWise machine learning",
    "specs_zh": "晶圆级封装检测；高分辨率光学；AI DefectWise",
    "notes_en": "[source note] KLA advanced packaging portfolio announcement",
    "notes_zh": "[source note] KLA 先进封装产品组合公告"
  },
  ("Onto Innovation", "Dragonfly G3"): {
    "specs_en": "Sub-micron 2D inspection (Brightfield/Darkfield/Clearfind); LT-200 dual-head 3D metrology (+50% bump throughput); +30% scan speed",
    "specs_zh": "亚微米 2D 检测（明场/暗场/Clearfind）；LT-200 双头 3D 量测（凸点产能 +50%）；扫描速度 +30%",
    "notes_en": "[source note] Onto Innovation product sheet; Dragonfly G5 is subsequent generation",
    "notes_zh": "[source note] Dragonfly G5 为更新一代"
  },
  ("Onto Innovation", "Firefly G5"): {
    "specs_en": "Sub-micron 2D inspection + 3D metrology for advanced IC substrates and panel-level packaging",
    "specs_zh": "亚微米 2D 检测 + 3D 量测，面向 IC 基板与面板级封装",
    "notes_en": "[source note] Onto Innovation IC substrate line; related to NovusEdge G2",
    "notes_zh": "[source note] 同线还有 NovusEdge G2（边缘/缺口/背面）"
  },
  ("Nordson (CyberOptics)", "SQ7000+"): {
    "specs_en": "3D AOI inspection system powered by Multi-Reflection Suppression (MRS) sensor; AI-driven defect filtering for advanced packaging",
    "specs_zh": "带 MRS 传感器的 3D AOI，面向先进封装；AI 驱动",
    "notes_en": "[source note] Exhibited at SEMICON West; sister model SQ3000 M2 for wire bond AOI",
    "notes_zh": "[source note] SEMICON West 2026 展出；同展 SQ3000 M2（焊线检测）"
  },
  ("Nordson (CyberOptics)", "MX3000"): {
    "specs_en": "3D final inspection system for high-density memory modules; Sub-10µm resolution; Dual MRS sensors",
    "specs_zh": "存储模组 3D 终检视觉系统；亚 10µm 分辨率；双 MRS 传感器",
    "notes_en": "[source note] Nordson official brochure (distributor hosted)",
    "notes_zh": "[source note] Nordson 手册（经销商挂牌）"
  },
  ("Viscom", "X7056-II"): {
    "specs_en": "Inline 3D AXI (60–130kV sealed microfocus tube; 6–32µm/pixel) + 3D AOI (Z-resolution 0.5µm); Cycle times down to 4s",
    "specs_zh": "在线 3D AXI（60–130kV 密封管；6–32µm/像素）+ 3D AOI（Z 分辨率 0.5µm）；处理至 4s",
    "notes_en": "[source note] Official datasheet; X7056-II BO variant combines wire bond AOI and AXI",
    "notes_zh": "[source note] 官方手册；X7056-II BO 变体 = 焊线 AOI + 焊线 AXI"
  },
  ("Viscom", "iX7059"): {
    "specs_en": "Heavy-duty inline 3D automated X-ray inspection (AXI) with computed tomography (CT) for heavy PCBAs and power modules",
    "specs_zh": "重型 3D 在线 AXI 带 CT，面向大型/重型板、功率电子、储能",
    "notes_en": "[source note] Viscom high-end X-ray inspection catalog",
    "notes_zh": "[source note] 德国 Viscom 高端工业 X 射线在线检测系统"
  },

  # --- Bay 10: Bumping & RDL (3 models) ---
  ("ACM Research", "Ultra ECP ap-p"): {
    "specs_en": "Horizontal panel electroplating system; Cu pillar >300µm; 4-edge sealed dry contact chuck; Rotating square electric field",
    "specs_zh": "水平面板电镀设备；铜柱 >300µm；四边密封干接触卡盘；旋转方形电场",
    "notes_en": "[source note] World's first commercial horizontal panel electroplating system; shipped November 2025",
    "notes_zh": "[source note] 首台商用水平面板电镀设备；2025 年 11 月出货"
  },
  ("Ultratech (Veeco)", "AP300"): {
    "specs_en": "Lithography stepper for Fan-Out Wafer-Level Packaging (FOWLP); Corrects die shift, wafer warpage, and topography",
    "specs_zh": "扇出晶圆级封装光刻步进机；处理芯片偏移/翘曲/不平整",
    "notes_en": "[source note] Multiple volume production follow-on orders for advanced packaging",
    "notes_zh": "[source note] FOWLP 量产多台复购订单"
  },
  ("Shibaura Mechatronics", "SWN-5000"): {
    "specs_en": "Sputtering system; Backside metallization for power devices and under-bump metallization (UBM); Multi-layer thin film",
    "specs_zh": "溅射设备；功率器件背面电极镀膜 / 凸点下金属层（UBM）；多层膜",
    "notes_en": "[source note] Shibaura sputtering portfolio; related to BM-1400W sputtering model",
    "notes_zh": "[source note] 同线还有 BM-1400W 溅射型号"
  },

  # --- Bay 11: Singulation (1 model) ---
  ("TOWA", "LSG1040"): {
    "specs_en": "Next-gen laser singulation system; High-speed non-contact dry dicing; Linear and complex contoured profile cutting",
    "specs_zh": "新一代激光切割；高速非接触干法工艺；直线 + 曲线/复杂形状切割",
    "notes_en": "[source note] TOWA singulation line; mechanical blade singulation also offered",
    "notes_zh": "[source note] TOWA 亦提供刀片切割（所查页面未公开型号）"
  }
}

def main():
    print(f"Total bilingual entries defined: {len(OSAT_BILINGUAL_MAP)}")

    # 1. Update data/osat-86-ground-truth.json
    with open("data/osat-86-ground-truth.json", "r", encoding="utf-8") as f:
        ground_truth = json.load(f)

    for item in ground_truth:
        key = (item["vendor"], item["model"])
        if key in OSAT_BILINGUAL_MAP:
            m = OSAT_BILINGUAL_MAP[key]
            item["key_specs_zh"] = m["specs_zh"]
            item["key_specs_en"] = m["specs_en"]
            item["notes_zh"] = m["notes_zh"]
            item["notes_en"] = m["notes_en"]
        else:
            print(f"WARNING: Missing mapping for ground truth {key}")

    with open("data/osat-86-ground-truth.json", "w", encoding="utf-8") as f:
        json.dump(ground_truth, f, indent=2, ensure_ascii=False)
    print("Updated data/osat-86-ground-truth.json with bilingual fields.")

    # 2. Update twin-osat.html embedded catalog data and script logic
    with open("twin-osat.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Extract embedded JSON in twin-osat.html
    m = re.search(r'(<script id="osat-catalog-data"[^>]*>)([\s\S]*?)(</script>)', html)
    if not m:
        raise ValueError("Could not find <script id=\"osat-catalog-data\"> in twin-osat.html")

    prefix, json_str, suffix = m.group(1), m.group(2), m.group(3)
    osat_records = json.loads(json_str)

    matched_count = 0
    for item in osat_records:
        key = (item["vendor"], item["model"])
        if key in OSAT_BILINGUAL_MAP:
            b = OSAT_BILINGUAL_MAP[key]
            item["key_specs_zh"] = b["specs_zh"]
            item["key_specs_en"] = b["specs_en"]
            item["notes_zh"] = b["notes_zh"]
            item["notes_en"] = b["notes_en"]
            matched_count += 1
        else:
            print(f"WARNING: Missing mapping for embedded item {key}")

    print(f"Matched {matched_count}/{len(osat_records)} records in twin-osat.html")
    new_json_str = json.dumps(osat_records, ensure_ascii=False)
    html = html[:m.start()] + prefix + new_json_str + suffix + html[m.end():]

    with open("twin-osat.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Saved updated embedded data in twin-osat.html.")

    # 3. Update catalog.json
    with open("catalog.json", "r", encoding="utf-8") as f:
        catalog_all = json.load(f)

    catalog_updated = 0
    for item in catalog_all:
        key = (item["vendor"], item["model"])
        if key in OSAT_BILINGUAL_MAP:
            b = OSAT_BILINGUAL_MAP[key]
            item["key_specs_zh"] = b["specs_zh"]
            item["key_specs_en"] = b["specs_en"]
            item["notes_zh"] = b["notes_zh"]
            item["notes_en"] = b["notes_en"]
            # Standardize record to English notes and specs to match other 167 tools
            if "record" in item and isinstance(item["record"], dict):
                item["record"]["notes"] = b["notes_en"]
                caps = item["record"].get("process_capability", {}).get("capabilities", [])
                if caps and isinstance(caps, list):
                    caps[0]["detail"]["value"] = b["specs_en"]
            catalog_updated += 1

    with open("catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog_all, f, indent=2, ensure_ascii=False)
    print(f"Updated {catalog_updated} OSAT items in catalog.json.")

    # 4. Update embedded-catalog-data in catalog-demo.html
    with open("catalog-demo.html", "r", encoding="utf-8") as f:
        demo_html = f.read()

    m_demo = re.search(r'(<script id="embedded-catalog-data"[^>]*>)([\s\S]*?)(</script>)', demo_html)
    if m_demo:
        prefix_d, _, suffix_d = m_demo.group(1), m_demo.group(2), m_demo.group(3)
        demo_json_str = "\n" + json.dumps(catalog_all, ensure_ascii=False, indent=2) + "\n    "
        demo_html = demo_html[:m_demo.start()] + prefix_d + demo_json_str + suffix_d + demo_html[m_demo.end():]
        with open("catalog-demo.html", "w", encoding="utf-8") as f:
            f.write(demo_html)
        print("Synchronized catalog-demo.html embedded catalog data.")

if __name__ == "__main__":
    main()
