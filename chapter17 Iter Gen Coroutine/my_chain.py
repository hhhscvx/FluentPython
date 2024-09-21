from typing import Iterable


def chain(*iterables: Iterable) -> Iterable:
    for it in iterables:
        yield from it


print(list(chain(('govno',), 'zalupa', ['penis', 'her', 'davalka', 'huy', 'blyadina'])))
