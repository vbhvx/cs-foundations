"""Unit test suite for Range Analysis & Bounds Elimination (compilers)."""
from compilers.bounds_elim import BoundsElim

def test_bounds_elim_lifecycle():
    obj = BoundsElim("test_bounds_elim", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bounds_elim"
    assert status["capacity"] == 10

def test_bounds_elim_operations():
    obj = BoundsElim("test_bounds_elim_ops", capacity=5)
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
