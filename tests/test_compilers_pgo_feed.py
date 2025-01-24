"""Unit test suite for Profile-Guided Optimization (PGO) Feed (compilers)."""
from compilers.pgo_feed import PgoFeed

def test_pgo_feed_lifecycle():
    obj = PgoFeed("test_pgo_feed", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_pgo_feed"
    assert status["capacity"] == 10

def test_pgo_feed_operations():
    obj = PgoFeed("test_pgo_feed_ops", capacity=5)
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
