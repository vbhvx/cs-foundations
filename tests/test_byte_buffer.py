from foundations.byte_buffer import ByteBuffer
def test_byte_buffer_uint32():
    buf = ByteBuffer(); buf.write_uint32(0x12345678, ">")
    assert buf.read_uint32(">") == 0x12345678
