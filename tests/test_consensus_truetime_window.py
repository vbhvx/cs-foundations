"""Unit test suite for Spanner TrueTime Uncertainty Window (consensus)."""
from consensus.truetime_window import TruetimeWindow

def test_truetime_window_lifecycle():
    obj = TruetimeWindow("test_truetime_window", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_truetime_window"
    assert status["capacity"] == 10

def test_truetime_window_operations():
    obj = TruetimeWindow("test_truetime_window_ops", capacity=5)
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
