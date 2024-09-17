from typing import Self
import math


class Vector2d:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        x = self.x + other.x
        y = self.y + other.y
        return Vector2d(x, y)

    def __mul__(self, scalar: int) -> Self:
        return Vector2d(self.x * scalar, self.y * scalar)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'

    """Что-то новое снизу"""

    def __neg__(self):
        """-v"""
        return Vector2d(*[-x for x in (self.x, self.y)])

    def __pos__(self):
        """+v"""
        return Vector2d(self.x, self.y)


v = Vector2d(2, 4)
print(v)
print(-v)
print(+v)

"""
    Перегрузка это халява, но не знал про +v, -v, и ~x (-x - 1)
    __add__ это Vector + other, а __radd__ это other + Vector
"""
