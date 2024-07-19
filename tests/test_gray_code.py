from foundations.gray_code import binary_to_gray, gray_to_binary
def test_gray_code():
    for i in range(16): assert gray_to_binary(binary_to_gray(i)) == i
