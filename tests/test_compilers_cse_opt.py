"""Unit test suite for Common Subexpression Elimination (compilers)."""
from compilers.cse_opt import CseOpt

def test_cse_opt_lifecycle():
    obj = CseOpt("test_cse_opt", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_cse_opt"
    assert status["capacity"] == 10

def test_cse_opt_operations():
    obj = CseOpt("test_cse_opt_ops", capacity=5)
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
