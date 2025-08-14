"""Unit test suite for External Sort-Merge Join (databases)."""
from databases.sort_merge_join import SortMergeJoin

def test_sort_merge_join_lifecycle():
    obj = SortMergeJoin("test_sort_merge_join", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_sort_merge_join"
    assert status["capacity"] == 10

def test_sort_merge_join_operations():
    obj = SortMergeJoin("test_sort_merge_join_ops", capacity=5)
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
