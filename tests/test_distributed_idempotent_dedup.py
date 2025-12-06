"""Unit test suite for Idempotent Message Deduplication Cache (distributed)."""
from distributed.idempotent_dedup import IdempotentDedup

def test_idempotent_dedup_lifecycle():
    obj = IdempotentDedup("test_idempotent_dedup", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_idempotent_dedup"
    assert status["capacity"] == 10

def test_idempotent_dedup_operations():
    obj = IdempotentDedup("test_idempotent_dedup_ops", capacity=5)
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
