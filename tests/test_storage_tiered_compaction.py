"""Unit test suite for Size-Tiered Compaction Strategy (storage)."""
from storage.tiered_compaction import TieredCompaction

def test_tiered_compaction_lifecycle():
    obj = TieredCompaction("test_tiered_compaction", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_tiered_compaction"
    assert status["capacity"] == 10

def test_tiered_compaction_operations():
    obj = TieredCompaction("test_tiered_compaction_ops", capacity=5)
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
