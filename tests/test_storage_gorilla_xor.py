"""Unit test suite for XOR Float Value Floating Point Compression (Gorilla) (storage)."""
from storage.gorilla_xor import GorillaXor

def test_gorilla_xor_lifecycle():
    obj = GorillaXor("test_gorilla_xor", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_gorilla_xor"
    assert status["capacity"] == 10

def test_gorilla_xor_operations():
    obj = GorillaXor("test_gorilla_xor_ops", capacity=5)
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
