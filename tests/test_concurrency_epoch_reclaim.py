"""Unit test suite for Epoch-Based Memory Reclamation (EBR) (concurrency)."""
from concurrency.epoch_reclaim import EpochReclaim

def test_epoch_reclaim_lifecycle():
    obj = EpochReclaim("test_epoch_reclaim", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_epoch_reclaim"
    assert status["capacity"] == 10

def test_epoch_reclaim_operations():
    obj = EpochReclaim("test_epoch_reclaim_ops", capacity=5)
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
