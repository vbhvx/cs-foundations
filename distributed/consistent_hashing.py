"""Consistent Hashing ring for distributed partitioning."""
import hashlib
from bisect import bisect_right

class ConsistentHashRing:
    def __init__(self, replicas: int = 100):
        self.replicas = replicas
        self.ring = []
        self.ring_map = {}
        self.nodes = set()

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)

    def add_node(self, node: str):
        self.nodes.add(node)
        for i in range(self.replicas):
            v_key = f"{node}#v{i}"
            h = self._hash(v_key)
            self.ring.append(h)
            self.ring_map[h] = node
        self.ring.sort()

    def remove_node(self, node: str):
        self.nodes.remove(node)
        new_ring = []
        for h in self.ring:
            if self.ring_map[h] == node:
                del self.ring_map[h]
            else:
                new_ring.append(h)
        self.ring = new_ring

    def get_node(self, key: str) -> str:
        if not self.ring: return None
        h = self._hash(key)
        idx = bisect_right(self.ring, h)
        if idx == len(self.ring):
            idx = 0
        return self.ring_map[self.ring[idx]]
