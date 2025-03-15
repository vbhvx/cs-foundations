"""Unit test suite for Strength Reduction Transformation (compilers)."""
from compilers.strength_reduce import StrengthReduce

def test_strength_reduce_lifecycle():
    obj = StrengthReduce("test_strength_reduce", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_strength_reduce"
    assert status["capacity"] == 10

def test_strength_reduce_operations():
    obj = StrengthReduce("test_strength_reduce_ops", capacity=5)
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
