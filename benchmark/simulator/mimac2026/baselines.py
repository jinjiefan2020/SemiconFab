from __future__ import annotations

from typing import Callable, List, Optional
from .model import Lot, ToolGroupSpec


def fifo_select(queue: List[Lot], current_time: float) -> Optional[Lot]:
    """First-In, First-Out (SPEC §5.1): earliest queue entry time."""
    if not queue:
        return None
    return min(queue, key=lambda l: (l.queue_enter_time, l.lot_id))


def spt_select(queue: List[Lot], current_time: float, exp_proc_time: float) -> Optional[Lot]:
    """Shortest Processing Time (SPEC §5.2): lowest step duration, tie-breaker FIFO."""
    if not queue:
        return None
    # For identical step duration at same tool group, falls back to FIFO
    return min(queue, key=lambda l: (exp_proc_time, l.queue_enter_time, l.lot_id))


def edd_select(queue: List[Lot], current_time: float) -> Optional[Lot]:
    """Earliest Due Date (SPEC §5.3): min due date, tie-breaker FIFO."""
    if not queue:
        return None
    return min(queue, key=lambda l: (l.due_date, l.queue_enter_time, l.lot_id))


def cr_select(queue: List[Lot], current_time: float) -> Optional[Lot]:
    """
    Critical Ratio Dispatching (SPEC §5.4).
    CR = (due_date - current_time) / remaining_workload
    Late lots (CR < 0) are strictly prioritized over on-time lots.
    """
    if not queue:
        return None

    def cr_key(l: Lot):
        rem = max(0.01, l.remaining_workload_h)
        slack = l.due_date - current_time
        cr_val = slack / rem
        # Tuple ordering:
        # If cr_val < 0: primary sort is 0 (late bucket), then cr_val (more negative = more urgent)
        # If cr_val >= 0: primary sort is 1 (on-time bucket), then cr_val (smaller = more urgent)
        is_late = 0 if cr_val < 0 else 1
        return (is_late, cr_val, l.due_date, l.queue_enter_time, l.lot_id)

    return min(queue, key=cr_key)


def get_dispatcher(name: str) -> Callable[[List[Lot], float, ToolGroupSpec], Optional[List[Lot]]]:
    """Return dispatcher callable for policy name."""
    name_low = name.lower().strip()

    def serial_wrapper(policy_fn):
        def _dispatch(queue: List[Lot], current_time: float, spec: ToolGroupSpec) -> Optional[List[Lot]]:
            if not queue:
                return None
            if spec.tool_type == "serial":
                selected = policy_fn(queue, current_time)
                return [selected] if selected else None
            else:
                # Batch tool logic (SPEC §5.5)
                b_min, b_max = spec.batch_min, spec.batch_max
                timeout = spec.batch_timeout_h
                sorted_queue = sorted(queue, key=lambda l: l.queue_enter_time)
                if len(sorted_queue) >= b_max:
                    return sorted_queue[:b_max]
                if len(sorted_queue) >= b_min:
                    oldest_wait = current_time - sorted_queue[0].queue_enter_time
                    if oldest_wait >= timeout:
                        return sorted_queue[:b_max]
                return None
        return _dispatch

    if name_low == "fifo":
        return serial_wrapper(fifo_select)
    elif name_low == "spt":
        return serial_wrapper(lambda q, t: spt_select(q, t, 0.5))
    elif name_low == "edd":
        return serial_wrapper(edd_select)
    elif name_low == "cr":
        return serial_wrapper(cr_select)
    else:
        raise ValueError(f"Unknown dispatching policy: {name}")
