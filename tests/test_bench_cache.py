from benchmarks.bench_cache import evaluate_cache_hit_ratio
from distributed.lru_cache import LRUCache

def test_cache_hit_eval():
    seq = ["a", "b", "a", "c", "a"]
    ratio = evaluate_cache_hit_ratio(LRUCache, 2, seq)
    assert ratio > 0.0
