"""Unit test suite for Distributed Lock Manager (Redlock Algorithm) (distributed)."""
from distributed.redlock_algorithm import RedlockAlgorithm

def test_redlock_algorithm_lifecycle():
    obj = RedlockAlgorithm("test_redlock_algorithm", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_redlock_algorithm"
    assert status["capacity"] == 10

def test_redlock_algorithm_operations():
    obj = RedlockAlgorithm("test_redlock_algorithm_ops", capacity=5)
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
