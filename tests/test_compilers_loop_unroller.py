"""Unit test suite for Loop Unrolling Optimizer (compilers)."""
from compilers.loop_unroller import LoopUnroller

def test_loop_unroller_lifecycle():
    obj = LoopUnroller("test_loop_unroller", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_loop_unroller"
    assert status["capacity"] == 10

def test_loop_unroller_operations():
    obj = LoopUnroller("test_loop_unroller_ops", capacity=5)
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
