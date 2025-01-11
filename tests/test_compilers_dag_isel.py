"""Unit test suite for Instruction Selection DAG (compilers)."""
from compilers.dag_isel import DagIsel

def test_dag_isel_lifecycle():
    obj = DagIsel("test_dag_isel", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_dag_isel"
    assert status["capacity"] == 10

def test_dag_isel_operations():
    obj = DagIsel("test_dag_isel_ops", capacity=5)
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
