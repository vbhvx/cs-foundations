"""Unit test suite for Circuit Breaker Failure State Machine (distributed)."""
from distributed.circuit_breaker import CircuitBreaker

def test_circuit_breaker_lifecycle():
    obj = CircuitBreaker("test_circuit_breaker", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_circuit_breaker"
    assert status["capacity"] == 10

def test_circuit_breaker_operations():
    obj = CircuitBreaker("test_circuit_breaker_ops", capacity=5)
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
