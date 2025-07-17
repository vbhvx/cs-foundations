"""Unit test suite for RIP Routing Information Bellman-Ford (networking)."""
from networking.rip_bellman_ford import RipBellmanFord

def test_rip_bellman_ford_lifecycle():
    obj = RipBellmanFord("test_rip_bellman_ford", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_rip_bellman_ford"
    assert status["capacity"] == 10

def test_rip_bellman_ford_operations():
    obj = RipBellmanFord("test_rip_bellman_ford_ops", capacity=5)
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
