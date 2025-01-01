"""Sparse bit set for high-cardinality indexing."""

class SparseBitSet:
    def __init__(self):
        self.chunks = {}

    def add(self, bit: int):
        chunk = bit // 64
        offset = bit % 64
        self.chunks[chunk] = self.chunks.get(chunk, 0) | (1 << offset)

    def contains(self, bit: int) -> bool:
        chunk = bit // 64
        offset = bit % 64
        return bool((self.chunks.get(chunk, 0) >> offset) & 1)
