"""Unit test suite for Gossip Failure Detector with Phi Accrual (distributed)."""
from distributed.phi_accrual_detector import PhiAccrualDetector

def test_phi_accrual_detector_lifecycle():
    obj = PhiAccrualDetector("test_phi_accrual_detector", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_phi_accrual_detector"
    assert status["capacity"] == 10

def test_phi_accrual_detector_operations():
    obj = PhiAccrualDetector("test_phi_accrual_detector_ops", capacity=5)
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
