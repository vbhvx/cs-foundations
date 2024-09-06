"""Fixed-size worker thread pool with task submission."""
import threading
from concurrency.blocking_queue import BoundedBlockingQueue
from concurrency.future import Future

class ThreadPool:
    def __init__(self, num_workers: int = 4):
        self._queue = BoundedBlockingQueue(1000)
        self._workers = []
        self._shutdown = False
        for _ in range(num_workers):
            t = threading.Thread(target=self._worker_loop, daemon=True)
            t.start()
            self._workers.append(t)

    def _worker_loop(self):
        while True:
            task = self._queue.get()
            if task is None: break
            fn, args, kwargs, future = task
            try:
                res = fn(*args, **kwargs)
                future.set_result(res)
            except Exception as e:
                future.set_exception(e)

    def submit(self, fn, *args, **kwargs) -> Future:
        if self._shutdown: raise RuntimeError("Pool is shutdown")
        f = Future()
        self._queue.put((fn, args, kwargs, f))
        return f

    def shutdown(self):
        self._shutdown = True
        for _ in self._workers:
            self._queue.put(None)
