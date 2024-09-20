import itertools
import operator


# как map, только каждый элемент распаковывает как *, т.е. смарт для подобных списков: [(1, 2), (2, 4)]
print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))


print(list(itertools.chain('ABC', range(2))))  # ['A', 'B', 'C', 0, 1]

print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))

print(list(itertools.product('ABC')))
print(list(itertools.product('ABC', repeat=2)))

print(list(map(operator.mul, range(11), itertools.repeat(5))))  # все в range(11) умножаем на 5


animals = ['duck', 'eagle', 'rag', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']

for char, group in itertools.groupby(sorted(animals, key=len), key=len):
    print(f'{char} -> {list(group)}')

for char, group in itertools.groupby('LLLLAAGGG'):  # встречающиеся подряд совпадающие по key
    print(f'{char} -> {list(group)}')
