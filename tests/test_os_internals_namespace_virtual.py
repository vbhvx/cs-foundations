"""Unit test suite for Namespaces PID & Mount Virtualization (os_internals)."""
from os_internals.namespace_virtual import NamespaceVirtual

def test_namespace_virtual_lifecycle():
    obj = NamespaceVirtual("test_namespace_virtual", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_namespace_virtual"
    assert status["capacity"] == 10

def test_namespace_virtual_operations():
    obj = NamespaceVirtual("test_namespace_virtual_ops", capacity=5)
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
