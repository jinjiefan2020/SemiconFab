from __future__ import annotations

from dataclasses import dataclass, field
import math
from typing import Dict, List, Optional


@dataclass
class ReplicationMetrics:
    total_started_lots: int = 0
    completed_lots: int = 0
    scrapped_lots: int = 0
    mean_cycle_time_days: float = 0.0
    cycle_time_std_days: float = 0.0
    mean_tardiness_days: float = 0.0
    throughput_lots_per_day: float = 0.0
    throughput_wafers_per_day: float = 0.0
    mean_wip: float = 0.0
    bottleneck_utilization: float = 0.0
    tool_utilizations: Dict[str, float] = field(default_factory=dict)
    runtime_sec: float = 0.0


@dataclass
class AggregateSummary:
    replications: int
    mean: float
    std_err: float
    ci_95_low: float
    ci_95_high: float

    def format_ci(self) -> str:
        return f"{self.mean:.3f} ± {self.std_err * 2.045:.3f} [{self.ci_95_low:.3f}, {self.ci_95_high:.3f}]"


def compute_confidence_interval(values: List[float], confidence: float = 0.95) -> AggregateSummary:
    n = len(values)
    if n == 0:
        return AggregateSummary(0, 0.0, 0.0, 0.0, 0.0)
    if n == 1:
        return AggregateSummary(1, values[0], 0.0, values[0], values[0])

    mean_val = sum(values) / n
    variance = sum((x - mean_val) ** 2 for x in values) / (n - 1)
    std_err = math.sqrt(variance / n)
    # Student's t critical value for df = n - 1 (df = 29 -> ~2.045, fallback to ~2.0 for general)
    t_crit = 2.045 if n >= 30 else 2.0
    half_width = t_crit * std_err

    return AggregateSummary(
        replications=n,
        mean=mean_val,
        std_err=std_err,
        ci_95_low=mean_val - half_width,
        ci_95_high=mean_val + half_width,
    )
