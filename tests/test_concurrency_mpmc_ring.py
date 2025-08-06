"""Unit test suite for Lock-Free MPMC Multi-Producer Ring (concurrency)."""
from concurrency.mpmc_ring import MpmcRing

def test_mpmc_ring_lifecycle():
    obj = MpmcRing("test_mpmc_ring", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_mpmc_ring"
    assert status["capacity"] == 10

def test_mpmc_ring_operations():
    obj = MpmcRing("test_mpmc_ring_ops", capacity=5)
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
