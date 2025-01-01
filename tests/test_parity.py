from foundations.parity import parity
def test_parity(): assert parity(0b1011) == 1 and parity(0b1100) == 0
