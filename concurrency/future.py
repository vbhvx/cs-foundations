"""Promise/Future pattern for deferred result computation."""
import threading

class Future:
    def __init__(self):
        self._result = None
        self._exception = None
        self._done = False
        self._cond = threading.Condition()

    def set_result(self, val):
        with self._cond:
            if self._done: raise RuntimeError("Future already done")
            self._result = val
            self._done = True
            self._cond.notify_all()

    def set_exception(self, exc):
        with self._cond:
            if self._done: raise RuntimeError("Future already done")
            self._exception = exc
            self._done = True
            self._cond.notify_all()

    def result(self, timeout=None):
        with self._cond:
            if not self._done:
                self._cond.wait(timeout)
            if not self._done: raise TimeoutError("Future timed out")
            if self._exception: raise self._exception
            return self._result
