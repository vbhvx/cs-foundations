"""SSTable reader performing point lookup using sparse index."""
import struct

class SSTableReader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self._load_index()

    def _load_index(self):
        with open(self.filepath, "rb") as f:
            f.seek(-12, 2)
            index_offset, magic = struct.unpack(">QI", f.read(12))
            if magic != 0x53535442: raise ValueError("Invalid SSTable magic")
            f.seek(index_offset)
            idx_data = f.read(f.seek(0, 2) - 12 - index_offset)
        self.index = []
        pos = 0
        while pos < len(idx_data):
            k_len, off = struct.unpack_from(">II", idx_data, pos)
            pos += 8
            k = idx_data[pos:pos+k_len].decode("utf-8")
            pos += k_len
            self.index.append((k, off))

    def get(self, key: str):
        with open(self.filepath, "rb") as f:
            f.seek(-12, 2)
            index_offset, _ = struct.unpack(">QI", f.read(12))
            f.seek(0)
            data = f.read(index_offset)
        pos = 0
        while pos < len(data):
            k_len, v_len = struct.unpack_from(">II", data, pos)
            pos += 8
            k = data[pos:pos+k_len].decode("utf-8")
            pos += k_len
            v = data[pos:pos+v_len].decode("utf-8")
            pos += v_len
            if k == key:
                return v
        return None
