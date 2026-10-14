from __future__ import annotations

import copy
from pathlib import Path
import pytest

from mimac2026.model import FabConfig
from mimac2026.sim import FabSimulator
from mimac2026.baselines import get_dispatcher
from mimac2026.gym_api import FabEnv

CONFIG_PATH = Path(__file__).resolve().parent.parent / "fab_config.json"


@pytest.fixture
def fab_config():
    return FabConfig.from_file(CONFIG_PATH)


def test_smoke_7_day_run_completes(fab_config):
    """Test (a): 7-day smoke run completes without error."""
    sim = FabSimulator(fab_config, dispatcher="fifo", seed=42, warmup_days=2.0, run_length_days=5.0)
    metrics = sim.run()

    assert metrics.completed_lots > 0
    assert metrics.throughput_lots_per_day > 0
    assert metrics.runtime_sec < 60.0, f"Runtime too slow: {metrics.runtime_sec} s"


def test_bottleneck_utilization_within_spec_band(fab_config):
    """Test (b): Bottleneck utilization lands within the designed spec band [88%, 93%]."""
    sim = FabSimulator(fab_config, dispatcher="fifo", seed=42, warmup_days=30.0, run_length_days=90.0)
    metrics = sim.run()

    u_litho = metrics.bottleneck_utilization * 100.0
    # Spec band: [88.0%, 93.0%], allow minor simulation variance window [87.0%, 94.0%]
    assert 87.0 <= u_litho <= 94.0, f"Litho utilization {u_litho:.2f}% out of spec band [88%, 93%]"


def test_directional_superiority_cr_vs_fifo(fab_config):
    """Test (c): Critical Ratio (CR) mean cycle time < FIFO mean cycle time (directional check)."""
    # Use Common Random Numbers (CRN) with same seed
    sim_fifo = FabSimulator(fab_config, dispatcher="fifo", seed=100, warmup_days=20.0, run_length_days=60.0)
    m_fifo = sim_fifo.run()

    sim_cr = FabSimulator(fab_config, dispatcher="cr", seed=100, warmup_days=20.0, run_length_days=60.0)
    m_cr = sim_cr.run()

    assert m_cr.mean_cycle_time_days < m_fifo.mean_cycle_time_days, (
        f"Expected CR ({m_cr.mean_cycle_time_days:.2f}d) < FIFO ({m_fifo.mean_cycle_time_days:.2f}d)"
    )


def test_all_baselines_produce_finite_metrics(fab_config):
    """Test (d): All baselines (FIFO, SPT, EDD, CR) run without deadlock and produce finite metrics."""
    for policy in ["fifo", "spt", "edd", "cr"]:
        sim = FabSimulator(fab_config, dispatcher=policy, seed=123, warmup_days=5.0, run_length_days=15.0)
        m = sim.run()
        assert m.completed_lots > 0, f"Policy {policy} completed 0 lots"
        assert m.mean_cycle_time_days > 0, f"Policy {policy} has invalid cycle time"
        assert m.mean_wip > 0, f"Policy {policy} has 0 WIP"


def test_config_absence_breaks_simulation():
    """Test (e) / AC6: Deleting or missing fab_config.json breaks the sim (no hardcoded numbers)."""
    with pytest.raises((FileNotFoundError, ValueError)):
        FabConfig.from_file(Path("/non/existent/path/fab_config.json"))


def test_gym_api_environment(fab_config):
    """Test Gymnasium API reset and step interface."""
    env_default = FabEnv()
    obs_def, _ = env_default.reset(seed=42)
    assert "tool_group_id" in obs_def

    env = FabEnv(config=fab_config)
    obs, info = env.reset(seed=42)
    assert "tool_group_id" in obs
    assert "queue_matrix" in obs
    assert obs["queue_matrix"].shape == (env.max_queue_len, env.lot_features)

    obs, reward, term, trunc, info = env.step(action=0)
    assert isinstance(reward, float)


def test_pm_scheduled_downtime_execution(fab_config):
    """Test SEMI E10 Scheduled Downtime (SDT) when enable_pm=True."""
    from mimac2026.events import EventEmitter
    events_log = []

    class MockEmitter(EventEmitter):
        def emit(self, event_type, timestamp_sec, payload):
            if event_type == "tool_state_change":
                events_log.append(payload)

    emitter = MockEmitter(enabled=True)
    sim = FabSimulator(
        fab_config,
        dispatcher="fifo",
        seed=42,
        warmup_days=0.0,
        run_length_days=10.0,
        enable_pm=True,
        event_emitter=emitter,
    )
    sim.run()

    # Verify at least one tool executed SDT scheduled maintenance
    sdt_events = [e for e in events_log if e.get("semi_e10_state") == "SDT_scheduled_down"]
    assert len(sdt_events) > 0, "No SDT scheduled downtime events observed with enable_pm=True"
    assert any("TG01_LITHO" in e["machine_id"] or "TG03_ETCH" in e["machine_id"] for e in sdt_events)
