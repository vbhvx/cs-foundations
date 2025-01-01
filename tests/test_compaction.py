from storage.compaction import merge_sstable_records

def test_compaction():
    newer = [("k1", "v1_new"), ("k2", "__DELETED__")]
    older = [("k1", "v1_old"), ("k2", "v2_old"), ("k3", "v3")]
    merged = merge_sstable_records(newer, older)
    assert merged == [("k1", "v1_new"), ("k3", "v3")]
