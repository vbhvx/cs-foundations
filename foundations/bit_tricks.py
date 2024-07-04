"""Common bitwise manipulation routines."""
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
def lowest_set_bit(n: int) -> int:
    return n & (-n)
def clear_lowest_set_bit(n: int) -> int:
    return n & (n - 1)
