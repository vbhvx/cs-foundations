from os_internals.disk_scheduler import disk_fcfs, disk_sstf

def test_disk_scheduler():
    reqs = [98, 183, 37, 122, 14, 124, 65, 67]
    assert disk_fcfs(reqs, 53) == 640
    assert disk_sstf(reqs, 53) == 236
