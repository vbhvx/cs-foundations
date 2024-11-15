"""Multi-Level Feedback Queue (MLFQ) scheduling simulator."""
from collections import deque
from os_internals.pcb import Process

class MLFQScheduler:
    def __init__(self, num_queues: int = 3, base_quantum: int = 2):
        self.queues = [deque() for _ in range(num_queues)]
        self.quantums = [base_quantum * (2 ** i) for i in range(num_queues)]

    def add_process(self, p: Process):
        self.queues[0].append(p)

    def step(self):
        for lvl, q in enumerate(self.queues):
            if q:
                p = q.popleft()
                qnt = self.quantums[lvl]
                run_time = min(p.remaining_time, qnt)
                p.remaining_time -= run_time
                if p.remaining_time > 0 and lvl < len(self.queues) - 1:
                    self.queues[lvl + 1].append(p)
                elif p.remaining_time > 0:
                    self.queues[lvl].append(p)
                return p.pid, run_time, p.remaining_time == 0
        return None, 0, True
