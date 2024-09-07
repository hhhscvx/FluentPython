import math
from array import array


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y) -> None:
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self.x!r}, {self.y!r})'

    def __str__(self) -> str:
        return str(tuple(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __bytes__(self) -> str:
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other: object) -> bool:
        return tuple(self) == tuple(other)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __format__(self, format_spec: str = '') -> str:
        components = (format(c, format_spec) for c in self)  # отформатированные self.__x и self.__y
        return '({}, {})'.format(*components)

    def __hash__(self) -> hash:
        return hash((self.x, self.y))


print(repr(Vector2d(1, 2)))
