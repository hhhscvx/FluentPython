from functools import reduce
import math
import operator
import reprlib
from array import array


class Vector:
    typecode = 'd'

    def __init__(self, components) -> None:
        self._components = array(self.typecode, components)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        components = reprlib.repr(self._components)
        # не Vector(array('d', [3.0, 4.0, 5.0])), а Vector([3.0, 4.0, 5.0])
        components = components[components.find('['):-1]
        class_name = type(self).__name__
        return f'{class_name}({components})'

    def __str__(self) -> str:
        return str(tuple(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __bytes__(self) -> str:
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    # def __eq__(self, other: object) -> bool:
    #     if len(self) != len(other):
    #         return False
    #     for a, b in zip(self, other):
    #         if a != b:  # прям кайф бля
    #             return False
    #     return True

    def __eq__(self, other: object) -> bool:
        """ЕЩЕ БОЛЬШЕ КАЙФ АААА"""
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __abs__(self) -> float:
        return math.hypot(*self)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __format__(self, format_spec: str = '') -> str:
        components = (format(c, format_spec) for c in self)  # отформатированные self.__x и self.__y
        return '({}, {})'.format(*components)

    def __hash__(self):
        """Применение map к reduce (изменение map к каждому элементу и ко всем reduce)"""
        hashes = map(hash, self._components)
        return reduce(operator.xor, hashes)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(cls)
            return cls(self._components[key])
        index = operator.index(key)  # в основном это чтоб нельзя было передать float
        return self._components(index)
