"""Unit test suite for Zero-Knowledge Range Proof (Bulletproofs) (crypto)."""
from crypto.zk_range_proof import ZkRangeProof

def test_zk_range_proof_lifecycle():
    obj = ZkRangeProof("test_zk_range_proof", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_zk_range_proof"
    assert status["capacity"] == 10

def test_zk_range_proof_operations():
    obj = ZkRangeProof("test_zk_range_proof_ops", capacity=5)
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
