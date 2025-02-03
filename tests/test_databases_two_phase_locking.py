"""Unit test suite for Two-Phase Locking (2PL) Concurrency (databases)."""
from databases.two_phase_locking import TwoPhaseLocking

def test_two_phase_locking_lifecycle():
    obj = TwoPhaseLocking("test_two_phase_locking", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_two_phase_locking"
    assert status["capacity"] == 10

def test_two_phase_locking_operations():
    obj = TwoPhaseLocking("test_two_phase_locking_ops", capacity=5)
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
