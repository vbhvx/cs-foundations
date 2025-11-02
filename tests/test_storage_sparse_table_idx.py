"""Unit test suite for Sparse Table Range Query Index (storage)."""
from storage.sparse_table_idx import SparseTableIdx

def test_sparse_table_idx_lifecycle():
    obj = SparseTableIdx("test_sparse_table_idx", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_sparse_table_idx"
    assert status["capacity"] == 10

def test_sparse_table_idx_operations():
    obj = SparseTableIdx("test_sparse_table_idx_ops", capacity=5)
    ok, res = obj.execute("k1", 100)
    assert ok is True
    assert res == 100
    assert obj.query("k1") == 100
    assert obj.size() == 1
    
    # Overwrite
    ok, res = obj.execute("k1", 200)
    assert ok is True
    assert obj.query("k1") == 200
    assert obj.size() == 1
    
    # Reset
    obj.reset()
    assert obj.size() == 0
