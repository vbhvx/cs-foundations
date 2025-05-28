"""Unit test suite for Address Sanitizer Redzone Poisoning (memory)."""
from memory.asan_redzone import AsanRedzone

def test_asan_redzone_lifecycle():
    obj = AsanRedzone("test_asan_redzone", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_asan_redzone"
    assert status["capacity"] == 10

def test_asan_redzone_operations():
    obj = AsanRedzone("test_asan_redzone_ops", capacity=5)
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
