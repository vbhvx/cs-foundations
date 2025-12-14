"""Unit test suite for Distributed Semaphore Lease Expiration (distributed)."""
from distributed.distributed_semaphore import DistributedSemaphore

def test_distributed_semaphore_lifecycle():
    obj = DistributedSemaphore("test_distributed_semaphore", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_distributed_semaphore"
    assert status["capacity"] == 10

def test_distributed_semaphore_operations():
    obj = DistributedSemaphore("test_distributed_semaphore_ops", capacity=5)
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
