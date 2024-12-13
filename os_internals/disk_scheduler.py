"""Disk arm scheduling algorithms: FCFS and Shortest Seek Time First."""
from typing import List

def disk_fcfs(requests: List[int], initial_head: int) -> int:
    head = initial_head
    total_seek = 0
    for r in requests:
        total_seek += abs(r - head)
        head = r
    return total_seek

def disk_sstf(requests: List[int], initial_head: int) -> int:
    head = initial_head
    reqs = list(requests)
    total_seek = 0
    while reqs:
        closest = min(reqs, key=lambda r: abs(r - head))
        total_seek += abs(closest - head)
        head = closest
        reqs.remove(closest)
    return total_seek
