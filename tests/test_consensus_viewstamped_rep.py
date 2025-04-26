"""Unit test suite for Viewstamped Replication (VR) Protocol (consensus)."""
from consensus.viewstamped_rep import ViewstampedRep

def test_viewstamped_rep_lifecycle():
    obj = ViewstampedRep("test_viewstamped_rep", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_viewstamped_rep"
    assert status["capacity"] == 10

def test_viewstamped_rep_operations():
    obj = ViewstampedRep("test_viewstamped_rep_ops", capacity=5)
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
