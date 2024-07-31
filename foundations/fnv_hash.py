"""Fowler-Noll-Vo hash functions (FNV-1a)."""
FNV_32_INIT = 0x811c9dc5; FNV_32_PRIME = 0x01000193
def fnv1a_32(data: bytes) -> int:
    h = FNV_32_INIT
    for b in data: h = ((h ^ b) * FNV_32_PRIME) & 0xFFFFFFFF
    return h
