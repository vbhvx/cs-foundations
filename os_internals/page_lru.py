"""Least Recently Used page replacement simulation."""
from typing import List

def simulate_lru_page_replacement(pages: List[int], frames_count: int) -> int:
    frames = []
    faults = 0
    for p in pages:
        if p in frames:
            frames.remove(p)
            frames.append(p)
        else:
            faults += 1
            if len(frames) >= frames_count:
                frames.pop(0)
            frames.append(p)
    return faults
