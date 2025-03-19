"""Unit test suite for ChaCha20 Stream Cipher (crypto)."""
from crypto.chacha20 import Chacha20

def test_chacha20_lifecycle():
    obj = Chacha20("test_chacha20", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_chacha20"
    assert status["capacity"] == 10

def test_chacha20_operations():
    obj = Chacha20("test_chacha20_ops", capacity=5)
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
