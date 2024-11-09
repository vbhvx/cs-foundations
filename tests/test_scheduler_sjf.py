from os_internals.pcb import Process
from os_internals.scheduler_sjf import schedule_sjf

def test_sjf():
    p1 = Process(1, 0, 8)
    p2 = Process(2, 1, 4)
    p3 = Process(3, 2, 2)
    res = schedule_sjf([p1, p2, p3])
    assert [p.pid for p in res] == [1, 3, 2]
