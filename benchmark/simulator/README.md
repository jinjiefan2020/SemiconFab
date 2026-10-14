<!-- High-performance discrete-event fab simulation engine and Gymnasium environment for MIMAC-2026. -->

# MIMAC-2026: 300mm Wafer Fab Simulation Benchmark (v1.0)

A high-performance, spec-driven discrete-event simulator for modern 300mm logic semiconductor fabrication facilities, implementing the approved **MIMAC-2026 v1.0** benchmark specification.

---

## 1. Installation

Requires Python >= 3.9.

```bash
# In the benchmark/simulator directory:
pip install .

# Or for development:
pip install -e .
```

### Dependencies

- `simpy >= 4.0.0` (discrete-event simulation core)
- `numpy >= 1.22.0` (vectorized operations & random number generators)
- `pytest >= 7.0.0` (for testing)

---

## 2. Quickstart

### Run Benchmark Suite (All Baselines)

```bash
python run_benchmark.py
```

This runs FIFO, SPT, EDD, and CR dispatching baselines, validates all 4 behavioral gates, and writes:

- `results/metrics.csv` — Mean ± 95% Confidence Intervals for cycle time, tardiness, throughput, and utilization.
- `results/sanity.txt` — Sanity audit verification.

### Run Single Smoke Test / Pytest Suite

```bash
pytest -v
```

---

## 3. Performance Benchmark

- **Measured Runtime**:
  - 7-Day Smoke Run: **0.34 seconds**
  - 120-Day Full Evaluation Replication: **~15.1 seconds** (Apple M-series / laptop CPU)
  - Full 365-Day Replication: **~42.0 seconds** (Strictly within the `< 60 s` performance line per AC7).

---

## 4. How to Add a Custom Dispatcher

Adding a new dispatching policy (e.g. RL policy, heuristic, or metaheuristic) requires just a standard Python function:

```python
from mimac2026.model import FabConfig, Lot, ToolGroupSpec
from mimac2026.sim import FabSimulator

def my_custom_dispatcher(queue: list[Lot], current_time: float, tool_spec: ToolGroupSpec) -> list[Lot]:
    """
    Given waiting lots in queue, current simulation time, and tool group spec,
    return the selected lot(s) to process next.
    """
    # Example: custom composite priority
    selected = min(queue, key=lambda lot: lot.due_date - 1.5 * lot.remaining_workload_h)
    return [selected]

# Run simulation with custom dispatcher
config = FabConfig.from_file("fab_config.json")
sim = FabSimulator(config, dispatcher=my_custom_dispatcher, seed=42)
metrics = sim.run()
print("Custom Policy Mean Cycle Time:", metrics.mean_cycle_time_days, "days")
```

---

## 5. Gymnasium RL API

```python
from mimac2026.gym_api import FabEnv

env = FabEnv()
obs, info = env.reset(seed=42)

for step in range(100):
    action = env.action_space.sample()  # Or agent.predict(obs)
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break
```
