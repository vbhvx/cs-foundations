"""Bitwise rotation primitives for 32-bit words."""
def rotl32(n: int, shift: int) -> int:
    shift &= 31; return ((n << shift) | (n >> (32 - shift))) & 0xFFFFFFFF
def rotr32(n: int, shift: int) -> int:
    shift &= 31; return ((n >> shift) | (n << (32 - shift))) & 0xFFFFFFFF
