from scripts.package_release import generate_manifest
import tempfile, os

def test_manifest():
    tmp = tempfile.mkdtemp()
    with open(os.path.join(tmp, "test.py"), "w") as f: f.write("x = 1\n")
    m = generate_manifest(tmp)
    assert "test.py" in m
