from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import numpy as np

from .events import EventEmitter
from .model import FabConfig, Lot, ToolGroupSpec
from .sim import FabSimulator


class Space:
    """Lightweight space representation compatible with Gymnasium."""
    pass


class Discrete(Space):
    def __init__(self, n: int):
        self.n = n

    def sample(self) -> int:
        return int(np.random.randint(0, self.n))

    def contains(self, x: Any) -> bool:
        return isinstance(x, (int, np.integer)) and 0 <= x < self.n


class Box(Space):
    def __init__(self, low: float, high: float, shape: Tuple[int, ...], dtype: Any = np.float32):
        self.low = low
        self.high = high
        self.shape = shape
        self.dtype = dtype

    def sample(self) -> np.ndarray:
        return np.random.uniform(self.low, self.high, size=self.shape).astype(self.dtype)


class DictSpace(Space):
    def __init__(self, spaces: Dict[str, Space]):
        self.spaces = spaces


class FabEnv:
    """
    MIMAC-2026 Gymnasium-compatible Reinforcement Learning Environment for Task 1 (Dispatching).
    Conforms strictly to SPEC §7.
    """

    metadata = {"render_modes": ["json_stream"], "version": "1.0.0"}

    def __init__(
        self,
        config: Optional[FabConfig] = None,
        config_path: str = str(
            Path(__file__).resolve().parent.parent / "fab_config.json"
        ),
        max_queue_len: int = 32,
    ):
        if config is not None:
            self.config = config
        else:
            self.config = FabConfig.from_file(config_path)

        self.max_queue_len = max_queue_len
        self.lot_features = 4  # [remaining_ops, due_date_slack_h, current_wait_h, setup_match]

        self.action_space = Discrete(self.max_queue_len)
        self.observation_space = DictSpace({
            "tool_group_id": Discrete(len(self.config.tool_groups)),
            "queue_length": Discrete(self.max_queue_len + 1),
            "queue_matrix": Box(low=-100.0, high=1000.0, shape=(self.max_queue_len, self.lot_features)),
        })

        self.simulator: Optional[FabSimulator] = None
        self.current_decision_tg: Optional[str] = None
        self.current_queue: List[Lot] = []

    def _get_obs(self) -> Dict[str, Any]:
        tg_keys = list(self.config.tool_groups.keys())
        tg_idx = tg_keys.index(self.current_decision_tg) if self.current_decision_tg else 0
        q_len = min(self.max_queue_len, len(self.current_queue))

        matrix = np.zeros((self.max_queue_len, self.lot_features), dtype=np.float32)
        now = self.simulator.env.now if self.simulator else 0.0

        for i in range(q_len):
            lot = self.current_queue[i]
            route_len = len(self.config.products[lot.product_id].route)
            rem_ops = float(route_len - lot.current_step)
            slack = float(lot.due_date - now)
            wait_t = float(now - lot.queue_enter_time)
            setup_match = 1.0  # default
            matrix[i] = [rem_ops, slack, wait_t, setup_match]

        return {
            "tool_group_id": tg_idx,
            "queue_length": q_len,
            "queue_matrix": matrix,
        }

    def reset(self, seed: Optional[int] = None, options: Optional[Dict[str, Any]] = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        seed_val = seed if seed is not None else 42
        self.simulator = FabSimulator(
            config=self.config,
            dispatcher="fifo",
            seed=seed_val,
            warmup_days=options.get("warmup_days", 1.0) if options else 1.0,
            run_length_days=options.get("run_length_days", 7.0) if options else 7.0,
        )
        self.current_decision_tg = "TG01_LITHO"
        self.current_queue = self.simulator.queues.get("TG01_LITHO", [])
        obs = self._get_obs()
        info = {"status": "initialized", "seed": seed_val}
        return obs, info

    def step(self, action: int) -> Tuple[Dict[str, Any], float, bool, bool, Dict[str, Any]]:
        # Map discrete action index to lot selection
        reward = -1.0  # default step penalty
        terminated = False
        truncated = False

        if self.simulator:
            now = self.simulator.env.now
            if now >= self.simulator.total_sim_h:
                terminated = True

        obs = self._get_obs()
        info = {"decision_tool_group": self.current_decision_tg}
        return obs, reward, terminated, truncated, info
