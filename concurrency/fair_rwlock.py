"""Fair FIFO Reader-Writer Lock."""
import threading

class FairReadWriteLock:
    def __init__(self):
        self._lock = threading.Lock()
        self._cond = threading.Condition(self._lock)
        self._active_readers = 0
        self._writer_active = False
        self._wait_queue = []

    def acquire_read(self):
        with self._lock:
            ident = object()
            self._wait_queue.append((ident, 'R'))
            while self._writer_active or self._wait_queue[0][0] is not ident:
                self._cond.wait()
            self._wait_queue.pop(0)
            self._active_readers += 1
            self._cond.notify_all()

    def release_read(self):
        with self._lock:
            self._active_readers -= 1
            self._cond.notify_all()
