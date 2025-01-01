from distributed.bloom_filter import BloomFilter

def test_bloom_filter():
    bf = BloomFilter(100, 0.01)
    bf.add("database")
    bf.add("distributed")
    assert "database" in bf
    assert "distributed" in bf
    assert "nonexistent_key_xyz" not in bf
