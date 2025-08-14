"""Unit test suite for Exchanger Two-Thread Rendezvous Swap (concurrency)."""
from concurrency.thread_exchanger import ThreadExchanger

def test_thread_exchanger_lifecycle():
    obj = ThreadExchanger("test_thread_exchanger", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_thread_exchanger"
    assert status["capacity"] == 10

def test_thread_exchanger_operations():
    obj = ThreadExchanger("test_thread_exchanger_ops", capacity=5)
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
