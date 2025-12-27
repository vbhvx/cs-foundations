"""Unit test suite for Page Checksum & CRC Verification (databases)."""
from databases.page_checksum import PageChecksum

def test_page_checksum_lifecycle():
    obj = PageChecksum("test_page_checksum", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_page_checksum"
    assert status["capacity"] == 10

def test_page_checksum_operations():
    obj = PageChecksum("test_page_checksum_ops", capacity=5)
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
