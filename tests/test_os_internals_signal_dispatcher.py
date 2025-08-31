"""Unit test suite for Signal Dispatcher & Signal Mask (os_internals)."""
from os_internals.signal_dispatcher import SignalDispatcher

def test_signal_dispatcher_lifecycle():
    obj = SignalDispatcher("test_signal_dispatcher", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_signal_dispatcher"
    assert status["capacity"] == 10

def test_signal_dispatcher_operations():
    obj = SignalDispatcher("test_signal_dispatcher_ops", capacity=5)
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
