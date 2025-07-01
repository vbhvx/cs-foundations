"""Unit test suite for ARP Table & Cache Expiration (networking)."""
from networking.arp_cache import ArpCache

def test_arp_cache_lifecycle():
    obj = ArpCache("test_arp_cache", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_arp_cache"
    assert status["capacity"] == 10

def test_arp_cache_operations():
    obj = ArpCache("test_arp_cache_ops", capacity=5)
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
