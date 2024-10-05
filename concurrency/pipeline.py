"""Multi-stage concurrent pipeline processor."""
from concurrency.blocking_queue import BoundedBlockingQueue
import threading

class PipelineStage:
    def __init__(self, fn, in_q: BoundedBlockingQueue, out_q: BoundedBlockingQueue):
        self.fn = fn
        self.in_q = in_q
        self.out_q = out_q
        self.thread = threading.Thread(target=self._run, daemon=True)

    def start(self): self.thread.start()
    def _run(self):
        while True:
            item = self.in_q.get()
            if item is None:
                self.out_q.put(None)
                break
            self.out_q.put(self.fn(item))
