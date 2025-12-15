"""Unit test suite for Distributed Broadcast Tree Spanning Protocol (distributed)."""
from distributed.broadcast_tree import BroadcastTree

def test_broadcast_tree_lifecycle():
    obj = BroadcastTree("test_broadcast_tree", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_broadcast_tree"
    assert status["capacity"] == 10

def test_broadcast_tree_operations():
    obj = BroadcastTree("test_broadcast_tree_ops", capacity=5)
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
