"""Fair FIFO ticket lock preventing starvation."""
import threading, time

class TicketLock:
    def __init__(self):
        self._next_ticket = 0
        self._now_serving = 0
        self._lock = threading.Lock()

    def acquire(self) -> int:
        with self._lock:
            my_ticket = self._next_ticket
            self._next_ticket += 1
        while True:
            with self._lock:
                if self._now_serving == my_ticket:
                    return my_ticket
            time.sleep(0.0001)

    def release(self):
        with self._lock:
            self._now_serving += 1
