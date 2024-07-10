from foundations.bit_tricks import is_power_of_two, lowest_set_bit, clear_lowest_set_bit
def test_power_of_two():
    assert is_power_of_two(1) and is_power_of_two(16) and not is_power_of_two(18)
def test_lowest_set_bit():
    assert lowest_set_bit(12) == 4 and lowest_set_bit(18) == 2
