from networking.token_bucket import TokenBucket

def test_token_bucket():
    tb = TokenBucket(capacity=5, refill_rate=1.0)
    for _ in range(5):
        assert tb.allow_request()
    assert not tb.allow_request()
