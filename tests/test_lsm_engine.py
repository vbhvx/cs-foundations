from storage.lsm_engine import LSMEngine
import tempfile, shutil

def test_lsm_engine():
    tmp = tempfile.mkdtemp()
    engine = LSMEngine(tmp, memtable_limit=50)
    engine.put("alpha", "1")
    engine.put("beta", "2")
    assert engine.get("alpha") == "1"
    assert engine.get("beta") == "2"
    shutil.rmtree(tmp)
