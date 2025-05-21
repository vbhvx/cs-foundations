"""Unit test suite for Shenandoah Brooks Pointers Relocation (memory)."""
from memory.shenandoah_gc import ShenandoahGc

def test_shenandoah_gc_lifecycle():
    obj = ShenandoahGc("test_shenandoah_gc", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_shenandoah_gc"
    assert status["capacity"] == 10

def test_shenandoah_gc_operations():
    obj = ShenandoahGc("test_shenandoah_gc_ops", capacity=5)
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
