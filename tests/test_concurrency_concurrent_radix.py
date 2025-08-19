"""Unit test suite for Read-Mostly Concurrent Radix Tree (concurrency)."""
from concurrency.concurrent_radix import ConcurrentRadix

def test_concurrent_radix_lifecycle():
    obj = ConcurrentRadix("test_concurrent_radix", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_concurrent_radix"
    assert status["capacity"] == 10

def test_concurrent_radix_operations():
    obj = ConcurrentRadix("test_concurrent_radix_ops", capacity=5)
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
