from __future__ import annotations
import math


class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: int) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'


v1 = Vector(1, 3)
v2 = Vector(4, 2)

print(v1 * 2)
