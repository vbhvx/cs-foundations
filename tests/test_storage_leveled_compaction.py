"""Unit test suite for Leveled Compaction Strategy (storage)."""
from storage.leveled_compaction import LeveledCompaction

def test_leveled_compaction_lifecycle():
    obj = LeveledCompaction("test_leveled_compaction", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_leveled_compaction"
    assert status["capacity"] == 10

def test_leveled_compaction_operations():
    obj = LeveledCompaction("test_leveled_compaction_ops", capacity=5)
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
