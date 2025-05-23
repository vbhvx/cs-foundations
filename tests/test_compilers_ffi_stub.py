"""Unit test suite for Foreign Function Interface (FFI) Stub (compilers)."""
from compilers.ffi_stub import FfiStub

def test_ffi_stub_lifecycle():
    obj = FfiStub("test_ffi_stub", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ffi_stub"
    assert status["capacity"] == 10

def test_ffi_stub_operations():
    obj = FfiStub("test_ffi_stub_ops", capacity=5)
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
