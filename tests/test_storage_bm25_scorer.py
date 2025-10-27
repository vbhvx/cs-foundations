"""Unit test suite for BM25 Relevance Scoring Function (storage)."""
from storage.bm25_scorer import Bm25Scorer

def test_bm25_scorer_lifecycle():
    obj = Bm25Scorer("test_bm25_scorer", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_bm25_scorer"
    assert status["capacity"] == 10

def test_bm25_scorer_operations():
    obj = Bm25Scorer("test_bm25_scorer_ops", capacity=5)
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
