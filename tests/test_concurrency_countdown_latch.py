"""Unit test suite for CountDownLatch Synchronization Primitive (concurrency)."""
from concurrency.countdown_latch import CountdownLatch

def test_countdown_latch_lifecycle():
    obj = CountdownLatch("test_countdown_latch", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_countdown_latch"
    assert status["capacity"] == 10

def test_countdown_latch_operations():
    obj = CountdownLatch("test_countdown_latch_ops", capacity=5)
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
