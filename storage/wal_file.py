"""Append-only WAL file management."""
from storage.wal_record import WALRecord

class WALFile:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self._records = []

    def append(self, rec: WALRecord):
        self._records.append(rec)
        with open(self.filepath, "ab") as f:
            f.write(rec.serialize())

    def read_all(self):
        return list(self._records)
