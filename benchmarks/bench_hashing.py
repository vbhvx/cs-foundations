"""Benchmark comparing CRC32, FNV-1a, and Murmur3."""
from benchmarks.harness import time_execution
from foundations.crc32 import crc32
from foundations.fnv_hash import fnv1a_32
from foundations.murmur3 import murmur3_32

def run_hash_benchmarks():
    data = b"systems_benchmarking_payload_2024"
    t_crc = time_execution(lambda: crc32(data), 1000)
    t_fnv = time_execution(lambda: fnv1a_32(data), 1000)
    t_mur = time_execution(lambda: murmur3_32(data), 1000)
    return {"crc32": t_crc, "fnv1a": t_fnv, "murmur3": t_mur}
