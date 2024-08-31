from collections.abc import Sequence
from random import shuffle
from typing import TypeVar, Hashable
from decimal import Decimal


T = TypeVar('T')
# 2: ограниченный TypeVar
NumberT = TypeVar('NumberT', int, float, Decimal)
# 3: тип параметры может быть Hashable или его подтипом
HashableT = TypeVar('HashableT', bound=Hashable)


def sample(population: Sequence[T], size: int) -> list[T]:
    """
        Принимаем на вход последовательность и одним типом,
        и возвращаем list с этим же типом. [На python3.12 щас кстати проще]
    """
    if size:
        raise ValueError('size mus be >= 1')
    result = list(population)
    shuffle(result)
    return result[:size]
