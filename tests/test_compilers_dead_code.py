"""Unit test suite for Dead Code Eliminator (compilers)."""
from compilers.dead_code import DeadCode

def test_dead_code_lifecycle():
    obj = DeadCode("test_dead_code", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_dead_code"
    assert status["capacity"] == 10

def test_dead_code_operations():
    obj = DeadCode("test_dead_code_ops", capacity=5)
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
