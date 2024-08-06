from foundations.bit_rotations import rotl32, rotr32
def test_rotations():
    assert rotl32(0x80000001, 1) == 0x00000003 and rotr32(0x00000003, 1) == 0x80000001
