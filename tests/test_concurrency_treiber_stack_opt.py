"""Unit test suite for Treiber Lock-Free Stack (concurrency)."""
from concurrency.treiber_stack_opt import TreiberStackOpt

def test_treiber_stack_opt_lifecycle():
    obj = TreiberStackOpt("test_treiber_stack_opt", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_treiber_stack_opt"
    assert status["capacity"] == 10

def test_treiber_stack_opt_operations():
    obj = TreiberStackOpt("test_treiber_stack_opt_ops", capacity=5)
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
