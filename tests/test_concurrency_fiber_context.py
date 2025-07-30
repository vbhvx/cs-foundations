"""Unit test suite for Fiber Execution Context Switch (concurrency)."""
from concurrency.fiber_context import FiberContext

def test_fiber_context_lifecycle():
    obj = FiberContext("test_fiber_context", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_fiber_context"
    assert status["capacity"] == 10

def test_fiber_context_operations():
    obj = FiberContext("test_fiber_context_ops", capacity=5)
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
