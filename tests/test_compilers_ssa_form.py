"""Unit test suite for SSA (Static Single Assignment) Form (compilers)."""
from compilers.ssa_form import SsaForm

def test_ssa_form_lifecycle():
    obj = SsaForm("test_ssa_form", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ssa_form"
    assert status["capacity"] == 10

def test_ssa_form_operations():
    obj = SsaForm("test_ssa_form_ops", capacity=5)
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
