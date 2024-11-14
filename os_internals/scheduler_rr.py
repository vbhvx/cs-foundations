"""Round Robin preemptive CPU scheduler with time quantum."""
from typing import List
from collections import deque
from os_internals.pcb import Process, ProcessState

def schedule_rr(processes: List[Process], quantum: int):
    procs = sorted(processes, key=lambda p: p.arrival_time)
    ready_queue = deque()
    current_time = 0
    idx = 0
    completed = []
    while idx < len(procs) or ready_queue:
        while idx < len(procs) and procs[idx].arrival_time <= current_time:
            ready_queue.append(procs[idx])
            idx += 1
        if not ready_queue:
            current_time = procs[idx].arrival_time
            continue
        cur = ready_queue.popleft()
        exec_time = min(quantum, cur.remaining_time)
        cur.remaining_time -= exec_time
        current_time += exec_time
        while idx < len(procs) and procs[idx].arrival_time <= current_time:
            ready_queue.append(procs[idx])
            idx += 1
        if cur.remaining_time == 0:
            cur.completion_time = current_time
            cur.turnaround_time = cur.completion_time - cur.arrival_time
            cur.waiting_time = cur.turnaround_time - cur.burst_time
            cur.state = ProcessState.TERMINATED
            completed.append(cur)
        else:
            ready_queue.append(cur)
    return completed
