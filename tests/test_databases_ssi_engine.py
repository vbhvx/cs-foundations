"""Unit test suite for Serializable Snapshot Isolation (SSI) (databases)."""
from databases.ssi_engine import SsiEngine

def test_ssi_engine_lifecycle():
    obj = SsiEngine("test_ssi_engine", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ssi_engine"
    assert status["capacity"] == 10

def test_ssi_engine_operations():
    obj = SsiEngine("test_ssi_engine_ops", capacity=5)
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
