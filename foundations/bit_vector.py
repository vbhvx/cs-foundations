"""Dynamically expandable bit array vector."""

class BitVector:
    def __init__(self, size: int = 64):
        self.size = size
        self.words = [0] * ((size + 63) // 64)

    def set(self, idx: int):
        w_idx = idx // 64
        bit_idx = idx % 64
        self.words[w_idx] |= (1 << bit_idx)

    def get(self, idx: int) -> bool:
        w_idx = idx // 64
        bit_idx = idx % 64
        return bool((self.words[w_idx] >> bit_idx) & 1)

    def clear(self, idx: int):
        w_idx = idx // 64
        bit_idx = idx % 64
        self.words[w_idx] &= ~(1 << bit_idx)
