#!/usr/bin/env python3
"""
verify_estimates.py
Validates Acceptance Criteria for price_estimates.json
"""

import json
import os
import urllib.request

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "price_estimates.json")
CATALOG_PATH = os.path.join(os.path.dirname(__file__), "..", "catalog.json")

def verify():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        estimates = json.load(f)

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog_list = json.load(f)
        catalog = {d["record_id"]: d for d in catalog_list}

    total_catalog = len(catalog_list)
    assert total_catalog == 167, f"Catalog size must be 167, got {total_catalog}"

    valid_count = 0
    reported_items = []
    category_estimate_items = []
    unknown_items = []

    for rid, cat_rec in catalog.items():
        assert rid in estimates, f"Record ID {rid} missing from price_estimates.json"
        est = estimates[rid]

        # Field validation
        assert "low_usd" in est
        assert "high_usd" in est
        assert "condition" in est
        assert "basis" in est
        assert "as_of" in est
        assert "source_url" in est
        assert "note" in est

        assert est["basis"] in ("observed_listing", "reported", "category_estimate", "unknown"), f"Invalid basis {est['basis']}"
        assert est["condition"] in ("new", "used", "refurbished"), f"Invalid condition {est['condition']}"

        if est["basis"] in ("observed_listing", "reported"):
            assert est["source_url"].startswith("http"), f"Reported item {rid} has no valid http URL: {est['source_url']}"
            assert est["low_usd"] is not None and est["low_usd"] > 0
            assert est["high_usd"] is not None and est["high_usd"] >= est["low_usd"]
            reported_items.append((rid, cat_rec, est))
            valid_count += 1
        elif est["basis"] == "category_estimate":
            assert est["low_usd"] is not None and est["low_usd"] > 0
            assert est["high_usd"] is not None and est["high_usd"] >= est["low_usd"]
            assert len(est["note"]) > 10, f"Category estimate {rid} missing informative note"
            category_estimate_items.append((rid, cat_rec, est))
            valid_count += 1
        else:
            unknown_items.append((rid, cat_rec, est))

    print(f"==================================================")
    print(f"AC-1 Verification Results:")
    print(f"Total catalog records: {total_catalog}")
    print(f"Valid price estimates: {valid_count} (>=134 target: {'PASS' if valid_count >= 134 else 'FAIL'})")
    print(f"Coverage percentage: {valid_count / total_catalog * 100:.1f}%")
    print(f"Reported items: {len(reported_items)}")
    print(f"Category estimate items: {len(category_estimate_items)}")
    print(f"Unknown items: {len(unknown_items)}")
    print(f"==================================================")

    print("\n[Sample 10 Reported/Observed Items]:")
    for i, (rid, rec, est) in enumerate(reported_items[:10]):
        v = rec.get("vendor")
        m = rec.get("model")
        cat = rec.get("category")
        low = est["low_usd"]
        high = est["high_usd"]
        print(f"#{i+1}: {v} {m} [{cat}]")
        print(f"   Record ID: {rid}")
        print(f"   Range: ${low:,} - ${high:,} USD ({est['condition']})")
        print(f"   Basis: {est['basis']}")
        print(f"   Source URL: {est['source_url']}")
        print(f"   Note: {est['note']}\n")

if __name__ == "__main__":
    verify()
