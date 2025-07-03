"""Unit test suite for Nagle Algorithm Packet Coalescer (networking)."""
from networking.nagle_algo import NagleAlgo

def test_nagle_algo_lifecycle():
    obj = NagleAlgo("test_nagle_algo", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_nagle_algo"
    assert status["capacity"] == 10

def test_nagle_algo_operations():
    obj = NagleAlgo("test_nagle_algo_ops", capacity=5)
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
