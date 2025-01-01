from storage.wal_record import WALRecord, OP_PUT
from storage.wal_reader import deserialize_wal_record

def test_wal_record():
    rec = WALRecord(101, OP_PUT, "user:1", "Alice")
    b = rec.serialize()
    decoded, length = deserialize_wal_record(b)
    assert decoded.lsn == 101
    assert decoded.key == "user:1"
    assert decoded.value == "Alice"
    assert length == len(b)
