from unicodedata import normalize, name


s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'

print(len(s1), len(s2))  # 4, 5

print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))  # 4, 4

print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))  # 4, 5

print(normalize('NFC', s1) == normalize('NFC', s2), s1 == s2)

'--------'

print(name('🤡'))
print(name('A'))
print(name('0'))
