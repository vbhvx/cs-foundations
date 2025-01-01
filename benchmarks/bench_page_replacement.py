"""Page replacement algorithm comparison under random access patterns."""
from os_internals.page_fifo import simulate_fifo_page_replacement
from os_internals.page_lru import simulate_lru_page_replacement

def compare_page_algorithms():
    trace = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    fifo_faults = simulate_fifo_page_replacement(trace, 3)
    lru_faults = simulate_lru_page_replacement(trace, 3)
    return {"fifo": fifo_faults, "lru": lru_faults}
