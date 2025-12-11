"""Unit test suite for Cardinality Estimator (HyperLogLog) (databases)."""
from databases.cardinality_est import CardinalityEst

def test_cardinality_est_lifecycle():
    obj = CardinalityEst("test_cardinality_est", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_cardinality_est"
    assert status["capacity"] == 10

def test_cardinality_est_operations():
    obj = CardinalityEst("test_cardinality_est_ops", capacity=5)
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
