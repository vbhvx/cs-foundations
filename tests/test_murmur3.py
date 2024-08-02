from foundations.murmur3 import murmur3_32
def test_murmur3(): assert murmur3_32(b"", 0) == 0 and isinstance(murmur3_32(b"test", 42), int)
