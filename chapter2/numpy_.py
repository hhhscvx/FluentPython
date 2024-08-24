import numpy as np


a = np.arange(12)
print(a)

print(a.shape)

a.shape = 3, 4
print(a)
print(a[2][1], a[2, 1])

a = a.transpose()  # гениально
print(a)
