from concurrency.token_ring import TokenRingNode

def test_token_ring():
    ring = [TokenRingNode(i, 3) for i in range(3)]
    assert ring[0].has_token
    ring[0].pass_token(ring)
    assert not ring[0].has_token
    assert ring[1].has_token
