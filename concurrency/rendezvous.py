"""Zero-capacity synchronous rendezvous channel."""
import threading

class RendezvousChannel:
    def __init__(self):
        self._lock = threading.Lock()
        self._put_cond = threading.Condition(self._lock)
        self._get_cond = threading.Condition(self._lock)
        self._data = None
        self._has_data = False

    def send(self, val):
        with self._lock:
            while self._has_data:
                self._put_cond.wait()
            self._data = val
            self._has_data = True
            self._get_cond.notify()
            while self._has_data:
                self._put_cond.wait()

    def receive(self):
        with self._lock:
            while not self._has_data:
                self._get_cond.wait()
            val = self._data
            self._has_data = False
            self._data = None
            self._put_cond.notify()
            return val
