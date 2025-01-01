from os_internals.disk_look import disk_look
def test_look(): assert disk_look([10, 20], 5) > 0
