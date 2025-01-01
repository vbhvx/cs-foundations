"""Adler-32 checksum algorithm (RFC 1950)."""

MOD_ADLER = 65521

def adler32(data: bytes) -> int:
    a = 1
    b = 0
    for byte in data:
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a
