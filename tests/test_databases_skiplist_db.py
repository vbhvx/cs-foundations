"""Unit test suite for SkipList In-Memory Index (databases)."""
from databases.skiplist_db import SkiplistDb

def test_skiplist_db_lifecycle():
    obj = SkiplistDb("test_skiplist_db", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_skiplist_db"
    assert status["capacity"] == 10

def test_skiplist_db_operations():
    obj = SkiplistDb("test_skiplist_db_ops", capacity=5)
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
