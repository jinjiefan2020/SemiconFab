from __future__ import annotations

import json
from typing import Any, Callable, Dict, List, Optional


class EventEmitter:
    """Emits discrete simulation events conforming to MIMAC-2026 SPEC §8."""

    def __init__(self, callback: Optional[Callable[[Dict[str, Any]], None]] = None, enabled: bool = True):
        self.callback = callback
        self.enabled = enabled
        self.events: List[Dict[str, Any]] = []

    def emit(self, event_type: str, timestamp_sec: float, payload: Dict[str, Any]) -> None:
        if not self.enabled:
            return
        packet = {
            "timestamp_sec": round(timestamp_sec, 3),
            "event_type": event_type,
            "payload": payload,
        }
        if self.callback:
            self.callback(packet)
        else:
            self.events.append(packet)

    def to_json_lines(self) -> str:
        return "\n".join(json.dumps(e) for e in self.events)
