"""Unit test suite for Constant Folding Optimizer (compilers)."""
from compilers.constant_folder import ConstantFolder

def test_constant_folder_lifecycle():
    obj = ConstantFolder("test_constant_folder", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_constant_folder"
    assert status["capacity"] == 10

def test_constant_folder_operations():
    obj = ConstantFolder("test_constant_folder_ops", capacity=5)
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
