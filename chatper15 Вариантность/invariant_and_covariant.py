from typing import TypeVar, Generic


class Beverage:
    """Любой напиток"""


class Juice(Beverage):
    """Любой сок"""


class OrangeJuice(Juice):
    """Апельсиновый сок"""


T = TypeVar('T')


class BeverageDispenser(Generic[T]):
    """Автомат, параметризованный типом напитка"""

    def __init__(self, beverage: T) -> None:
        self.beverage = beverage

    def dispense(self) -> T:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
    """Установить автомат для розлива сока"""


"""
    Тут install примет только именно Juice, OrangeJuice не пройдет - это инвариантность,
    Если добавить covariant=True, то BeverageDispenser будет ковариантен, теперь и Juice, и OrangeJuice пройдут
"""
