"""MurmurHash3 32-bit variant."""
def murmur3_32(data: bytes, seed: int = 0) -> int:
    c1 = 0xcc9e2d51; c2 = 0x1b873593; h = seed
    n_blocks = len(data) // 4
    for i in range(n_blocks):
        k = int.from_bytes(data[i*4:(i+1)*4], "little")
        k = (k * c1) & 0xFFFFFFFF; k = ((k << 15) | (k >> 17)) & 0xFFFFFFFF; k = (k * c2) & 0xFFFFFFFF
        h ^= k; h = ((h << 13) | (h >> 19)) & 0xFFFFFFFF; h = (h * 5 + 0xe6546b64) & 0xFFFFFFFF
    tail = data[n_blocks*4:]; k = 0
    for j, b in enumerate(tail): k ^= b << (j * 8)
    if k:
        k = (k * c1) & 0xFFFFFFFF; k = ((k << 15) | (k >> 17)) & 0xFFFFFFFF; k = (k * c2) & 0xFFFFFFFF; h ^= k
    h ^= len(data); h ^= (h >> 16); h = (h * 0x85ebca6b) & 0xFFFFFFFF; h ^= (h >> 13); h = (h * 0xc2b2ae35) & 0xFFFFFFFF; h ^= (h >> 16)
    return h
