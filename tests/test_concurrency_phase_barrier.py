"""Unit test suite for Async Barrier Phase Synchronizer (concurrency)."""
from concurrency.phase_barrier import PhaseBarrier

def test_phase_barrier_lifecycle():
    obj = PhaseBarrier("test_phase_barrier", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_phase_barrier"
    assert status["capacity"] == 10

def test_phase_barrier_operations():
    obj = PhaseBarrier("test_phase_barrier_ops", capacity=5)
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
