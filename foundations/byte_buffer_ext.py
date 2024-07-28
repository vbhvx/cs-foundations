"""Extended integer encodings for ByteBuffer."""
import struct
from foundations.byte_buffer import ByteBuffer
def write_uint64(buf: ByteBuffer, val: int, endian: str = ">"):
    buf._buffer.extend(struct.pack(f"{endian}Q", val))
def read_uint64(buf: ByteBuffer, endian: str = ">") -> int:
    val = struct.unpack_from(f"{endian}Q", buf._buffer, buf._pos)[0]
    buf._pos += 8; return val
