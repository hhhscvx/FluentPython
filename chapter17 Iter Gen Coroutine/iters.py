from random import randint


def d6():
    return randint(1, 6)


d6_iter = iter(d6, 1)  # итерирует до момента, пока значение не будет 1

for roll in d6_iter:
    print(roll)
