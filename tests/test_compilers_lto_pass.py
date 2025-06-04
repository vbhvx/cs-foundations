"""Unit test suite for Link-Time Optimizer (LTO) Pass (compilers)."""
from compilers.lto_pass import LtoPass

def test_lto_pass_lifecycle():
    obj = LtoPass("test_lto_pass", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_lto_pass"
    assert status["capacity"] == 10

def test_lto_pass_operations():
    obj = LtoPass("test_lto_pass_ops", capacity=5)
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
