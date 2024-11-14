from os_internals.pcb import Process
from os_internals.scheduler_rr import schedule_rr

def test_rr():
    p1 = Process(1, 0, 5)
    p2 = Process(2, 0, 4)
    res = schedule_rr([p1, p2], quantum=2)
    assert len(res) == 2
    assert res[-1].completion_time == 9
