"""Unit test suite for Vector Time Causality Matrix (consensus)."""
from consensus.vector_time_matrix import VectorTimeMatrix

def test_vector_time_matrix_lifecycle():
    obj = VectorTimeMatrix("test_vector_time_matrix", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_vector_time_matrix"
    assert status["capacity"] == 10

def test_vector_time_matrix_operations():
    obj = VectorTimeMatrix("test_vector_time_matrix_ops", capacity=5)
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
