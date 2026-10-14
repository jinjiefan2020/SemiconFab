#!/usr/bin/env python3
"""
Generate MIMAC-2026 T1 FIFO 30-Day Event Log for Cleanroom Digital Twin.
Spec: MIMAC-2026 SPEC §8.
Outputs downsampled event stream to twin/events-t1-fifo.jsonl (<= 5 MB).
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

# Add simulator to path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmark" / "simulator"))

from mimac2026.model import FabConfig
from mimac2026.sim import FabSimulator
from mimac2026.events import EventEmitter


def generate_event_stream(
    config_path: Path,
    output_paths: list[Path],
    seed: int = 42,
    run_days: float = 30.0,
    target_max_mb: float = 4.8,
):
    print(f"Loading FabConfig from {config_path}...")
    cfg = FabConfig.from_file(config_path)

    print(f"Running simulation: 1 rep, FIFO baseline, {run_days} days, seed={seed}...")
    emitter = EventEmitter(enabled=True)
    sim = FabSimulator(
        config=cfg,
        dispatcher="fifo",
        seed=seed,
        warmup_days=0.0,
        run_length_days=run_days,
        enable_pm=True,
        event_emitter=emitter,
    )
    metrics = sim.run()

    raw_events = emitter.events
    print(f"Raw simulation events emitted: {len(raw_events)}")

    # Downsampling strategy (WS3):
    # 1. 100% of wip_sample (hourly fab WIP count)
    # 2. 100% of lot_spawned (arrival records)
    # 3. 100% of UDT (unscheduled down) and SDT (scheduled down / PM)
    # 4. Sampled tool_state_change (PR_productive and SBY_standby) to fit <= 5 MB
    wips = [e for e in raw_events if e["event_type"] == "wip_sample"]
    lots = [e for e in raw_events if e["event_type"] == "lot_spawned"]
    tools = [e for e in raw_events if e["event_type"] == "tool_state_change"]

    down_events = [
        e for e in tools
        if e["payload"].get("semi_e10_state") in ("UDT_unscheduled_down", "SDT_scheduled_down")
    ]
    other_tools = [
        e for e in tools
        if e["payload"].get("semi_e10_state") not in ("UDT_unscheduled_down", "SDT_scheduled_down")
    ]

    target_other_count = 23000
    factor = max(1, len(other_tools) // target_other_count)
    sampled_other = other_tools[::factor]

    downsampled = wips + lots + down_events + sampled_other
    downsampled.sort(key=lambda x: x["timestamp_sec"])

    print(
        f"Filtered summary: WIP samples={len(wips)}, Lots={len(lots)}, "
        f"Downtime/PM={len(down_events)}, Productive/Standby={len(sampled_other)} (factor {factor})"
    )
    print(f"Total events in downsampled stream: {len(downsampled)}")

    lines = [json.dumps(e, separators=(",", ":")) for e in downsampled]
    jsonl_content = "\n".join(lines) + "\n"
    size_mb = len(jsonl_content.encode("utf-8")) / (1024 * 1024)
    print(f"Serialized JSONL size: {size_mb:.2f} MB")
    assert size_mb <= 5.0, f"File size {size_mb:.2f} MB exceeds 5 MB limit!"

    for p in output_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(jsonl_content, encoding="utf-8")
        print(f"Saved: {p} ({size_mb:.2f} MB)")


if __name__ == "__main__":
    cfg_file = ROOT / "benchmark" / "simulator" / "fab_config.json"
    targets = [
        ROOT / "twin" / "events-t1-fifo.jsonl",
    ]
    generate_event_stream(cfg_file, targets)
