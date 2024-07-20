"""Subsets generation using bit masks."""
def power_set(elements):
    n = len(elements)
    for mask in range(1 << n): yield [elements[i] for i in range(n) if (mask >> i) & 1]
