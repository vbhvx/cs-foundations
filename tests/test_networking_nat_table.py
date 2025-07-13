"""Unit test suite for NAT Port Forwarding Translation Table (networking)."""
from networking.nat_table import NatTable

def test_nat_table_lifecycle():
    obj = NatTable("test_nat_table", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_nat_table"
    assert status["capacity"] == 10

def test_nat_table_operations():
    obj = NatTable("test_nat_table_ops", capacity=5)
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
