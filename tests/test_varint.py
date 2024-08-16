from foundations.varint import encode_varint, decode_varint
def test_varint():
    assert encode_varint(300) == b"\xac\x02"
    assert decode_varint(b"\xac\x02")[0] == 300
