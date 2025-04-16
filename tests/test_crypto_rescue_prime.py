"""Unit test suite for Rescue Prime Arithmetization Cipher (crypto)."""
from crypto.rescue_prime import RescuePrime

def test_rescue_prime_lifecycle():
    obj = RescuePrime("test_rescue_prime", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_rescue_prime"
    assert status["capacity"] == 10

def test_rescue_prime_operations():
    obj = RescuePrime("test_rescue_prime_ops", capacity=5)
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
