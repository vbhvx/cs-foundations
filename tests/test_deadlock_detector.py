from concurrency.deadlock_detector import WaitForGraph

def test_deadlock_detection():
    g = WaitForGraph()
    g.add_dependency("T1", "T2")
    g.add_dependency("T2", "T3")
    assert len(g.detect_deadlock()) == 0
    g.add_dependency("T3", "T1")  # Cycle: T1 -> T2 -> T3 -> T1
    cycle = g.detect_deadlock()
    assert len(cycle) > 0
