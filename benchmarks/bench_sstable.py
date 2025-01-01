"""Sparse index binary lookup latency benchmark."""
from storage.sstable_writer import SSTableWriter
from storage.sstable_reader import SSTableReader
import tempfile, os

def bench_sstable_lookup():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        items = [(f"key_{i:04d}", f"val_{i}") for i in range(100)]
        SSTableWriter.write(tmp.name, items)
        r = SSTableReader(tmp.name)
        val = r.get("key_0050")
    os.unlink(tmp.name)
    return val == "val_50"
