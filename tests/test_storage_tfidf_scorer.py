"""Unit test suite for Tf-Idf Vector Space Term Scorer (storage)."""
from storage.tfidf_scorer import TfidfScorer

def test_tfidf_scorer_lifecycle():
    obj = TfidfScorer("test_tfidf_scorer", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_tfidf_scorer"
    assert status["capacity"] == 10

def test_tfidf_scorer_operations():
    obj = TfidfScorer("test_tfidf_scorer_ops", capacity=5)
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
