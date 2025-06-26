"""Unit test suite for DNS Recursive Resolver Core (networking)."""
from networking.dns_resolver import DnsResolver

def test_dns_resolver_lifecycle():
    obj = DnsResolver("test_dns_resolver", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_dns_resolver"
    assert status["capacity"] == 10

def test_dns_resolver_operations():
    obj = DnsResolver("test_dns_resolver_ops", capacity=5)
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
