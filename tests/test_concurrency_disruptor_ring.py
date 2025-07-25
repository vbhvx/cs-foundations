"""Unit test suite for LMAX Disruptor Ring Buffer (concurrency)."""
from concurrency.disruptor_ring import DisruptorRing

def test_disruptor_ring_lifecycle():
    obj = DisruptorRing("test_disruptor_ring", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_disruptor_ring"
    assert status["capacity"] == 10

def test_disruptor_ring_operations():
    obj = DisruptorRing("test_disruptor_ring_ops", capacity=5)
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
