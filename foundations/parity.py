def parity(n: int) -> int:
    p = 0
    while n:
        p ^= 1
        n &= (n - 1)
    return p
