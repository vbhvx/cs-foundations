"""Unit test suite for Baker Real-Time Treadmill Collector (memory)."""
from memory.baker_treadmill import BakerTreadmill

def test_baker_treadmill_lifecycle():
    obj = BakerTreadmill("test_baker_treadmill", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_baker_treadmill"
    assert status["capacity"] == 10

def test_baker_treadmill_operations():
    obj = BakerTreadmill("test_baker_treadmill_ops", capacity=5)
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
