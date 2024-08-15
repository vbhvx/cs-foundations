from foundations.float_ieee import decompose_float32
def test_float_decomposition():
    dec = decompose_float32(0x3F800000)
    assert dec["sign"] == 0 and dec["exponent"] == 127 and dec["fraction"] == 0
