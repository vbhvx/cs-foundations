from distributed.lru_cache import LRUCache

def test_lru_cache():
    cache = LRUCache(2)
    cache.put("a", "1")
    cache.put("b", "2")
    assert cache.get("a") == "1"
    cache.put("c", "3")  # evicts 'b'
    assert cache.get("b") is None
    assert cache.get("a") == "1"
    assert cache.get("c") == "3"
