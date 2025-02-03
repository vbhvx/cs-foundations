"""Unit test suite for Bytecode Virtual Machine (compilers)."""
from compilers.bytecode_vm import BytecodeVm

def test_bytecode_vm_lifecycle():
    obj = BytecodeVm("test_bytecode_vm", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bytecode_vm"
    assert status["capacity"] == 10

def test_bytecode_vm_operations():
    obj = BytecodeVm("test_bytecode_vm_ops", capacity=5)
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
