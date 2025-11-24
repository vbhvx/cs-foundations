"""Unit test suite for Dynamo-Style Sloppy Quorum and Hinted Handoff (distributed)."""
from distributed.sloppy_quorum import SloppyQuorum

def test_sloppy_quorum_lifecycle():
    obj = SloppyQuorum("test_sloppy_quorum", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_sloppy_quorum"
    assert status["capacity"] == 10

def test_sloppy_quorum_operations():
    obj = SloppyQuorum("test_sloppy_quorum_ops", capacity=5)
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
