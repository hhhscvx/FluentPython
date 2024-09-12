from typing import TypeVar, Protocol


T = TypeVar('T')


class Repeatable(Protocol):
    """Проверить, что x имеет метод __mul__"""

    def __mul__(self: T, repeat_count: int) -> T: ...


RT = TypeVar('RT', bound=Repeatable)  # данный тип должен поддерживать *


def double(x: RT) -> RT:
    return x * 2
