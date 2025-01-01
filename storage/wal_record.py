"""WAL record format with LSN, operation type, key, value, and CRC32."""
import struct
from foundations.crc32 import crc32

OP_PUT = 1
OP_DELETE = 2

class WALRecord:
    def __init__(self, lsn: int, op_type: int, key: str, value: str = ""):
        self.lsn = lsn
        self.op_type = op_type
        self.key = key
        self.value = value

    def serialize(self) -> bytes:
        k_bytes = self.key.encode("utf-8")
        v_bytes = self.value.encode("utf-8")
        payload = struct.pack(">QBB", self.lsn, self.op_type, len(k_bytes)) + k_bytes + struct.pack(">I", len(v_bytes)) + v_bytes
        checksum = crc32(payload)
        return struct.pack(">I", checksum) + payload
