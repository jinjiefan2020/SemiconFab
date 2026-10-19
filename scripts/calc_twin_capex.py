import json
from collections import defaultdict

with open("twin/layout-default.json") as f:
    layout = json.load(f)

with open("data/price_estimates.json") as f:
    estimates = json.load(f)

tools = layout.get("tools", [])
print(f"Total tools in twin cleanroom layout: {len(tools)}")

missing_estimates = []
total_low = 0
total_high = 0
total_median = 0
cat_totals = defaultdict(lambda: {"low": 0, "median": 0, "high": 0, "count": 0})
unique_models = defaultdict(lambda: {"count": 0, "sample": None})

for t in tools:
    tid = t["tool_id"]
    est = estimates.get(tid)
    if not est:
        missing_estimates.append(t)
        continue
    low = est["low_usd"] or 0
    high = est["high_usd"] or 0
    med = (low + high) / 2
    total_low += low
    total_high += high
    total_median += med

    cat = t.get("category", "other")
    cat_totals[cat]["low"] += low
    cat_totals[cat]["median"] += med
    cat_totals[cat]["high"] += high
    cat_totals[cat]["count"] += 1

    key = (t["vendor"], t["model"], t["category"])
    unique_models[key]["count"] += 1
    unique_models[key]["sample"] = (t, est)

print(f"Missing estimates: {len(missing_estimates)}")
print(f"Twin WFE Total Low:    ${total_low:,.0f} (~${total_low/1e9:.2f}B)")
print(f"Twin WFE Total Median: ${total_median:,.0f} (~${total_median/1e9:.2f}B)")
print(f"Twin WFE Total High:   ${total_high:,.0f} (~${total_high/1e9:.2f}B)")

print(f"\nUnique Tool Models in Layout: {len(unique_models)}")
print("\nCategory Breakdown in Twin Layout:")
for cat, data in sorted(cat_totals.items(), key=lambda x: x[1]["median"], reverse=True):
    share = (data["median"] / total_median) * 100
    print(f"  {cat:22}: {data['count']:2d} tools | ${data['median']/1e6:7.1f}M ({share:5.1f}%) | Range: ${data['low']/1e6:6.1f}M - ${data['high']/1e6:6.1f}M")
