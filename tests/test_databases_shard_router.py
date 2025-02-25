"""Unit test suite for Distributed Hash Shard Router (databases)."""
from databases.shard_router import ShardRouter

def test_shard_router_lifecycle():
    obj = ShardRouter("test_shard_router", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_shard_router"
    assert status["capacity"] == 10

def test_shard_router_operations():
    obj = ShardRouter("test_shard_router_ops", capacity=5)
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
