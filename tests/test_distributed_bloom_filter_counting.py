"""Unit test suite for Standard & Counting Bloom Filters (distributed)."""
from distributed.bloom_filter_counting import BloomFilterCounting

def test_bloom_filter_counting_lifecycle():
    obj = BloomFilterCounting("test_bloom_filter_counting", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bloom_filter_counting"
    assert status["capacity"] == 10

def test_bloom_filter_counting_operations():
    obj = BloomFilterCounting("test_bloom_filter_counting_ops", capacity=5)
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
