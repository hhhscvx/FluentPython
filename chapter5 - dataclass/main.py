# class Coordinate:
#     def __init__(self, lat, lon):
#         self.lat = lat
#         self.lon = lon

# moscow = Coordinate(55.756, 37.617)
# print(moscow)  # bruh
# <__main__.Coordinate object at 0x7802ca812c50>
# """
#    Обычное построение классов может быть неудобно,
#    т.к. repr не особо полезен, eq сравнивает просто
#    идентификаторы, а прописывая init надо упомянуть
#    каждый атрибут 3 раза
# """
from collections import namedtuple
from typing import NamedTuple, get_type_hints
from dataclasses import dataclass, fields, asdict, replace

Coordinate = namedtuple('Coordinate', 'lat lon')

moscow = Coordinate(55.756, 37.617)
print(moscow)  # уже куда лучше
print(moscow == Coordinate(55.756, 37.617))

'-----------------------------'


class Coordinate(NamedTuple):  # на самом деле наследует tuple, а не NamedTuplei
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


moscow = Coordinate(55.756, 37.617)
print(moscow)
moscow2 = eval(repr(moscow))
print(moscow == moscow2)
print(get_type_hints(Coordinate))

'-----------------------------'


@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


moscow = Coordinate(55.756, 37.617)

print([f.name for f in fields(moscow)])
print(asdict(moscow))
moscow = replace(moscow, lon=36.507)
print(asdict(moscow))
