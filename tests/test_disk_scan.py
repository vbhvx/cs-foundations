from os_internals.disk_scan import disk_scan

def test_disk_scan():
    reqs = [98, 183, 37, 122, 14, 124, 65, 67]
    seek = disk_scan(reqs, 53, 200)
    assert seek > 0
