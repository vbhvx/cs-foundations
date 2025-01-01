from foundations.radix_tree import RadixTree

def test_radix_tree():
    rt = RadixTree()
    rt.insert("192.168.", "local_subnet")
    rt.insert("192.168.1.", "gateway_subnet")
    assert rt.longest_prefix_match("192.168.1.100") == "gateway_subnet"
    assert rt.longest_prefix_match("192.168.2.5") == "local_subnet"
