"""SCAN and Circular SCAN (C-SCAN) disk scheduling."""
from typing import List

def disk_scan(requests: List[int], initial_head: int, disk_size: int = 200) -> int:
    left = sorted([r for r in requests if r < initial_head])
    right = sorted([r for r in requests if r >= initial_head])
    # Moving towards right, then reversing
    seek = (disk_size - 1 - initial_head)
    if left:
        seek += (disk_size - 1 - left[0])
    return seek
