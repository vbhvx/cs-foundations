"""Unit test suite for Prepared Statement Cache (databases)."""
from databases.stmt_cache import StmtCache

def test_stmt_cache_lifecycle():
    obj = StmtCache("test_stmt_cache", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_stmt_cache"
    assert status["capacity"] == 10

def test_stmt_cache_operations():
    obj = StmtCache("test_stmt_cache_ops", capacity=5)
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
