"""Atomic reference counter simulating smart pointer management."""
import threading

class AtomicRefCount:
    def __init__(self, initial_count: int = 1):
        self._count = initial_count
        self._lock = threading.Lock()

    def inc(self) -> int:
        with self._lock:
            self._count += 1
            return self._count

    def dec(self) -> int:
        with self._lock:
            self._count -= 1
            return self._count

    def get(self) -> int:
        with self._lock:
            return self._count
