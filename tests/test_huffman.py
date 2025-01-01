from foundations.huffman import build_huffman_tree

def test_huffman():
    root, codes = build_huffman_tree("abbcccdddd")
    assert codes["d"] == "0" or len(codes["d"]) == 1
    assert len(codes) == 4
