"""Optimized mathematical operations."""
def fast_pow(base: int, exp: int, mod: int = None) -> int:
    res = 1
    b = base if mod is None else base % mod
    e = exp
    while e > 0:
        if e & 1: res = res * b if mod is None else (res * b) % mod
        b = b * b if mod is None else (b * b) % mod
        e >>= 1
    return res
