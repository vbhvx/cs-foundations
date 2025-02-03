"""Unit test suite for Multi-Version Concurrency Control (MVCC) (databases)."""
from databases.mvcc_engine import MvccEngine

def test_mvcc_engine_lifecycle():
    obj = MvccEngine("test_mvcc_engine", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_mvcc_engine"
    assert status["capacity"] == 10

def test_mvcc_engine_operations():
    obj = MvccEngine("test_mvcc_engine_ops", capacity=5)
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
