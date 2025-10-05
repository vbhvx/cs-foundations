"""Unit test suite for Projection Pushdown Planner (databases)."""
from databases.projection_pushdown import ProjectionPushdown

def test_projection_pushdown_lifecycle():
    obj = ProjectionPushdown("test_projection_pushdown", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_projection_pushdown"
    assert status["capacity"] == 10

def test_projection_pushdown_operations():
    obj = ProjectionPushdown("test_projection_pushdown_ops", capacity=5)
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
