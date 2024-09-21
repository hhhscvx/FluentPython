import itertools


class ArithmeticProgression:
    def __init__(self, begin, step, end=None) -> None:
        self.begin = begin
        self.step = step,
        self.end = end

    def __iter__(self):
        result_type = type(self.begin + self.step)
        result = result_type(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            # каждый раз result вычисляется заново, относительно начального begin (неочевидная хуйня)
            result = self.begin + self.step * index


def aritprog_gen(begin, step, end=None):
    """То же самое, но в сто раз проще (генератор лучше реализовывать как def, а не iter)"""
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


def aritprog_itertools_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(start=first, step=step)
    if end is None:
        return ap_gen
    return itertools.takewhile(lambda n: n < end)
