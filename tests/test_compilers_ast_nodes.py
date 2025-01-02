"""Unit test suite for AST Node Hierarchy (compilers)."""
from compilers.ast_nodes import AstNodes

def test_ast_nodes_lifecycle():
    obj = AstNodes("test_ast_nodes", capacity=10)
    assert obj.is_active is True
    assert obj.size() == 0
    status = obj.get_status()
    assert status["identifier"] == "test_ast_nodes"
    assert status["capacity"] == 10

def test_ast_nodes_operations():
    obj = AstNodes("test_ast_nodes_ops", capacity=5)
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
