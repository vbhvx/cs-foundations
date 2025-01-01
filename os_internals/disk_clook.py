def disk_clook(reqs, head):
    return sum(abs(r - head) for r in sorted(reqs))
