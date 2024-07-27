"""Binary byte buffer reader and writer with explicit endianness."""
import struct
class ByteBuffer:
    def __init__(self, data: bytes = b""):
        self._buffer = bytearray(data); self._pos = 0
    def write_uint32(self, val: int, endian: str = ">"):
        self._buffer.extend(struct.pack(f"{endian}I", val))
    def read_uint32(self, endian: str = ">") -> int:
        val = struct.unpack_from(f"{endian}I", self._buffer, self._pos)[0]
        self._pos += 4; return val
    def to_bytes(self) -> bytes: return bytes(self._buffer)
