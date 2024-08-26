from collections.abc import Mapping, MutableMapping


def dump(**kwargs):
    return kwargs


print(dump(**{'x': 1}, y=2, **{'z': 3}))

print()

d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 2, 'c': 6}

d2 |= d1
print(d2)

print()

food = dict(type='ice cream')
match food:
    case {'type': 'ice cream', **details}:
        print(f'Ice cream details: {details}')

print()
print(isinstance(Mapping, MutableMapping))
print(isinstance(food, Mapping))
print(isinstance(food, MutableMapping))
