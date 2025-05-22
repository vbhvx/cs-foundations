"""Unit test suite for Semi-Space Cheney Copying Collector (memory)."""
from memory.cheney_collector import CheneyCollector

def test_cheney_collector_lifecycle():
    obj = CheneyCollector("test_cheney_collector", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_cheney_collector"
    assert status["capacity"] == 10

def test_cheney_collector_operations():
    obj = CheneyCollector("test_cheney_collector_ops", capacity=5)
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
