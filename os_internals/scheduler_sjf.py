"""Shortest Job First CPU scheduling algorithm."""
from typing import List
from os_internals.pcb import Process, ProcessState

def schedule_sjf(processes: List[Process]):
    remaining = sorted(processes, key=lambda p: p.arrival_time)
    completed = []
    current_time = 0
    while remaining:
        available = [p for p in remaining if p.arrival_time <= current_time]
        if not available:
            current_time = remaining[0].arrival_time
            continue
        shortest = min(available, key=lambda p: p.burst_time)
        remaining.remove(shortest)
        shortest.waiting_time = current_time - shortest.arrival_time
        current_time += shortest.burst_time
        shortest.completion_time = current_time
        shortest.turnaround_time = shortest.completion_time - shortest.arrival_time
        shortest.state = ProcessState.TERMINATED
        completed.append(shortest)
    return completed
