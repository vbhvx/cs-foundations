"""Unit test suite for JIT Trampoline Dispatcher (compilers)."""
from compilers.jit_trampoline import JitTrampoline

def test_jit_trampoline_lifecycle():
    obj = JitTrampoline("test_jit_trampoline", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_jit_trampoline"
    assert status["capacity"] == 10

def test_jit_trampoline_operations():
    obj = JitTrampoline("test_jit_trampoline_ops", capacity=5)
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
