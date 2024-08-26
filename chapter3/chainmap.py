from collections import ChainMap

d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)

chain = ChainMap(d1, d2)

chain['c'] = -1  # изменит у первого dict`а

print(chain)  # ChainMap({'a': 1, 'b': 3}, {'a': 2, 'b': 4, 'c': 6})
print(dict(chain))  # {'a': 1, 'b': 3, 'c': 6}
print(dict(chain) == d1)
print(dict(chain) == d2)

# useful когда надо найти какое-то значение среди нескольких диктов
