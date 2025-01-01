"""Package release artifacts and checksum manifests."""
import hashlib, os

def generate_manifest(root_dir: str):
    manifest = {}
    for r, _, files in os.walk(root_dir):
        for f in files:
            if f.endswith(".py"):
                p = os.path.join(r, f)
                h = hashlib.sha256(open(p, "rb").read()).hexdigest()
                manifest[os.path.relpath(p, root_dir)] = h
    return manifest
