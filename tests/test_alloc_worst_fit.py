from os_internals.alloc_worst_fit import WorstFit
def test_wf(): wf = WorstFit([10, 50]); assert wf.alloc(5) == 1
