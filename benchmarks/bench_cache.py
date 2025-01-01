"""Benchmark cache hit-rates under Zipfian access distributions."""
from distributed.lru_cache import LRUCache
from distributed.lfu_cache import LFUCache

def evaluate_cache_hit_ratio(cache_cls, capacity: int, access_sequence: list) -> float:
    c = cache_cls(capacity)
    hits = 0
    for k in access_sequence:
        if c.get(k) is not None:
            hits += 1
        else:
            c.put(k, "val")
    return hits / len(access_sequence) if access_sequence else 0.0
