
s = "cafè"

print(len(s))

b = s.encode('utf-8')
print(b)
print(len(b))
print(type(b))  # <class 'bytes'>

print('--------------')

cafe = bytes(s, encoding='utf-8')
print(cafe[0], cafe[1])  # каждый элемент - число 0-255
print(cafe[:1])  # какого-то хуя результат другой (b'c')

cafe_arr = bytearray(cafe)  # аргумент = bytes
print(cafe_arr)
print([el for el in cafe_arr])  # [99, 97, 102, 195, 168]

print(bytes.fromhex('C2 BF').decode('utf-8'))
