"""Unit test suite for Event-Driven Async Reactor Loop (concurrency)."""
from concurrency.async_reactor import AsyncReactor

def test_async_reactor_lifecycle():
    obj = AsyncReactor("test_async_reactor", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_async_reactor"
    assert status["capacity"] == 10

def test_async_reactor_operations():
    obj = AsyncReactor("test_async_reactor_ops", capacity=5)
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
