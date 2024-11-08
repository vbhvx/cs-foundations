from os_internals.pcb import Process
from os_internals.scheduler_fcfs import schedule_fcfs

def test_fcfs():
    p1 = Process(1, 0, 5)
    p2 = Process(2, 1, 3)
    schedule_fcfs([p1, p2])
    assert p1.completion_time == 5
    assert p2.completion_time == 8
    assert p2.waiting_time == 4
