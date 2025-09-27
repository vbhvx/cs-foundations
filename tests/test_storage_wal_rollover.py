"""Unit test suite for Write-Ahead Log Segment Rollover (storage)."""
from storage.wal_rollover import WalRollover

def test_wal_rollover_lifecycle():
    obj = WalRollover("test_wal_rollover", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_wal_rollover"
    assert status["capacity"] == 10

def test_wal_rollover_operations():
    obj = WalRollover("test_wal_rollover_ops", capacity=5)
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
