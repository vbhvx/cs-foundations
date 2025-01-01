"""Two-way merge iterator deduplicating keys across SSTables."""

def merge_sstable_records(iter_a, iter_b):
    # iter_a (newer), iter_b (older)
    res = {}
    for k, v in iter_b:
        res[k] = v
    for k, v in iter_a:
        res[k] = v
    # filter tombstones
    return sorted([(k, v) for k, v in res.items() if v != "__DELETED__"])
