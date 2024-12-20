from os_internals.path_resolver import SimpleFS

def test_path_resolution():
    fs = SimpleFS()
    usr = fs.mkdir(0, "usr")
    bin_dir = fs.mkdir(usr, "bin")
    assert fs.resolve("/usr/bin") == bin_dir
