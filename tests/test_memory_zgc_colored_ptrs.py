"""Unit test suite for ZGC Color Pointer Concurrent Marking (memory)."""
from memory.zgc_colored_ptrs import ZgcColoredPtrs

def test_zgc_colored_ptrs_lifecycle():
    obj = ZgcColoredPtrs("test_zgc_colored_ptrs", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_zgc_colored_ptrs"
    assert status["capacity"] == 10

def test_zgc_colored_ptrs_operations():
    obj = ZgcColoredPtrs("test_zgc_colored_ptrs_ops", capacity=5)
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
