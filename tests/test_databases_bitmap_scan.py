"""Unit test suite for Bitmap Index Scan Operator (databases)."""
from databases.bitmap_scan import BitmapScan

def test_bitmap_scan_lifecycle():
    obj = BitmapScan("test_bitmap_scan", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bitmap_scan"
    assert status["capacity"] == 10

def test_bitmap_scan_operations():
    obj = BitmapScan("test_bitmap_scan_ops", capacity=5)
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
