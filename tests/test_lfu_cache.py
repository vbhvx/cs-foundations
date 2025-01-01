from distributed.lfu_cache import LFUCache

def test_lfu_cache():
    cache = LFUCache(2)
    cache.put("a", "1")
    cache.put("b", "2")
    assert cache.get("a") == "1"  # a freq=2, b freq=1
    cache.put("c", "3")  # evicts 'b'
    assert cache.get("b") is None
    assert cache.get("a") == "1"
