"""Clock / Second-Chance page replacement algorithm."""
from typing import List

def simulate_clock_page_replacement(pages: List[int], frames_count: int) -> int:
    frames = [-1] * frames_count
    ref_bits = [0] * frames_count
    hand = 0
    faults = 0
    for p in pages:
        if p in frames:
            idx = frames.index(p)
            ref_bits[idx] = 1
        else:
            faults += 1
            while ref_bits[hand] == 1:
                ref_bits[hand] = 0
                hand = (hand + 1) % frames_count
            frames[hand] = p
            ref_bits[hand] = 1
            hand = (hand + 1) % frames_count
    return faults
