from os_internals.pcb import Process
from os_internals.scheduler_priority import schedule_priority
def test_pri(): p = [Process(1, 0, 5, 10)]; assert schedule_priority(p)[0].priority == 10
