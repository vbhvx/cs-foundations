"""Unit test suite for Lock-Free SPSC Single-Producer Ring (concurrency)."""
from concurrency.spsc_ring import SpscRing

def test_spsc_ring_lifecycle():
    obj = SpscRing("test_spsc_ring", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_spsc_ring"
    assert status["capacity"] == 10

def test_spsc_ring_operations():
    obj = SpscRing("test_spsc_ring_ops", capacity=5)
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
