from os_internals.page_lru import simulate_lru_page_replacement

def test_lru_page_faults():
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    faults = simulate_lru_page_replacement(pages, 3)
    assert faults == 10
