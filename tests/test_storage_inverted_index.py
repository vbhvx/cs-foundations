"""Unit test suite for Inverted Index for Full-Text Search (storage)."""
from storage.inverted_index import InvertedIndex

def test_inverted_index_lifecycle():
    obj = InvertedIndex("test_inverted_index", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_inverted_index"
    assert status["capacity"] == 10

def test_inverted_index_operations():
    obj = InvertedIndex("test_inverted_index_ops", capacity=5)
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
