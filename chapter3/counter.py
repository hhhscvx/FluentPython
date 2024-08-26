from collections import Counter

ct = Counter('abracadabra')

print(ct)
print(dict(ct))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

ct.update('aaaaazzz')

print(dict(ct))  # {'a': 10, 'b': 2, 'r': 2, 'c': 1, 'd': 1, 'z': 3}

print(ct.most_common(3))  # [('a', 10), ('z', 3), ('b', 2)]

# Ну а че, гениально в некоторых кейсах
