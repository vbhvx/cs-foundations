"""Thread-safe bounded queue with blocking operations."""
import threading
from collections import deque

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        if capacity <= 0: raise ValueError("Capacity must be positive")
        self._capacity = capacity
        self._queue = deque()
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        self._not_full = threading.Condition(self._lock)

    def put(self, item):
        with self._not_full:
            while len(self._queue) >= self._capacity:
                self._not_full.wait()
            self._queue.append(item)
            self._not_empty.notify()

    def get(self):
        with self._not_empty:
            while not self._queue:
                self._not_empty.wait()
            item = self._queue.popleft()
            self._not_full.notify()
            return item

    def size(self) -> int:
        with self._lock:
            return len(self._queue)
