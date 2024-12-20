"""Banker's Algorithm for safe resource allocation state checking."""
from typing import List

def is_safe_state(available: List[int], max_need: List[List[int]], allocated: List[List[int]]) -> bool:
    n_procs = len(allocated)
    n_res = len(available)
    work = list(available)
    finish = [False] * n_procs
    need = [[max_need[i][j] - allocated[i][j] for j in range(n_res)] for i in range(n_procs)]

    while True:
        found = False
        for i in range(n_procs):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(n_res)):
                for j in range(n_res):
                    work[j] += allocated[i][j]
                finish[i] = True
                found = True
                break
        if not found: break
    return all(finish)
