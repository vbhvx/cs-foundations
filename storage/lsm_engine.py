"""Unified LSM-Tree store combining MemTable, WAL, and SSTables."""
from storage.memtable import MemTable
from storage.sstable_writer import SSTableWriter
from storage.sstable_reader import SSTableReader
import os

class LSMEngine:
    def __init__(self, data_dir: str, memtable_limit: int = 100):
        self.data_dir = data_dir
        self.memtable_limit = memtable_limit
        self.memtable = MemTable(max_bytes=memtable_limit)
        self.sstables = []
        self.file_counter = 0
        os.makedirs(data_dir, exist_ok=True)

    def put(self, key: str, value: str):
        self.memtable.put(key, value)
        if self.memtable.is_full():
            self.flush()

    def get(self, key: str):
        val = self.memtable.get(key)
        if val is not None: return val
        for sst in reversed(self.sstables):
            val = sst.get(key)
            if val is not None:
                return val if val != "__DELETED__" else None
        return None

    def flush(self):
        items = self.memtable.items()
        if not items: return
        sst_path = os.path.join(self.data_dir, f"sst_{self.file_counter:04d}.db")
        self.file_counter += 1
        SSTableWriter.write(sst_path, items)
        self.sstables.append(SSTableReader(sst_path))
        self.memtable = MemTable(max_bytes=self.memtable_limit)
