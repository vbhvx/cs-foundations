from foundations.endian import swap16, swap32

def test_endian():
    assert swap16(0x1234) == 0x3412
    assert swap32(0x12345678) == 0x78563412
