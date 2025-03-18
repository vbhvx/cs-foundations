"""Unit test suite for Induction Variable Analysis (compilers)."""
from compilers.induction_vars import InductionVars

def test_induction_vars_lifecycle():
    obj = InductionVars("test_induction_vars", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_induction_vars"
    assert status["capacity"] == 10

def test_induction_vars_operations():
    obj = InductionVars("test_induction_vars_ops", capacity=5)
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
