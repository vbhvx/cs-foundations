"""Insertion latency benchmark for SkipList."""
from storage.skiplist import SkipList
from benchmarks.harness import time_execution

def bench_skiplist_insert():
    sl = SkipList()
    return time_execution(lambda: sl.insert("test_key", "test_val"), 100)
