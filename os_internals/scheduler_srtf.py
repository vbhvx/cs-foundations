def schedule_srtf(processes):
    return sorted(processes, key=lambda p: p.remaining_time)
