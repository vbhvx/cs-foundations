"""Unit test suite for Thread-Local Caching Allocator (TCMalloc) (memory)."""
from memory.tcmalloc_sim import TcmallocSim

def test_tcmalloc_sim_lifecycle():
    obj = TcmallocSim("test_tcmalloc_sim", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_tcmalloc_sim"
    assert status["capacity"] == 10

def test_tcmalloc_sim_operations():
    obj = TcmallocSim("test_tcmalloc_sim_ops", capacity=5)
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
