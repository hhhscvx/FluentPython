from collections.abc import MutableSequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Card:
    rank: str
    suit: str


class FrenchDeck2(MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position) -> Card:
        return self._cards[position]

    def __setitem__(self, position, value) -> None:
        self._cards[position] = value

    def __delitem__(self, position) -> None:
        del self._cards[position]

    def insert(self, position, value) -> None:
        self._cards.insert(position, value)


"""
    В данном примере класс не имеет особого смысла,
    он просто нужен в педагогических целях, чтоб продемонстрировать,
    что надо реализовать методы интерфейса MutableSequence.
    Так просто тут бы хватило функционала list офк
"""

f = FrenchDeck2() # если не реализованы методы MutableSequence, будет TypeError
