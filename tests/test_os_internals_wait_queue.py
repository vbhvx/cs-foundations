"""Unit test suite for Wait Queue & Sleeping Lock Thread Wakeup (os_internals)."""
from os_internals.wait_queue import WaitQueue

def test_wait_queue_lifecycle():
    obj = WaitQueue("test_wait_queue", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_wait_queue"
    assert status["capacity"] == 10

def test_wait_queue_operations():
    obj = WaitQueue("test_wait_queue_ops", capacity=5)
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
