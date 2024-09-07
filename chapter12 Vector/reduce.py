from functools import reduce
import operator


n = 4
n ^= 5  # n будет равно 5 - текущее значение

print(n)

'-----'

n = 0
for i in range(1, 6):
    n ^= i

print(n)  # в ренже понятно n всегда будет 1

'------'

print(reduce(lambda a, b: a ^ b, range(6)))

'------'

print(reduce(operator.xor, range(6)))


"""У reduce еще есть третий аргумент - initializer"""


def __hash__(self):
    """Применение map к reduce (изменение map к каждому элементу и ко всем reduce)"""
    hashes = map(hash, self._components)
    return reduce(operator.xor, hashes)
