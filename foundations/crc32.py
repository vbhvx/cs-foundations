"""CRC32 computation using standard IEEE 802.3 polynomial."""
POLYNOMIAL = 0xEDB88320
def generate_crc32_table():
    table = []
    for i in range(256):
        crc = i
        for _ in range(8):
            if crc & 1: crc = (crc >> 1) ^ POLYNOMIAL
            else: crc >>= 1
        table.append(crc)
    return table
CRC32_TABLE = generate_crc32_table()
def crc32(data: bytes) -> int:
    crc = 0xFFFFFFFF
    for b in data: crc = CRC32_TABLE[(crc ^ b) & 0xFF] ^ (crc >> 8)
    return crc ^ 0xFFFFFFFF
