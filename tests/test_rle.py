from foundations.rle import rle_encode, rle_decode

def test_rle():
    data = b"AAAAABBBCCDAAAAA"
    comp = rle_encode(data)
    assert len(comp) < len(data)
    assert rle_decode(comp) == data
