from os_internals.page_clock import simulate_clock_page_replacement

def test_clock_page_faults():
    pages = [1, 2, 3, 1, 4, 5]
    faults = simulate_clock_page_replacement(pages, 3)
    assert faults >= 3
