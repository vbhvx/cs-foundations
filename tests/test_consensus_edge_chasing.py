"""Unit test suite for Distributed Deadlock Edge Chasing (consensus)."""
from consensus.edge_chasing import EdgeChasing

def test_edge_chasing_lifecycle():
    obj = EdgeChasing("test_edge_chasing", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_edge_chasing"
    assert status["capacity"] == 10

def test_edge_chasing_operations():
    obj = EdgeChasing("test_edge_chasing_ops", capacity=5)
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
