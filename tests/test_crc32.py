from foundations.crc32 import crc32
import binascii
def test_crc32_matches_standard():
    assert crc32(b"123456789") == binascii.crc32(b"123456789")
