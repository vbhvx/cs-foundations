from storage.sstable_writer import SSTableWriter
from storage.sstable_reader import SSTableReader
import tempfile, os

def test_sstable():
    items = [("a", "1"), ("b", "2"), ("c", "3")]
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        SSTableWriter.write(tmp.name, items)
        r = SSTableReader(tmp.name)
        assert r.get("a") == "1"
        assert r.get("b") == "2"
        assert r.get("z") is None
    os.unlink(tmp.name)
