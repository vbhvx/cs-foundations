"""Unit test suite for Pedersen Commitment Scheme (crypto)."""
from crypto.pedersen_commit import PedersenCommit

def test_pedersen_commit_lifecycle():
    obj = PedersenCommit("test_pedersen_commit", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_pedersen_commit"
    assert status["capacity"] == 10

def test_pedersen_commit_operations():
    obj = PedersenCommit("test_pedersen_commit_ops", capacity=5)
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
