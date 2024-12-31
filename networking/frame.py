"""Binary frame format: [MAGIC(2) | TYPE(1) | LEN(4) | PAYLOAD | CRC(4)]."""
import struct
from foundations.crc32 import crc32

MAGIC = 0xAA55

def encode_frame(msg_type: int, payload: bytes) -> bytes:
    header = struct.pack(">HBI", MAGIC, msg_type, len(payload))
    checksum = crc32(payload)
    trailer = struct.pack(">I", checksum)
    return header + payload + trailer

def decode_frame(data: bytes):
    if len(data) < 11: raise ValueError("Frame too short")
    magic, msg_type, length = struct.unpack_from(">HBI", data, 0)
    if magic != MAGIC: raise ValueError("Invalid magic number")
    if len(data) < 7 + length + 4: raise ValueError("Incomplete frame payload")
    payload = data[7:7+length]
    expected_crc = struct.unpack_from(">I", data, 7 + length)[0]
    if crc32(payload) != expected_crc: raise ValueError("CRC32 mismatch")
    return msg_type, payload
