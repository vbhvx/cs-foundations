"""Cyclic barrier for coordinated multi-threaded phases."""
import threading

class CyclicBarrier:
    def __init__(self, parties: int):
        if parties <= 0: raise ValueError("Parties must be positive")
        self._parties = parties
        self._count = 0
        self._generation = 0
        self._lock = threading.Lock()
        self._cond = threading.Condition(self._lock)

    def wait(self) -> int:
        with self._cond:
            gen = self._generation
            self._count += 1
            index = self._count - 1
            if self._count == self._parties:
                self._generation += 1
                self._count = 0
                self._cond.notify_all()
                return index
            while gen == self._generation:
                self._cond.wait()
            return index
