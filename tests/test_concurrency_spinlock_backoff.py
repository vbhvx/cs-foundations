"""Unit test suite for Atomic Flag Spinlock with Exponential Backoff (concurrency)."""
from concurrency.spinlock_backoff import SpinlockBackoff

def test_spinlock_backoff_lifecycle():
    obj = SpinlockBackoff("test_spinlock_backoff", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_spinlock_backoff"
    assert status["capacity"] == 10

def test_spinlock_backoff_operations():
    obj = SpinlockBackoff("test_spinlock_backoff_ops", capacity=5)
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
