from foundations.bit_vector import BitVector

def test_bit_vector():
    bv = BitVector(100)
    bv.set(42)
    assert bv.get(42)
    assert not bv.get(41)
    bv.clear(42)
    assert not bv.get(42)
