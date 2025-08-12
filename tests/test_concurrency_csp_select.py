"""Unit test suite for Select Multiplexer on Concurrent Channels (concurrency)."""
from concurrency.csp_select import CspSelect

def test_csp_select_lifecycle():
    obj = CspSelect("test_csp_select", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_csp_select"
    assert status["capacity"] == 10

def test_csp_select_operations():
    obj = CspSelect("test_csp_select_ops", capacity=5)
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
