"""Endian byte-swapping utility functions."""

def swap16(n: int) -> int:
    return ((n << 8) & 0xFF00) | ((n >> 8) & 0x00FF)

def swap32(n: int) -> int:
    return (((n << 24) & 0xFF000000) |
            ((n << 8)  & 0x00FF0000) |
            ((n >> 8)  & 0x0000FF00) |
            ((n >> 24) & 0x000000FF))
