"""Leaky bucket rate limiter enforcing constant outflow."""
import time

class LeakyBucket:
    def __init__(self, capacity: int, leak_rate: float):
        self.capacity = capacity
        self.leak_rate = leak_rate  # units leaked per second
        self.water = 0.0
        self.last_leak = time.time()

    def add_drop(self, amount: float = 1.0) -> bool:
        now = time.time()
        elapsed = now - self.last_leak
        self.water = max(0.0, self.water - elapsed * self.leak_rate)
        self.last_leak = now
        if self.water + amount <= self.capacity:
            self.water += amount
            return True
        return False
