"""Unit test suite for Columnar Chunk Compression (databases)."""
from databases.column_store import ColumnStore

def test_column_store_lifecycle():
    obj = ColumnStore("test_column_store", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_column_store"
    assert status["capacity"] == 10

def test_column_store_operations():
    obj = ColumnStore("test_column_store_ops", capacity=5)
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
