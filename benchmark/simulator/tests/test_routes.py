import json
from pathlib import Path
from collections import Counter

TABLE2 = {
    "A": {
        "TG01_LITHO": 28, "TG02_TRACK": 28, "TG03_ETCH": 16, "TG04_STRIP": 6,
        "TG05_CVD": 8, "TG06_PVD": 4, "TG07_FURN_DIFF": 2, "TG08_FURN_LPCVD": 2,
        "TG09_IMPL_MED": 3, "TG10_IMPL_HIGH": 2, "TG11_CMP_OX": 3, "TG12_CMP_MET": 3,
        "TG13_WET_BENCH": 2, "TG14_WET_SINGLE": 4, "TG15_RTP": 2, "TG16_MET_CD": 3,
        "TG17_MET_THICK": 2, "TG18_INSPECT": 2
    },
    "B": {
        "TG01_LITHO": 24, "TG02_TRACK": 24, "TG03_ETCH": 14, "TG04_STRIP": 5,
        "TG05_CVD": 7, "TG06_PVD": 3, "TG07_FURN_DIFF": 2, "TG08_FURN_LPCVD": 2,
        "TG09_IMPL_MED": 2, "TG10_IMPL_HIGH": 2, "TG11_CMP_OX": 3, "TG12_CMP_MET": 2,
        "TG13_WET_BENCH": 2, "TG14_WET_SINGLE": 3, "TG15_RTP": 2, "TG16_MET_CD": 3,
        "TG17_MET_THICK": 2, "TG18_INSPECT": 2
    },
    "C": {
        "TG01_LITHO": 20, "TG02_TRACK": 20, "TG03_ETCH": 12, "TG04_STRIP": 5,
        "TG05_CVD": 7, "TG06_PVD": 3, "TG07_FURN_DIFF": 2, "TG08_FURN_LPCVD": 2,
        "TG09_IMPL_MED": 2, "TG10_IMPL_HIGH": 2, "TG11_CMP_OX": 2, "TG12_CMP_MET": 2,
        "TG13_WET_BENCH": 2, "TG14_WET_SINGLE": 3, "TG15_RTP": 2, "TG16_MET_CD": 2,
        "TG17_MET_THICK": 2, "TG18_INSPECT": 2
    }
}

VALID_18_TGS = set(TABLE2["A"].keys())
BATCH_TGS = {"TG07_FURN_DIFF", "TG08_FURN_LPCVD", "TG13_WET_BENCH"}

def test_routes_constraints():
    candidates = [
        Path(__file__).parent.parent / "routes.json",
        Path(__file__).parent.parent.parent / "routes.json",
        Path(__file__).parent.parent / "../routes.json",
        Path("benchmark/routes.json"),
    ]
    routes_file = next((p for p in candidates if p.exists()), candidates[0])
    assert routes_file.exists(), f"routes.json missing at {routes_file}"
    with open(routes_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    prods = data["products"]
    
    # C1 & C2
    for p_id, exp_len in [("A", 120), ("B", 104), ("C", 92)]:
        route = prods[p_id]["route"]
        assert len(route) == exp_len, f"C1 violation on {p_id}"
        counts = Counter(s["tool_group"] for s in route)
        assert counts == TABLE2[p_id], f"C2 violation on {p_id}"
        
        # C4 valid tool groups
        for s in route:
            assert s["tool_group"] in VALID_18_TGS, f"C4 invalid tg: {s['tool_group']}"
            
        # C5 batch recipes
        for s in route:
            if s["tool_group"] in BATCH_TGS:
                assert s.get("recipe"), f"C5 missing recipe at step {s['step']}"
                
    # C3 anchors on Product A
    ra = prods["A"]["route"]
    assert ra[27]["tool_group"] == "TG01_LITHO", "C3 Step 28 must be TG01_LITHO"
    assert ra[63]["tool_group"] == "TG11_CMP_OX", "C3 Step 64 must be TG11_CMP_OX"
    
    # C6 rework loops
    gate_loop = [ra[i]["tool_group"] for i in range(24, 28)]
    assert gate_loop == ["TG04_STRIP", "TG14_WET_SINGLE", "TG02_TRACK", "TG01_LITHO"]
    cmp_loop = [ra[i]["tool_group"] for i in range(63, 65)]
    assert cmp_loop == ["TG11_CMP_OX", "TG14_WET_SINGLE"]
