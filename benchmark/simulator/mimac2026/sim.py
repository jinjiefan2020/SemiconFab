from __future__ import annotations

import math
from typing import Any, Callable, Dict, List, Optional, Tuple
import numpy as np
import simpy

from .baselines import get_dispatcher
from .events import EventEmitter
from .metrics import ReplicationMetrics
from .model import FabConfig, Lot, Machine, ToolGroupSpec


class FabSimulator:
    """SimPy discrete-event simulation core for MIMAC-2026."""

    def __init__(
        self,
        config: FabConfig,
        dispatcher: str | Callable = "fifo",
        seed: int = 42,
        event_emitter: Optional[EventEmitter] = None,
        warmup_days: Optional[float] = None,
        run_length_days: Optional[float] = None,
        enable_pm: bool = False,
    ):
        self.config = config
        self.seed = seed
        self.enable_pm = enable_pm
        self.rng = np.random.default_rng(seed)
        self.events = event_emitter or EventEmitter(enabled=False)

        if isinstance(dispatcher, str):
            self.dispatcher_name = dispatcher.lower()
            self.dispatch_fn = get_dispatcher(dispatcher)
        else:
            self.dispatcher_name = "custom"
            self.dispatch_fn = dispatcher

        self.warmup_h = (warmup_days if warmup_days is not None else config.warmup_days) * 24.0
        self.run_length_h = (run_length_days if run_length_days is not None else config.run_length_days) * 24.0
        self.total_sim_h = self.warmup_h + self.run_length_h

        self.env = simpy.Environment()

        # Build machine pools and queues per tool group
        self.machines: Dict[str, List[Machine]] = {}
        self.queues: Dict[str, List[Lot]] = {}
        self.tg_wake_events: Dict[str, simpy.Event] = {}

        for tg_id, spec in config.tool_groups.items():
            self.machines[tg_id] = [
                Machine(f"{tg_id}_{m+1:02d}", tg_id, spec) for m in range(spec.machines)
            ]
            self.queues[tg_id] = []
            self.tg_wake_events[tg_id] = self.env.event()

        # Metrics collection
        self.started_lots = 0
        self.completed_lots: List[Lot] = []
        self.scrapped_lots = 0
        self.wip_samples: List[Tuple[float, int]] = []
        self.active_lots: Dict[str, Lot] = {}

    def _sample_proc_time(self, spec: ToolGroupSpec) -> float:
        """Lognormal processing time sample (SPEC §2.5)."""
        mean_t = spec.t_proc_h
        cv = spec.cv
        sigma_log = math.sqrt(math.log(1.0 + cv * cv))
        mu_log = math.log(mean_t) - 0.5 * sigma_log * sigma_log
        val = self.rng.lognormal(mu_log, sigma_log)
        return max(0.01, float(val))

    def _calc_remaining_workload(self, product_id: str, from_step: int) -> float:
        route = self.config.products[product_id].route
        total_w = 0.0
        for s in range(from_step, len(route)):
            tg_id = route[s]
            spec = self.config.tool_groups[tg_id]
            batch_factor = spec.batch_max if spec.tool_type == "batch" else 1.0
            total_w += spec.t_proc_h / batch_factor
        return total_w

    def _arrival_process(self):
        """Poisson lot arrivals (SPEC §2.6)."""
        rate = self.config.arrival_rate_lots_h
        products = list(self.config.products.values())
        mix_probs = [p.mix for p in products]

        while True:
            # Inter-arrival time
            dt = self.rng.exponential(1.0 / rate)
            yield self.env.timeout(dt)

            self.started_lots += 1
            prod = self.rng.choice(products, p=mix_probs)
            now = self.env.now

            total_workload = self._calc_remaining_workload(prod.id, 0)
            due_date = now + prod.due_date_factor * total_workload

            lot = Lot(
                lot_id=f"LOT_{prod.id}_{self.started_lots:06d}",
                product_id=prod.id,
                wafers=self.config.lot_size_wafers,
                arrival_time=now,
                due_date=due_date,
                current_step=0,
                remaining_workload_h=total_workload,
                queue_enter_time=now,
                setup_family=self.rng.integers(0, 4),
            )
            self.active_lots[lot.lot_id] = lot

            self.events.emit(
                "lot_spawned",
                now * 3600,
                {"lot_id": lot.lot_id, "product": prod.id, "due_date": due_date},
            )

            # Route to first step
            first_tg = prod.route[0]
            self.queues[first_tg].append(lot)
            self._trigger_wake(first_tg)

    def _trigger_wake(self, tg_id: str):
        if not self.tg_wake_events[tg_id].triggered:
            self.tg_wake_events[tg_id].succeed()
            self.tg_wake_events[tg_id] = self.env.event()

    def _machine_loop(self, machine: Machine):
        """Lifecycle process for a single machine in a tool group."""
        tg_id = machine.group_id
        spec = machine.spec

        while True:
            if machine.is_down:
                yield self.env.timeout(0.5)
                continue

            q = self.queues[tg_id]
            if not q:
                machine.state = "SBY_standby"
                # Wait for arrivals
                yield self.tg_wake_events[tg_id]
                continue

            # Dispatch selection
            selected_lots = self.dispatch_fn(q, self.env.now, spec)
            if not selected_lots:
                # E.g. waiting for batch timeout
                machine.state = "SBY_standby"
                yield self.env.timeout(0.2)
                continue

            # Remove lots from queue
            for l in selected_lots:
                if l in q:
                    q.remove(l)

            # Setup check
            setup_duration = 0.0
            primary_lot = selected_lots[0]
            if spec.setup_families > 1 and primary_lot.setup_family != machine.current_setup_family:
                setup_duration = spec.setup_time_h
                machine.current_setup_family = primary_lot.setup_family

            # Sample processing time
            proc_duration = self._sample_proc_time(spec)
            total_duration = setup_duration + proc_duration

            # Transition to Productive
            machine.state = "PR_productive"
            start_t = self.env.now
            self.events.emit(
                "tool_state_change",
                start_t * 3600,
                {
                    "machine_id": machine.machine_id,
                    "tool_group_id": tg_id,
                    "semi_e10_state": "PR_productive",
                },
            )

            for l in selected_lots:
                self.events.emit(
                    "lot_step_start",
                    start_t * 3600,
                    {
                        "lot_id": l.lot_id,
                        "tool_group_id": tg_id,
                        "machine_id": machine.machine_id,
                        "step_index": l.current_step,
                    },
                )

            # Execute run
            yield self.env.timeout(total_duration)

            finish_t = self.env.now
            machine.total_busy_time += total_duration
            machine.state = "SBY_standby"
            self.events.emit(
                "tool_state_change",
                finish_t * 3600,
                {
                    "machine_id": machine.machine_id,
                    "tool_group_id": tg_id,
                    "semi_e10_state": "SBY_standby",
                },
            )

            # Complete step for all lots in batch
            for l in selected_lots:
                l.remaining_workload_h = self._calc_remaining_workload(l.product_id, l.current_step + 1)
                self.events.emit(
                    "lot_step_complete",
                    finish_t * 3600,
                    {
                        "lot_id": l.lot_id,
                        "tool_group_id": tg_id,
                        "machine_id": machine.machine_id,
                        "step_index": l.current_step,
                    },
                )

                # Check Scrap (SPEC §2.8)
                if self.rng.random() < self.config.scrap_prob_per_step:
                    l.scrapped = True
                    self.scrapped_lots += 1
                    if l.lot_id in self.active_lots:
                        del self.active_lots[l.lot_id]
                    continue

                # Check Rework (SPEC §2.8)
                rework_triggered = False
                for rw in self.config.rework_rules:
                    if tg_id == rw.trigger_op and l.current_step == rw.trigger_step_index:
                        if self.rng.random() < rw.probability and l.rework_count < 2:
                            rework_triggered = True
                            l.rework_count += 1
                            # Move lot to first rework op
                            first_rw_op = rw.loop_ops[0]
                            l.queue_enter_time = finish_t
                            self.queues[first_rw_op].append(l)
                            self._trigger_wake(first_rw_op)
                            break
                if rework_triggered:
                    continue

                # Normal step advance
                l.current_step += 1
                route = self.config.products[l.product_id].route
                if l.current_step >= len(route):
                    # Route Complete!
                    l.completed = True
                    l.completion_time = finish_t
                    if l.lot_id in self.active_lots:
                        del self.active_lots[l.lot_id]
                    # Only collect statistics after warmup
                    if finish_t >= self.warmup_h:
                        self.completed_lots.append(l)
                else:
                    next_tg = route[l.current_step]
                    l.queue_enter_time = finish_t
                    self.queues[next_tg].append(l)
                    self._trigger_wake(next_tg)

    def _downtime_process(self, machine: Machine):
        """Exponential MTBF / MTTR equipment failures (SPEC §2.7)."""
        spec = machine.spec
        if spec.mtbf_h <= 0:
            return

        while True:
            up_time = self.rng.exponential(spec.mtbf_h)
            yield self.env.timeout(up_time)

            down_time = self.rng.exponential(spec.mttr_h)
            machine.is_down = True
            old_state = machine.state
            machine.state = "UDT_unscheduled_down"
            machine.total_down_time += down_time

            self.events.emit(
                "tool_state_change",
                self.env.now * 3600,
                {
                    "machine_id": machine.machine_id,
                    "tool_group_id": machine.group_id,
                    "semi_e10_state": machine.state,
                },
            )

            yield self.env.timeout(down_time)
            machine.is_down = False
            machine.state = "SBY_standby"
            self.events.emit(
                "tool_state_change",
                self.env.now * 3600,
                {
                    "machine_id": machine.machine_id,
                    "tool_group_id": machine.group_id,
                    "semi_e10_state": machine.state,
                },
            )
            self._trigger_wake(machine.group_id)

    def _pm_process(self, machine: Machine, machine_index: int, total_machines: int):
        """Periodic Preventive Maintenance (PM / SDT) per SEMI E10 (SPEC §2.7)."""
        spec = machine.spec
        if not spec.pm_interval_h or not spec.pm_duration_h:
            return

        interval = spec.pm_interval_h
        duration = spec.pm_duration_h

        # Stagger initial PM offsets across machines in the group
        # so all machines do not enter PM simultaneously
        stagger = (machine_index / max(1, total_machines)) * interval
        if stagger > 0:
            yield self.env.timeout(stagger)

        while True:
            yield self.env.timeout(interval)

            # Wait if machine is currently busy processing or in unscheduled down
            while machine.state == "PR_productive" or machine.state == "UDT_unscheduled_down":
                yield self.env.timeout(0.1)

            machine.is_down = True
            machine.state = "SDT_scheduled_down"
            machine.total_down_time += duration

            self.events.emit(
                "tool_state_change",
                self.env.now * 3600,
                {
                    "machine_id": machine.machine_id,
                    "tool_group_id": machine.group_id,
                    "semi_e10_state": machine.state,
                },
            )

            yield self.env.timeout(duration)
            machine.is_down = False
            machine.state = "SBY_standby"
            self._trigger_wake(machine.group_id)

            self.events.emit(
                "tool_state_change",
                self.env.now * 3600,
                {
                    "machine_id": machine.machine_id,
                    "tool_group_id": machine.group_id,
                    "semi_e10_state": machine.state,
                },
            )

    def _wip_sampler_process(self):
        """Sample fab WIP every hour."""
        while True:
            yield self.env.timeout(1.0)
            now = self.env.now
            wip = len(self.active_lots)
            if now >= self.warmup_h:
                self.wip_samples.append((now, wip))
            self.events.emit("wip_sample", now * 3600, {"wip_count": wip})

    def run(self) -> ReplicationMetrics:
        """Run simulation end-to-end and compute performance metrics."""
        import time

        t_start = time.time()

        # Start background processes
        self.env.process(self._arrival_process())
        self.env.process(self._wip_sampler_process())

        for tg_id, m_list in self.machines.items():
            tot_m = len(m_list)
            for idx, m in enumerate(m_list):
                self.env.process(self._machine_loop(m))
                self.env.process(self._downtime_process(m))
                if self.enable_pm and m.spec.pm_interval_h:
                    self.env.process(self._pm_process(m, idx, tot_m))

        # Execute SimPy environment
        self.env.run(until=self.total_sim_h)
        t_elapsed = time.time() - t_start

        # Calculate metrics
        comp = self.completed_lots
        n_comp = len(comp)

        if n_comp > 0:
            cycle_times = [(l.completion_time - l.arrival_time) / 24.0 for l in comp]  # in days
            mean_ct = float(np.mean(cycle_times))
            std_ct = float(np.std(cycle_times))
            tardiness = [max(0.0, (l.completion_time - l.due_date) / 24.0) for l in comp]
            mean_tardy = float(np.mean(tardiness))
        else:
            mean_ct = std_ct = mean_tardy = 0.0

        eval_days = self.run_length_h / 24.0
        tput_lots = n_comp / eval_days if eval_days > 0 else 0.0
        tput_wafers = tput_lots * self.config.lot_size_wafers

        mean_wip = float(np.mean([w for _, w in self.wip_samples])) if self.wip_samples else 0.0

        # Calculate utilizations
        utilizations = {}
        for tg_id, m_list in self.machines.items():
            tot_busy = sum(m.total_busy_time for m in m_list)
            # Total potential operating hours over simulation
            tot_avail = len(m_list) * self.total_sim_h
            utilizations[tg_id] = tot_busy / tot_avail if tot_avail > 0 else 0.0

        bottleneck_u = utilizations.get("TG01_LITHO", 0.0)

        return ReplicationMetrics(
            total_started_lots=self.started_lots,
            completed_lots=n_comp,
            scrapped_lots=self.scrapped_lots,
            mean_cycle_time_days=mean_ct,
            cycle_time_std_days=std_ct,
            mean_tardiness_days=mean_tardy,
            throughput_lots_per_day=tput_lots,
            throughput_wafers_per_day=tput_wafers,
            mean_wip=mean_wip,
            bottleneck_utilization=bottleneck_u,
            tool_utilizations=utilizations,
            runtime_sec=t_elapsed,
        )
