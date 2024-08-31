from typing import TypeVar, Protocol, Sequence


number = int | float


class DoubleProtocol(Protocol):
    def __mul__(self, other: number) -> number: ...


T = TypeVar('T', bound=DoubleProtocol)


def double(x: Sequence[T]) -> T:
    return x * 2
