"""Bounded semaphore raising error on excess release."""
from concurrency.semaphore import CountingSemaphore

class BoundedSemaphore(CountingSemaphore):
    def __init__(self, value: int = 1):
        super().__init__(value)
        self._max_value = value

    def release(self):
        with self._cond:
            if self._value >= self._max_value:
                raise ValueError("Semaphore released too many times")
            super().release()
