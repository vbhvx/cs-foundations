from os_internals.alloc_best_fit import BestFit
def test_bf(): bf = BestFit([10, 50, 20]); assert bf.alloc(15) == 2
