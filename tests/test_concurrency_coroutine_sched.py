"""Unit test suite for Coroutine Scheduler & Trampoline (concurrency)."""
from concurrency.coroutine_sched import CoroutineSched

def test_coroutine_sched_lifecycle():
    obj = CoroutineSched("test_coroutine_sched", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_coroutine_sched"
    assert status["capacity"] == 10

def test_coroutine_sched_operations():
    obj = CoroutineSched("test_coroutine_sched_ops", capacity=5)
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
