from foundations.lfsr import LFSR16

def test_lfsr():
    lfsr = LFSR16(0x1234)
    bits = [lfsr.next_bit() for _ in range(16)]
    assert len(bits) == 16
