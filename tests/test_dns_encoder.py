from networking.dns_encoder import encode_dns_query

def test_dns_query():
    q = encode_dns_query("example.com", tx_id=0x1234)
    assert len(q) > 12
    assert b"\x07example\x03com\x00" in q
