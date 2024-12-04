"""TLB cache simulation for virtual-to-physical address translation."""
from typing import Dict, Tuple, Optional

class TLB:
    def __init__(self, capacity: int = 16):
        self.capacity = capacity
        self.cache: Dict[int, int] = {}
        self.history = []
        self.hits = 0
        self.misses = 0

    def lookup(self, vpn: int) -> Optional[int]:
        if vpn in self.cache:
            self.hits += 1
            self.history.remove(vpn)
            self.history.append(vpn)
            return self.cache[vpn]
        self.misses += 1
        return None

    def insert(self, vpn: int, pfn: int):
        if len(self.cache) >= self.capacity:
            lru = self.history.pop(0)
            del self.cache[lru]
        self.cache[vpn] = pfn
        self.history.append(vpn)
