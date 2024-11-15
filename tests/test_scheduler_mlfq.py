from os_internals.pcb import Process
from os_internals.scheduler_mlfq import MLFQScheduler

def test_mlfq():
    mlfq = MLFQScheduler(3, 2)
    p = Process(1, 0, 10)
    mlfq.add_process(p)
    pid, run_t, done = mlfq.step()
    assert pid == 1 and run_t == 2 and not done
    assert len(mlfq.queues[1]) == 1
