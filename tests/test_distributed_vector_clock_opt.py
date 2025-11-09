"""Unit test suite for Vector Clock Causality Tracker (distributed)."""
from distributed.vector_clock_opt import VectorClockOpt

def test_vector_clock_opt_lifecycle():
    obj = VectorClockOpt("test_vector_clock_opt", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_vector_clock_opt"
    assert status["capacity"] == 10

def test_vector_clock_opt_operations():
    obj = VectorClockOpt("test_vector_clock_opt_ops", capacity=5)
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
