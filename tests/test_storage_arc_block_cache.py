"""Unit test suite for Block Cache LRU with ARC Adaptive Replacement (storage)."""
from storage.arc_block_cache import ArcBlockCache

def test_arc_block_cache_lifecycle():
    obj = ArcBlockCache("test_arc_block_cache", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_arc_block_cache"
    assert status["capacity"] == 10

def test_arc_block_cache_operations():
    obj = ArcBlockCache("test_arc_block_cache_ops", capacity=5)
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
