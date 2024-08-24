from collections import deque

dq = deque(range(10), maxlen=10)  # если длина превышает - удаляются какие-то элементы
print()
print(dq)

dq.rotate(3)
print()
print(dq)

dq.rotate(-4)
print()
print(dq)

dq.appendleft(-1)
print()
print(dq)

dq.extend([11, 22, 33])
print()
print(dq)

dq.extendleft([44, 55, 66])
print()
print(dq)
