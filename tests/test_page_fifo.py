from os_internals.page_fifo import simulate_fifo_page_replacement

def test_fifo_page_faults():
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    faults = simulate_fifo_page_replacement(pages, 3)
    assert faults > 0
