"""Unit test suite for Quiescent-State-Based Reclamation (QSBR) (concurrency)."""
from concurrency.qsbr_reclaim import QsbrReclaim

def test_qsbr_reclaim_lifecycle():
    obj = QsbrReclaim("test_qsbr_reclaim", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_qsbr_reclaim"
    assert status["capacity"] == 10

def test_qsbr_reclaim_operations():
    obj = QsbrReclaim("test_qsbr_reclaim_ops", capacity=5)
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
