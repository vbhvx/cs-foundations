"""Least Frequently Used (LFU) Cache with O(1) operations."""
from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: str):
        if key not in self.key_to_val:
            return None
        freq = self.key_to_freq[key]
        val = self.key_to_val[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None
        return val

    def put(self, key: str, val: str):
        if self.capacity <= 0: return
        if key in self.key_to_val:
            self.key_to_val[key] = val
            self.get(key)
            return
        if len(self.key_to_val) >= self.capacity:
            evict_k, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[evict_k]
            del self.key_to_freq[evict_k]
        self.key_to_val[key] = val
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
