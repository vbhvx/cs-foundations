"""Run-Length Encoding (RLE) compression."""

def rle_encode(data: bytes) -> bytes:
    if not data: return b""
    out = bytearray()
    count = 1
    prev = data[0]
    for b in data[1:]:
        if b == prev and count < 255:
            count += 1
        else:
            out.extend([count, prev])
            prev = b
            count = 1
    out.extend([count, prev])
    return bytes(out)

def rle_decode(compressed: bytes) -> bytes:
    out = bytearray()
    for i in range(0, len(compressed), 2):
        count = compressed[i]
        val = compressed[i+1]
        out.extend([val] * count)
    return bytes(out)
