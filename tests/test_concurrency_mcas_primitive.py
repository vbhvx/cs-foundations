"""Unit test suite for Wait-Free Multi-Word CAS (MCAS) (concurrency)."""
from concurrency.mcas_primitive import McasPrimitive

def test_mcas_primitive_lifecycle():
    obj = McasPrimitive("test_mcas_primitive", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_mcas_primitive"
    assert status["capacity"] == 10

def test_mcas_primitive_operations():
    obj = McasPrimitive("test_mcas_primitive_ops", capacity=5)
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
