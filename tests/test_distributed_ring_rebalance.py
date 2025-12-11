"""Unit test suite for Consistent Hash Ring Node Weight Rebalance (distributed)."""
from distributed.ring_rebalance import RingRebalance

def test_ring_rebalance_lifecycle():
    obj = RingRebalance("test_ring_rebalance", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ring_rebalance"
    assert status["capacity"] == 10

def test_ring_rebalance_operations():
    obj = RingRebalance("test_ring_rebalance_ops", capacity=5)
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
