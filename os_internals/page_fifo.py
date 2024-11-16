"""First-In First-Out page replacement simulation."""
from typing import List

def simulate_fifo_page_replacement(pages: List[int], frames_count: int) -> int:
    frames = []
    faults = 0
    for p in pages:
        if p not in frames:
            faults += 1
            if len(frames) >= frames_count:
                frames.pop(0)
            frames.append(p)
    return faults
