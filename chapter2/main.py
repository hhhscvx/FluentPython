from pprint import pprint


colors = ['black', 'white']
sizes = ['S', 'M', 'L']

res = [(color, size) for size in sizes for color in colors]
pprint(res)

# Вариант ниже занимает 0 памяти

for tshirt in (f'{color} {size}' for size in sizes for color in colors):
    print(tshirt)
