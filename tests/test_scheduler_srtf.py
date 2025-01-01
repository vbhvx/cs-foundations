from os_internals.pcb import Process
from os_internals.scheduler_srtf import schedule_srtf
def test_srtf(): p = [Process(1, 0, 5)]; assert len(schedule_srtf(p)) == 1
