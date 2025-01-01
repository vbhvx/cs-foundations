from foundations.adler32 import adler32
import zlib

def test_adler32():
    data = b"Wikipedia Adler32 Test Vector"
    assert adler32(data) == zlib.adler32(data)
