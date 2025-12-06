"""Unit test suite for Saga Compensating Action Rollback Engine (distributed)."""
from distributed.saga_rollback import SagaRollback

def test_saga_rollback_lifecycle():
    obj = SagaRollback("test_saga_rollback", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_saga_rollback"
    assert status["capacity"] == 10

def test_saga_rollback_operations():
    obj = SagaRollback("test_saga_rollback_ops", capacity=5)
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
