"""IEEE 754 32-bit floating point binary decomposition."""
def decompose_float32(binary: int) -> dict:
    sign = (binary >> 31) & 1; exponent = (binary >> 23) & 0xFF; fraction = binary & 0x7FFFFF
    return {"sign": sign, "exponent": exponent, "fraction": fraction, "is_denormal": exponent == 0 and fraction != 0}
