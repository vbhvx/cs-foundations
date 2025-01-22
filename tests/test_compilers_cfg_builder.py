"""Unit test suite for Control Flow Graph (CFG) (compilers)."""
from compilers.cfg_builder import CfgBuilder

def test_cfg_builder_lifecycle():
    obj = CfgBuilder("test_cfg_builder", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_cfg_builder"
    assert status["capacity"] == 10

def test_cfg_builder_operations():
    obj = CfgBuilder("test_cfg_builder_ops", capacity=5)
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
