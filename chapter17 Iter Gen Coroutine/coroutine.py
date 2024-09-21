from collections.abc import Generator


def averager() -> Generator[float, float, None]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


coro_avg = averager()
next(coro_avg)
print('*' * 40)
print()

print(coro_avg.send(10))  # TypeVar у Generator контрвариантен, поэтому мы можем передавать int помимо float (ПИЗДЕЦ ГЕНИАЛЬНО)
print(coro_avg.send(30))
print(coro_avg.send(5))
