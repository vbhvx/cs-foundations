"""Unit test suite for Conflict-Free Record Merger (databases)."""
from databases.record_merger import RecordMerger

def test_record_merger_lifecycle():
    obj = RecordMerger("test_record_merger", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_record_merger"
    assert status["capacity"] == 10

def test_record_merger_operations():
    obj = RecordMerger("test_record_merger_ops", capacity=5)
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
