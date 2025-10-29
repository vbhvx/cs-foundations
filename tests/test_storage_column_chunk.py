"""Unit test suite for Columnar Chunk Page Header & Footer (storage)."""
from storage.column_chunk import ColumnChunk

def test_column_chunk_lifecycle():
    obj = ColumnChunk("test_column_chunk", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_column_chunk"
    assert status["capacity"] == 10

def test_column_chunk_operations():
    obj = ColumnChunk("test_column_chunk_ops", capacity=5)
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
