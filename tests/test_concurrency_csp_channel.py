"""Unit test suite for CSP (Communicating Sequential Processes) Channel (concurrency)."""
from concurrency.csp_channel import CspChannel

def test_csp_channel_lifecycle():
    obj = CspChannel("test_csp_channel", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_csp_channel"
    assert status["capacity"] == 10

def test_csp_channel_operations():
    obj = CspChannel("test_csp_channel_ops", capacity=5)
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
