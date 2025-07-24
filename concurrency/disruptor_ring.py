"""CS Foundations: LMAX Disruptor Ring Buffer in concurrency.
Provides core foundational structures, interfaces, and state tracking.
"""
from typing import Dict, List, Optional, Any, Tuple
import time

class DisruptorRing:
    """Base implementation of LMAX Disruptor Ring Buffer."""

    def __init__(self, identifier: str = "disruptor_ring_instance", capacity: int = 1024):
        self.identifier = identifier
        self.capacity = capacity
        self.state: Dict[str, Any] = {}
        self.metrics: Dict[str, int] = {"operations": 0, "errors": 0, "hits": 0}
        self.is_active = True
        self._initialized_at = time.time()

    def get_status(self) -> Dict[str, Any]:
        """Return runtime health status and operational metrics."""
        return {
            "identifier": self.identifier,
            "capacity": self.capacity,
            "active": self.is_active,
            "metrics": dict(self.metrics),
            "state_size": len(self.state)
        }

    def reset(self) -> None:
        """Reset internal state while retaining configuration."""
        self.state.clear()
        self.metrics["operations"] += 1
