"""Merkle Tree computation and leaf audit verification."""
import hashlib
from typing import List

def _hash(val: str) -> str:
    return hashlib.sha256(val.encode("utf-8")).hexdigest()

class MerkleTree:
    def __init__(self, leaves: List[str]):
        self.leaves = leaves
        self.tree = []
        self._build()

    def _build(self):
        current = [_hash(l) for l in self.leaves]
        self.tree.append(current)
        while len(current) > 1:
            nxt = []
            for i in range(0, len(current), 2):
                left = current[i]
                right = current[i+1] if i + 1 < len(current) else left
                nxt.append(_hash(left + right))
            current = nxt
            self.tree.append(current)

    def root(self) -> str:
        return self.tree[-1][0] if self.tree else ""
