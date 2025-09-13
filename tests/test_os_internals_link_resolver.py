"""Unit test suite for Hardlink & Symlink Resolution Resolver (os_internals)."""
from os_internals.link_resolver import LinkResolver

def test_link_resolver_lifecycle():
    obj = LinkResolver("test_link_resolver", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_link_resolver"
    assert status["capacity"] == 10

def test_link_resolver_operations():
    obj = LinkResolver("test_link_resolver_ops", capacity=5)
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
