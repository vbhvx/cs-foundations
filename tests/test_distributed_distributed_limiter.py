"""Unit test suite for Rate Limiting Token Bucket with Redis Semantics (distributed)."""
from distributed.distributed_limiter import DistributedLimiter

def test_distributed_limiter_lifecycle():
    obj = DistributedLimiter("test_distributed_limiter", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_distributed_limiter"
    assert status["capacity"] == 10

def test_distributed_limiter_operations():
    obj = DistributedLimiter("test_distributed_limiter_ops", capacity=5)
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
