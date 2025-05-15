"""Unit test suite for Generational Garbage Collector (memory)."""
from memory.generational_gc import GenerationalGc

def test_generational_gc_lifecycle():
    obj = GenerationalGc("test_generational_gc", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_generational_gc"
    assert status["capacity"] == 10

def test_generational_gc_operations():
    obj = GenerationalGc("test_generational_gc_ops", capacity=5)
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
