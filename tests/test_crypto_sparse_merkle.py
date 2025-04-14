"""Unit test suite for Sparse Merkle Tree Proof Generator (crypto)."""
from crypto.sparse_merkle import SparseMerkle

def test_sparse_merkle_lifecycle():
    obj = SparseMerkle("test_sparse_merkle", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_sparse_merkle"
    assert status["capacity"] == 10

def test_sparse_merkle_operations():
    obj = SparseMerkle("test_sparse_merkle_ops", capacity=5)
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
