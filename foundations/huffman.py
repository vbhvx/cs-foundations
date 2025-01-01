"""Huffman compression tree builder and prefix encoder."""
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other): return self.freq < other.freq

def build_huffman_tree(text: str):
    if not text: return None, {}
    counts = Counter(text)
    heap = [HuffmanNode(ch, fr) for ch, fr in counts.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        parent = HuffmanNode(None, n1.freq + n2.freq)
        parent.left = n1
        parent.right = n2
        heapq.heappush(heap, parent)
    root = heap[0]
    codes = {}
    def gen_codes(node, code):
        if not node: return
        if node.char is not None:
            codes[node.char] = code or "0"
            return
        gen_codes(node.left, code + "0")
        gen_codes(node.right, code + "1")
    gen_codes(root, "")
    return root, codes
