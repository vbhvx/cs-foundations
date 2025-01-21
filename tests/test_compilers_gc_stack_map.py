"""Unit test suite for Garbage Collection Stack Map (compilers)."""
from compilers.gc_stack_map import GcStackMap

def test_gc_stack_map_lifecycle():
    obj = GcStackMap("test_gc_stack_map", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_gc_stack_map"
    assert status["capacity"] == 10

def test_gc_stack_map_operations():
    obj = GcStackMap("test_gc_stack_map_ops", capacity=5)
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
