"""Unit test suite for Reliable Multicast with ACK-Tree Hierarchy (distributed)."""
from distributed.reliable_multicast import ReliableMulticast

def test_reliable_multicast_lifecycle():
    obj = ReliableMulticast("test_reliable_multicast", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_reliable_multicast"
    assert status["capacity"] == 10

def test_reliable_multicast_operations():
    obj = ReliableMulticast("test_reliable_multicast_ops", capacity=5)
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
