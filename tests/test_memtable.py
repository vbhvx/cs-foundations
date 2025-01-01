from storage.memtable import MemTable

def test_memtable():
    mt = MemTable(max_bytes=1000)
    mt.put("k1", "v1")
    assert mt.get("k1") == "v1"
    mt.delete("k1")
    assert mt.get("k1") is None
