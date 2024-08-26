from collections.abc import MutableSet, Set

needles, haystack = [0, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(set(needles) & set(haystack)))  # сколько иголок в стоге сена

'--------'

print(issubclass(set, Set))
print(issubclass(set, MutableSet))  # Mutable - изменяемый

print(issubclass(frozenset, Set))  # True
print(issubclass(frozenset, MutableSet))  # False

s = {'a', 'e', 'i'}
d = {'a': 12, 'b': 11, 'c': 13}

print(d.keys() & s)  # {'a'}

"""dict_keys и dict_items очень похожи на frozenset"""
