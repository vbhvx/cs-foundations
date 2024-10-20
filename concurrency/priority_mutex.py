"""Priority-aware mutex tracking holding thread priority."""
import threading

class PriorityMutex:
    def __init__(self):
        self._lock = threading.Lock()
        self.holding_priority = 0
        self.owner = None

    def acquire(self, priority: int):
        self._lock.acquire()
        self.holding_priority = priority
        self.owner = threading.get_ident()

    def release(self):
        self.holding_priority = 0
        self.owner = None
        self._lock.release()
