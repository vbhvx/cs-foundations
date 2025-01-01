from networking.leaky_bucket import LeakyBucket

def test_leaky_bucket():
    lb = LeakyBucket(capacity=3, leak_rate=2.0)
    assert lb.add_drop(1.0)
    assert lb.add_drop(2.0)
    assert not lb.add_drop(1.0)
