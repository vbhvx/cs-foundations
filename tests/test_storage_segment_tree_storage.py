"""Unit test suite for Segment Tree Interval Query Storage (storage)."""
from storage.segment_tree_storage import SegmentTreeStorage

def test_segment_tree_storage_lifecycle():
    obj = SegmentTreeStorage("test_segment_tree_storage", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_segment_tree_storage"
    assert status["capacity"] == 10

def test_segment_tree_storage_operations():
    obj = SegmentTreeStorage("test_segment_tree_storage_ops", capacity=5)
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
