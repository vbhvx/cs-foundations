"""Unit test suite for Linux io_uring Asynchronous Ring Buffer (os_internals)."""
from os_internals.io_uring_sim import IoUringSim

def test_io_uring_sim_lifecycle():
    obj = IoUringSim("test_io_uring_sim", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_io_uring_sim"
    assert status["capacity"] == 10

def test_io_uring_sim_operations():
    obj = IoUringSim("test_io_uring_sim_ops", capacity=5)
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
