from os_internals.page_optimal import simulate_optimal_page_replacement

def test_optimal_page_faults():
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    faults = simulate_optimal_page_replacement(pages, 3)
    assert faults <= 9
