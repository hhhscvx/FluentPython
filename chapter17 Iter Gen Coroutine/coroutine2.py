from typing import TypeAlias
from dataclasses import dataclass
from collections.abc import Generator


@dataclass(frozen=True, slots=True)
class Result:
    count: int
    average: float


class Sentinel:
    def __repr__(self) -> str:
        return '<Sentinel>'


STOP = Sentinel()

SendType: TypeAlias = float | Sentinel


def averager2(
    print_received: bool = False
) -> Generator[None, SendType, Result]:  # что возвращает в yield, что принимает в yield и что return`ит
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield
        if print_received:
            print('received:', term)
        if isinstance(term, Sentinel):
            break
        total += term
        count += 1
        average = total / count
    return Result(count=count, average=average)
