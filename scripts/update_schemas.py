import json

osat_cats = [
    "osat_dicing",
    "osat_die_attach",
    "osat_wire_bonding",
    "osat_flip_chip",
    "osat_molding",
    "osat_singulation",
    "osat_bumping_rdl",
    "osat_prober",
    "osat_ate",
    "osat_test_handler",
    "osat_inspection"
]

for p in ["schema.json", "tools/validator/schemavalidator/schema.json"]:
    with open(p, "r", encoding="utf-8") as f:
        s = json.load(f)
    cur_enum = s["$defs"]["categoryEnum"]["enum"]
    for c in osat_cats:
        if c not in cur_enum:
            cur_enum.append(c)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(s, f, indent=2, ensure_ascii=False)
    print(f"Updated {p}")

layout_schema_path = "twin/layout-schema.json"
with open(layout_schema_path, "r", encoding="utf-8") as f:
    ls = json.load(f)
bay_enum = ls["properties"]["tools"]["items"]["properties"]["bay"]["enum"]
for c in osat_cats:
    if c not in bay_enum:
        bay_enum.append(c)
with open(layout_schema_path, "w", encoding="utf-8") as f:
    json.dump(ls, f, indent=2, ensure_ascii=False)
print("Updated twin/layout-schema.json")
