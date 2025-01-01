"""Bloom Filter using bitarray and k murmur-based hash seeds."""
import math
from foundations.murmur3 import murmur3_32

class BloomFilter:
    def __init__(self, expected_elements: int = 1000, false_positive_rate: float = 0.01):
        self.size = int(- (expected_elements * math.log(false_positive_rate)) / (math.log(2) ** 2))
        self.k = int((self.size / expected_elements) * math.log(2))
        self.bits = bytearray((self.size + 7) // 8)

    def add(self, item: str):
        b = item.encode("utf-8")
        for i in range(self.k):
            bit_idx = murmur3_32(b, seed=i) % self.size
            self.bits[bit_idx // 8] |= (1 << (bit_idx % 8))

    def __contains__(self, item: str) -> bool:
        b = item.encode("utf-8")
        for i in range(self.k):
            bit_idx = murmur3_32(b, seed=i) % self.size
            if not (self.bits[bit_idx // 8] & (1 << (bit_idx % 8))):
                return False
        return True
