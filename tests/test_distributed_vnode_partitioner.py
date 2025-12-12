"""Unit test suite for Virtual Node Range Token Partitioner (distributed)."""
from distributed.vnode_partitioner import VnodePartitioner

def test_vnode_partitioner_lifecycle():
    obj = VnodePartitioner("test_vnode_partitioner", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_vnode_partitioner"
    assert status["capacity"] == 10

def test_vnode_partitioner_operations():
    obj = VnodePartitioner("test_vnode_partitioner_ops", capacity=5)
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
