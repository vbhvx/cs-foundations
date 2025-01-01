from storage.wal_file import WALFile
from storage.wal_record import WALRecord, OP_PUT
import tempfile, os

def test_wal_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        wf = WALFile(tmp.name)
        wf.append(WALRecord(1, OP_PUT, "k1", "v1"))
        recs = wf.read_all()
        assert len(recs) == 1
        assert recs[0].key == "k1"
    os.unlink(tmp.name)
