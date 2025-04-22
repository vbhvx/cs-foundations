"""Unit test suite for Three-Phase Commit (3PC) Protocol (consensus)."""
from consensus.three_phase_commit import ThreePhaseCommit

def test_three_phase_commit_lifecycle():
    obj = ThreePhaseCommit("test_three_phase_commit", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_three_phase_commit"
    assert status["capacity"] == 10

def test_three_phase_commit_operations():
    obj = ThreePhaseCommit("test_three_phase_commit_ops", capacity=5)
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
