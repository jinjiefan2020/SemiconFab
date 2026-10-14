from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class ToolGroupSpec:
    id: str
    name: str
    machines: int
    tool_type: str  # "serial" | "batch"
    batch_min: int
    batch_max: int
    batch_timeout_h: float
    availability: float
    mtbf_h: float
    mttr_h: float
    t_proc_h: float
    cv: float
    setup_families: int = 1
    setup_time_h: float = 0.0
    pm_interval_h: Optional[float] = None
    pm_duration_h: Optional[float] = None


@dataclass
class Machine:
    machine_id: str
    group_id: str
    spec: ToolGroupSpec
    state: str = "SBY_standby"
    current_setup_family: int = 0
    total_busy_time: float = 0.0
    total_down_time: float = 0.0
    is_down: bool = False


@dataclass
class ProductSpec:
    id: str
    name: str
    mix: float
    due_date_factor: float
    route: List[str]


@dataclass
class ReworkRule:
    name: str
    trigger_op: str
    trigger_step_index: int
    probability: float
    loop_ops: List[str]


@dataclass
class Lot:
    lot_id: str
    product_id: str
    wafers: int
    arrival_time: float
    due_date: float
    current_step: int = 0
    remaining_workload_h: float = 0.0
    queue_enter_time: float = 0.0
    setup_family: int = 0
    rework_count: int = 0
    scrapped: bool = False
    completed: bool = False
    completion_time: Optional[float] = None


class FabConfig:
    """Loads and holds the fab topology transcribed from the spec."""

    def __init__(self, raw: Dict[str, Any]):
        if not raw or "tool_groups" not in raw or "product_mix" not in raw:
            raise ValueError("Invalid fab configuration: missing required sections.")

        self.meta = raw.get("_meta", {})
        self.arrival_rate_lots_h = float(raw["arrival_process"]["rate_lots_per_hour"])
        self.lot_size_wafers = int(raw["arrival_process"]["lot_size_wafers"])

        # Tool Groups
        self.tool_groups: Dict[str, ToolGroupSpec] = {}
        for tg_id, info in raw["tool_groups"].items():
            if tg_id.startswith("_"):
                continue
            bs = info.get("batch_size", [1, 1])
            setup_info = info.get("setup", {})
            pm_info = info.get("pm", {})
            self.tool_groups[tg_id] = ToolGroupSpec(
                id=tg_id,
                name=info.get("name", tg_id),
                machines=int(info["machines"]),
                tool_type=info["type"],
                batch_min=int(bs[0]),
                batch_max=int(bs[1]),
                batch_timeout_h=float(info.get("batch_timeout_h", 2.0)),
                availability=float(info["availability"]),
                mtbf_h=float(info["mtbf_h"]),
                mttr_h=float(info["mttr_h"]),
                t_proc_h=float(info["t_proc_h"]),
                cv=float(info["cv"]),
                setup_families=int(setup_info.get("families", 1)),
                setup_time_h=float(setup_info.get("time_h", 0.0)),
                pm_interval_h=float(pm_info["interval_h"]) if pm_info else None,
                pm_duration_h=float(pm_info["duration_h"]) if pm_info else None,
            )

        # Products
        self.products: Dict[str, ProductSpec] = {}
        for p_id, p_info in raw["product_mix"].items():
            if p_id.startswith("_"):
                continue
            self.products[p_id] = ProductSpec(
                id=p_id,
                name=p_info.get("name", p_id),
                mix=float(p_info["mix"]),
                due_date_factor=float(p_info.get("due_date_factor", 3.0)),
                route=[s["tool_group"] if isinstance(s, dict) else s for s in p_info["route"]],
            )

        # Quality
        q_info = raw.get("quality", {})
        self.scrap_prob_per_step = float(q_info.get("scrap_probability_per_step", 0.0004))
        self.rework_rules: List[ReworkRule] = []
        for rw in q_info.get("rework_rules", []):
            self.rework_rules.append(
                ReworkRule(
                    name=rw["name"],
                    trigger_op=rw["trigger_op"],
                    trigger_step_index=int(rw["trigger_step_index"]),
                    probability=float(rw["probability"]),
                    loop_ops=list(rw["loop_ops"]),
                )
            )

        # Protocols
        proto = raw.get("simulation_protocol", {})
        self.warmup_days = float(proto.get("warmup_days", 60.0))
        self.run_length_days = float(proto.get("run_length_days", 365.0))
        self.replications = int(proto.get("replications", 30))
        self.smoke_run_days = float(proto.get("smoke_run_days", 7.0))

    @classmethod
    def from_file(cls, path: str | Path) -> FabConfig:
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"Configuration file not found: {p}")
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(data)
