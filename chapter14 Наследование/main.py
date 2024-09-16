"""Почему не надо наследовать от встроенных типов (а например от UserDict):"""
from collections import UserDict


# class DoppelDict(dict):  # если сделать так - код не работает как задуманно
class DoppelDict(UserDict):
    def __setitem__(self, key, value) -> None:
        return super().__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)
print(dd)

dd['two'] = 2  # только это затригерилло нужный нам __setitem__
print(dd)

dd.update(three=3)
print(dd)
