def make_averager():
    count = 0
    total = 0

    def averager(new_value: float) -> float:
        nonlocal count, total  # nonlocal в averager
        count += 1  # the same of `count = ...` т.е. ошибка before assignment
        total += new_value
        return total / count
    return averager
