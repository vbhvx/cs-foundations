"""Streaming accumulator extracting framed packets from TCP streams."""
from networking.frame import decode_frame

class FrameStreamDecoder:
    def __init__(self):
        self._buf = bytearray()

    def feed(self, chunk: bytes):
        self._buf.extend(chunk)

    def pop_frame(self):
        if len(self._buf) < 11: return None
        import struct
        magic, _, length = struct.unpack_from(">HBI", self._buf, 0)
        if len(self._buf) < 11 + length: return None
        frame_bytes = bytes(self._buf[:11 + length])
        self._buf = self._buf[11 + length:]
        return decode_frame(frame_bytes)
