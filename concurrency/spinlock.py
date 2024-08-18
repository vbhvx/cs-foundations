"""User-space spinlock implementation using atomic flags."""
import threading, time

class SpinLock:
    def __init__(self):
        self._lock = threading.Lock()
        self._locked = False

    def acquire(self):
        while True:
            with self._lock:
                if not self._locked:
                    self._locked = True
                    return True
            time.sleep(0.0001)

    def release(self):
        with self._lock:
            if not self._locked:
                raise RuntimeError("Cannot release unacquired lock")
            self._locked = False

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
