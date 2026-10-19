with open("js/translations.js", "r", encoding="utf-8") as f:
    content = f.read()

en_keys = '''    cat_osat_dicing: "OSAT Dicing",
    cat_osat_die_attach: "OSAT Die Attach",
    cat_osat_wire_bonding: "OSAT Wire Bonding",
    cat_osat_flip_chip: "OSAT Flip Chip",
    cat_osat_molding: "OSAT Molding",
    cat_osat_singulation: "OSAT Singulation",
    cat_osat_bumping_rdl: "OSAT Bumping/RDL",
    cat_osat_prober: "OSAT Prober",
    cat_osat_ate: "OSAT ATE",
    cat_osat_test_handler: "OSAT Test Handler",
    cat_osat_inspection: "OSAT Inspection",
    osat_building_title: "OSAT Back-End · 封测工厂",
    osat_building_subtitle: "从硅片到芯片出货 · From Wafer to Shipment",
    osat_building_desc: "Dedicated standalone facility covering the complete back-end process flow: Dicing → Die Attach → Wire Bonding → Flip Chip → Molding → Singulation → Bumping/RDL → Prober → ATE → Test Handler → Inspection.",
    osat_badge_draft: "Draft Shell · Dimensions Pending Verification",
    osat_banner_honesty: "Dimensions pending verification · 3D scene displays a procedural category placeholder shell without physical CAD measurements.",
    osat_cta_contribute: "+ Contribute Verified Equipment Specs (Add Equipment) →",
    osat_gap_towa: "TOWA officially discloses process technologies and technical features without publishing specific model numbers — model unverified, cataloged as gap row.",'''

zh_keys = '''    cat_osat_dicing: "封测划片",
    cat_osat_die_attach: "封测固晶",
    cat_osat_wire_bonding: "引线键合",
    cat_osat_flip_chip: "倒装焊接",
    cat_osat_molding: "塑封成型",
    cat_osat_singulation: "切割分离",
    cat_osat_bumping_rdl: "凸块/RDL",
    cat_osat_prober: "探针电测",
    cat_osat_ate: "测试机ATE",
    cat_osat_test_handler: "分选机群",
    cat_osat_inspection: "出厂检测",
    osat_building_title: "OSAT Back-End · 封测工厂",
    osat_building_subtitle: "从硅片到芯片出货 · From Wafer to Shipment",
    osat_building_desc: "后道封测专属独立厂房，覆盖完整后道流程：划片 → 贴片 → 键合 → 倒装 → 塑封 → 分离 → 凸块/RDL → 探针 → ATE → 分选 → 检测。",
    osat_badge_draft: "Draft Shell · 尺寸待实测",
    osat_banner_honesty: "尺寸待实测 · 3D 场景展示为类别通用概念占位外形，物理包络尺寸未经实测核实。",
    osat_cta_contribute: "+ 补充实测机台参数 (Add Equipment) →",
    osat_gap_towa: "TOWA 官网只公开技术说明、不公开型号命名——型号无法核实，本行即缺口标注。",'''

zh_tw_keys = '''    cat_osat_dicing: "封測切割",
    cat_osat_die_attach: "封測固晶",
    cat_osat_wire_bonding: "打線鍵合",
    cat_osat_flip_chip: "覆晶焊接",
    cat_osat_molding: "模壓封裝",
    cat_osat_singulation: "切割分離",
    cat_osat_bumping_rdl: "凸塊/RDL",
    cat_osat_prober: "探針電測",
    cat_osat_ate: "測試機ATE",
    cat_osat_test_handler: "分選機群",
    cat_osat_inspection: "出廠檢測",
    osat_building_title: "OSAT Back-End · 封測工廠",
    osat_building_subtitle: "從矽片到晶片出貨 · From Wafer to Shipment",
    osat_building_desc: "後段封測專屬獨立廠房，覆蓋完整後段流程：劃片 → 貼片 → 鍵合 → 覆晶 → 模壓 → 分離 → 凸塊/RDL → 探針 → ATE → 分選 → 檢測。",
    osat_badge_draft: "Draft Shell · 尺寸待實測",
    osat_banner_honesty: "尺寸待實測 · 3D 場景展示為類別通用概念占位外形，物理包絡尺寸未經實測核實。",
    osat_cta_contribute: "+ 補充實測機台參數 (Add Equipment) →",
    osat_gap_towa: "TOWA 官網只公開技術說明、不公開型號命名——型號無法核實，本行即缺口標註。",'''

# Insert in en
target_en = '    cat_pkg: "Packaging/Test",'
if target_en in content and "cat_osat_dicing" not in content:
    content = content.replace(target_en, target_en + "\n" + en_keys, 1)

# Insert in zh-CN
target_zh = '    cat_pkg: "后道封测",'
if target_zh in content and "cat_osat_dicing: \"封测划片\"" not in content:
    content = content.replace(target_zh, target_zh + "\n" + zh_keys, 1)

# Insert in zh-TW
target_zhtw = '    cat_pkg: "後段封測",'
if target_zhtw in content and "cat_osat_dicing: \"封測切割\"" not in content:
    content = content.replace(target_zhtw, target_zhtw + "\n" + zh_tw_keys, 1)

with open("js/translations.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated js/translations.js")
