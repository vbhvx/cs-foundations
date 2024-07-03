"""Bit manipulation algorithms and bitwise operations."""
def popcount_naive(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
def popcount_brian_kernighan(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
