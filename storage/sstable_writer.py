"""SSTable writer producing data blocks and sparse index."""
import struct

class SSTableWriter:
    @staticmethod
    def write(filepath: str, items: list, index_interval: int = 4):
        index = []
        with open(filepath, "wb") as f:
            data_offset = 0
            for i, (k, v) in enumerate(items):
                if i % index_interval == 0:
                    index.append((k, data_offset))
                k_bytes = k.encode("utf-8")
                v_bytes = v.encode("utf-8")
                entry = struct.pack(">II", len(k_bytes), len(v_bytes)) + k_bytes + v_bytes
                f.write(entry)
                data_offset += len(entry)
            # Write index section
            index_offset = data_offset
            for k, off in index:
                k_bytes = k.encode("utf-8")
                f.write(struct.pack(">II", len(k_bytes), off) + k_bytes)
            # Footer: index offset + magic
            f.write(struct.pack(">QI", index_offset, 0x53535442)) # 'SSTB'
