"""WAL record decoder verifying CRC32 integrity."""
import struct
from foundations.crc32 import crc32
from storage.wal_record import WALRecord

def deserialize_wal_record(data: bytes, offset: int = 0):
    if len(data) - offset < 14: return None, 0
    expected_crc = struct.unpack_from(">I", data, offset)[0]
    lsn, op_type, k_len = struct.unpack_from(">QBB", data, offset + 4)
    k_start = offset + 14
    key = data[k_start:k_start + k_len].decode("utf-8")
    v_len_offset = k_start + k_len
    v_len = struct.unpack_from(">I", data, v_len_offset)[0]
    v_start = v_len_offset + 4
    val = data[v_start:v_start + v_len].decode("utf-8")
    total_len = (v_start + v_len) - offset
    payload = data[offset + 4:offset + total_len]
    if crc32(payload) != expected_crc:
        raise ValueError("WAL Record CRC32 mismatch")
    return WALRecord(lsn, op_type, key, val), total_len
