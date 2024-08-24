

import os


symbols = (123, 321, 2, 1, 5)

print(symbols)

print(os.path.split('/home/kirill/PycharmProjects/FluentPython/chapter2/tuple.py'))

print(*list(range(5)))

addr = ('Tokyo', 'JP', 36.933, (35.52389, 139.876921))

name, _, _, (lat, lon) = addr  # распаковка кортежа внутри кортежа

match addr:
    case [str(name), _, _, (float(lat), float(lon)) as coord] if lon >= 0:  # расширенные возможности case
        print(f'{name:15} | {lat: 9.4f} | {lon: 9.4f}')
        print(coord)
    case _:
        print("Совпадений нет")

# str(name) здесь служит лишь для проверки типа, а не для присваивания name в str
