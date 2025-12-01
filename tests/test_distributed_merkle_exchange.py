"""Unit test suite for Anti-Entropy Active Key Range Merkle Exchange (distributed)."""
from distributed.merkle_exchange import MerkleExchange

def test_merkle_exchange_lifecycle():
    obj = MerkleExchange("test_merkle_exchange", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_merkle_exchange"
    assert status["capacity"] == 10

def test_merkle_exchange_operations():
    obj = MerkleExchange("test_merkle_exchange_ops", capacity=5)
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
