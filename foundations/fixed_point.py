"""Fixed-point decimal representation with scaling factor."""

SCALE = 10000

class FixedPoint:
    def __init__(self, val: float):
        self.raw = int(round(val * SCALE))

    def __add__(self, other):
        res = FixedPoint(0)
        res.raw = self.raw + other.raw
        return res

    def to_float(self) -> float:
        return self.raw / SCALE
