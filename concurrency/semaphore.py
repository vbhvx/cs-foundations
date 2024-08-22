"""Counting semaphore synchronization primitive."""
import threading

class CountingSemaphore:
    def __init__(self, value: int = 1):
        if value < 0: raise ValueError("Semaphore value cannot be negative")
        self._value = value
        self._cond = threading.Condition()

    def acquire(self):
        with self._cond:
            while self._value <= 0:
                self._cond.wait()
            self._value -= 1

    def release(self):
        with self._cond:
            self._value += 1
            self._cond.notify()

    def __enter__(self):
        self.acquire(); return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
