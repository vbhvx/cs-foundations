"""Unit test suite for Grace Hash Join Operator (databases)."""
from databases.grace_hash_join import GraceHashJoin

def test_grace_hash_join_lifecycle():
    obj = GraceHashJoin("test_grace_hash_join", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_grace_hash_join"
    assert status["capacity"] == 10

def test_grace_hash_join_operations():
    obj = GraceHashJoin("test_grace_hash_join_ops", capacity=5)
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
