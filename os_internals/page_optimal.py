"""Optimal page replacement algorithm (Belady's MIN)."""
from typing import List

def simulate_optimal_page_replacement(pages: List[int], frames_count: int) -> int:
    frames = []
    faults = 0
    for i, p in enumerate(pages):
        if p not in frames:
            faults += 1
            if len(frames) < frames_count:
                frames.append(p)
            else:
                # Find frame page with farthest next occurrence
                farthest = -1
                victim = -1
                for f in frames:
                    try:
                        nxt = pages.index(f, i + 1)
                    except ValueError:
                        nxt = float('inf')
                    if nxt > farthest:
                        farthest = nxt
                        victim = f
                frames.remove(victim)
                frames.append(p)
    return faults
