"""Unit test suite for Loop Invariant Code Motion (compilers)."""
from compilers.licm_opt import LicmOpt

def test_licm_opt_lifecycle():
    obj = LicmOpt("test_licm_opt", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_licm_opt"
    assert status["capacity"] == 10

def test_licm_opt_operations():
    obj = LicmOpt("test_licm_opt_ops", capacity=5)
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
