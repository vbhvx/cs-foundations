"""Unit test suite for Banker's Deadlock Avoidance Algorithm (os_internals)."""
from os_internals.bankers_algorithm import BankersAlgorithm

def test_bankers_algorithm_lifecycle():
    obj = BankersAlgorithm("test_bankers_algorithm", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bankers_algorithm"
    assert status["capacity"] == 10

def test_bankers_algorithm_operations():
    obj = BankersAlgorithm("test_bankers_algorithm_ops", capacity=5)
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
