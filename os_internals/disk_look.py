def disk_look(reqs, head):
    return sum(abs(r - head) for r in sorted(reqs))
