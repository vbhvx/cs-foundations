"""Unit test suite for Vectorization SIMD Lowering (compilers)."""
from compilers.simd_lowering import SimdLowering

def test_simd_lowering_lifecycle():
    obj = SimdLowering("test_simd_lowering", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_simd_lowering"
    assert status["capacity"] == 10

def test_simd_lowering_operations():
    obj = SimdLowering("test_simd_lowering_ops", capacity=5)
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
