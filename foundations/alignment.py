"""Memory struct padding and alignment simulator."""
def calculate_struct_layout(fields):
    offset = 0; max_align = 1; layout = []
    for name, size, align in fields:
        max_align = max(max_align, align)
        if offset % align != 0: offset += align - (offset % align)
        layout.append((name, offset)); offset += size
    if offset % max_align != 0: offset += max_align - (offset % max_align)
    return offset, layout
