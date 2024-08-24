from typing import NamedTuple


class Card(NamedTuple):
    rank: str
    suit: str


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position) -> Card:
        return self._cards[position]


deck = FrenchDeck()
print(deck.ranks)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: Card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * 4 + suit_values[card.suit]


for card in sorted(deck, key=spades_high): # отсортировали по мастям и числам
    print(card)
