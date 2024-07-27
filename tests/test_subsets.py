from foundations.subsets import power_set
def test_power_set():
    res = list(power_set(["a", "b"]))
    assert len(res) == 4 and [] in res and ["a", "b"] in res
