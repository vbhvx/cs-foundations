def schedule_priority(processes):
    return sorted(processes, key=lambda p: p.priority, reverse=True)
