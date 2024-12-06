from os_internals.page_table import TwoLevelPageTable
import pytest

def test_page_table():
    pt = TwoLevelPageTable()
    pt.map_page(0x1005, 0x4)
    assert pt.translate(0x1005) == 0x4005
    with pytest.raises(MemoryError):
        pt.translate(0x9999)
