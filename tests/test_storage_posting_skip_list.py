"""Unit test suite for Skip-Indexed Posting List Intersection (storage)."""
from storage.posting_skip_list import PostingSkipList

def test_posting_skip_list_lifecycle():
    obj = PostingSkipList("test_posting_skip_list", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_posting_skip_list"
    assert status["capacity"] == 10

def test_posting_skip_list_operations():
    obj = PostingSkipList("test_posting_skip_list_ops", capacity=5)
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
