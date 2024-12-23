from os_internals.bankers import is_safe_state

def test_bankers():
    avail = [3, 3, 2]
    max_need = [[7, 5, 3], [3, 2, 2]]
    alloc = [[0, 1, 0], [2, 0, 0]]
    assert not is_safe_state(avail, max_need, alloc)
    assert is_safe_state([10, 10, 10], max_need, alloc)
