from array import array
from random import random

floats = array('d', (random() for _ in range(10**7)))
print(floats[-1])

with open('chapter2/floats.bin', 'wb') as fp:
    floats.tofile(fp)  # функционал шире чем у list

with open('chapter2/floats.bin', 'rb') as fp:
    floats2 = array('d')
    floats2.fromfile(fp, 10**7)

print(floats2[-1])
print(floats2 == floats)
