"""Galois Linear Feedback Shift Register pseudo-random generator."""

class LFSR16:
    def __init__(self, seed: int = 0xACE1):
        self.state = seed & 0xFFFF

    def next_bit(self) -> int:
        bit = ((self.state >> 0) ^ (self.state >> 2) ^ (self.state >> 3) ^ (self.state >> 5)) & 1
        self.state = (self.state >> 1) | (bit << 15)
        return bit
