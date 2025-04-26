"""Unit test suite for Hybrid Logical Clock (HLC) Synchronizer (consensus)."""
from consensus.hlc_clock import HlcClock

def test_hlc_clock_lifecycle():
    obj = HlcClock("test_hlc_clock", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_hlc_clock"
    assert status["capacity"] == 10

def test_hlc_clock_operations():
    obj = HlcClock("test_hlc_clock_ops", capacity=5)
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
