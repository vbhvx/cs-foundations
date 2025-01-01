"""RFC 6455 WebSocket frame header parser."""

def parse_ws_frame_header(data: bytes) -> dict:
    if len(data) < 2: raise ValueError("Header too short")
    b0, b1 = data[0], data[1]
    fin = (b0 >> 7) & 1
    opcode = b0 & 0x0F
    masked = (b1 >> 7) & 1
    length = b1 & 0x7F
    return {"fin": fin, "opcode": opcode, "masked": masked, "length": length}
