l = [1, 2, 3]

l += [5, 6]

print(l)  # перезапишет кортеж, а у листа останется тот же объект

'-----------'

t = (1, 2, [20, 30])
try:
    t[2] += [40, 50]
except TypeError as err:  # гениально
    print(t)
    raise err
