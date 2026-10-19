#!/usr/bin/env python3
"""
generate_bom_data.py
Aggregates twin/layout-default.json tools with data/price_estimates.json
into cleanroom BOM groups for fab-capex.html.
"""

import json
from collections import defaultdict

with open("twin/layout-default.json") as f:
    layout = json.load(f)

with open("data/price_estimates.json") as f:
    estimates = json.load(f)

with open("catalog.json") as f:
    catalog = {d["record_id"]: d for d in json.load(f)}

tools = layout.get("tools", [])

bom_map = {}

for t in tools:
    tid = t["tool_id"]
    est = estimates.get(tid, {})
    cat_rec = catalog.get(tid, {})

    key = (t["vendor"], t["model"], t["category"])
    if key not in bom_map:
        bom_map[key] = {
            "tool_id": tid,
            "vendor": t["vendor"],
            "model": t["model"],
            "category": t["category"],
            "bay": t["bay"],
            "count": 0,
            "low_usd": est.get("low_usd") or 0,
            "high_usd": est.get("high_usd") or 0,
            "condition": est.get("condition") or "new",
            "basis": est.get("basis") or "category_estimate",
            "source_url": est.get("source_url") or "",
            "note": est.get("note") or "",
            "conformance_level": cat_rec.get("conformance_level") or "draft",
            "positions": []
        }
    bom_map[key]["count"] += 1
    bom_map[key]["positions"].append({"x": t["x"], "z": t["z"]})

bom_list = list(bom_map.values())
# Sort by median subtotal descending
bom_list.sort(key=lambda x: ((x["low_usd"] + x["high_usd"]) / 2) * x["count"], reverse=True)

print(f"Total individual tools in cleanroom layout: {len(tools)}")
print(f"Aggregated unique BOM items: {len(bom_list)}")

with open("data/twin_bom_costs.json", "w", encoding="utf-8") as f:
    json.dump(bom_list, f, indent=2, ensure_ascii=False)

print("Saved aggregated BOM costs to data/twin_bom_costs.json")
