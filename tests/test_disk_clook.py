from os_internals.disk_clook import disk_clook
def test_clook(): assert disk_clook([10, 30], 20) > 0
