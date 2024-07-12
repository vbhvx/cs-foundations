"""Binary reflected Gray code implementation."""
def binary_to_gray(n: int) -> int: return n ^ (n >> 1)
def gray_to_binary(g: int) -> int:
    b = 0
    while g > 0: b ^= g; g >>= 1
    return b
