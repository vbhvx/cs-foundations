"""Unit test suite for Poseidon Algebraic Hash Function (crypto)."""
from crypto.poseidon_hash import PoseidonHash

def test_poseidon_hash_lifecycle():
    obj = PoseidonHash("test_poseidon_hash", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_poseidon_hash"
    assert status["capacity"] == 10

def test_poseidon_hash_operations():
    obj = PoseidonHash("test_poseidon_hash_ops", capacity=5)
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
