"""Unit test suite for Fixed-Size Block Page Cache Slab (memory)."""
from memory.page_cache_slab import PageCacheSlab

def test_page_cache_slab_lifecycle():
    obj = PageCacheSlab("test_page_cache_slab", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_page_cache_slab"
    assert status["capacity"] == 10

def test_page_cache_slab_operations():
    obj = PageCacheSlab("test_page_cache_slab_ops", capacity=5)
    ok, res = obj.execute("k1", 100)
    assert ok is True
    assert res == 100
    assert obj.query("k1") == 100
    assert obj.size() == 1
    
    # Overwrite
    ok, res = obj.execute("k1", 200)
    assert ok is True
    assert obj.query("k1") == 200
    assert obj.size() == 1
    
    # Reset
    obj.reset()
    assert obj.size() == 0
