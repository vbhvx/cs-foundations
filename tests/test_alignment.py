from foundations.alignment import calculate_struct_layout
def test_struct_layout():
    size, layout = calculate_struct_layout([("c1", 1, 1), ("i1", 4, 4), ("c2", 1, 1)])
    assert size == 12 and layout == [("c1", 0), ("i1", 4), ("c2", 8)]
