"""Unit test suite for Consistent Hashing Ring with Virtual Nodes (distributed)."""
from distributed.consistent_hash_vnodes import ConsistentHashVnodes

def test_consistent_hash_vnodes_lifecycle():
    obj = ConsistentHashVnodes("test_consistent_hash_vnodes", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_consistent_hash_vnodes"
    assert status["capacity"] == 10

def test_consistent_hash_vnodes_operations():
    obj = ConsistentHashVnodes("test_consistent_hash_vnodes_ops", capacity=5)
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
