import random


class BingoCage:
    def __init__(self, items: list) -> None:
        self._items = items
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):  # теперь к экземпляру можно обращаться как к функции
        return self.pick()

    def __str__(self) -> str:
        return f'{self._items}'


bingo = BingoCage([1, 2, 3])

print(bingo.pick())

print(bingo())

print(bingo)
