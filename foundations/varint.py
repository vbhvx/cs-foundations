"""Variable-length integer encoding (LEB128/Varint)."""
def encode_varint(val: int) -> bytes:
    buf = bytearray()
    while True:
        byte = val & 0x7F; val >>= 7
        if val: buf.append(byte | 0x80)
        else: buf.append(byte); break
    return bytes(buf)
def decode_varint(data: bytes) -> tuple:
    res = 0; shift = 0; read = 0
    for b in data:
        read += 1; res |= (b & 0x7F) << shift
        if not (b & 0x80): break
        shift += 7
    return res, read
