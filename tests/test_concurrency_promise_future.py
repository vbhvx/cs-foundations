"""Unit test suite for Async Promise & Future State Deferred (concurrency)."""
from concurrency.promise_future import PromiseFuture

def test_promise_future_lifecycle():
    obj = PromiseFuture("test_promise_future", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_promise_future"
    assert status["capacity"] == 10

def test_promise_future_operations():
    obj = PromiseFuture("test_promise_future_ops", capacity=5)
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
