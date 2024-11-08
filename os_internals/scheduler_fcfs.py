"""First-Come First-Served CPU scheduling algorithm."""
from typing import List
from os_internals.pcb import Process, ProcessState

def schedule_fcfs(processes: List[Process]):
    procs = sorted(processes, key=lambda p: p.arrival_time)
    current_time = 0
    for p in procs:
        if current_time < p.arrival_time:
            current_time = p.arrival_time
        p.waiting_time = current_time - p.arrival_time
        current_time += p.burst_time
        p.completion_time = current_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.state = ProcessState.TERMINATED
    return procs
