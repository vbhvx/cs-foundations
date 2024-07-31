from foundations.byte_buffer import ByteBuffer
from foundations.byte_buffer_ext import write_uint64, read_uint64
def test_uint64_encoding():
    buf = ByteBuffer(); write_uint64(buf, 10000000000, ">")
    assert read_uint64(buf, ">") == 10000000000
