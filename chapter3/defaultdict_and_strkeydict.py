from collections import defaultdict


my_dict = defaultdict(list, a='123')

"""по умолчанию в не найденный ключ будет помещен пустой объект первого параметра defaultdict"""
print(my_dict['z'].append('asdf'))

print(my_dict)


class MyDict(dict):
    def __missing__(self, key):
        print('этого ключа в помине не было')
        self[key] = key.__class__()
        return self


my_dict = MyDict(a='abc')

print(my_dict)
lst = ('abra',)
print(my_dict[lst])

"""------------------"""


class StrKeyDict(dict):

    def __missing__(self, key):
        """Если попадает тип данных кроме str, на
           третьей строчке он опыть пытается вернуться,
           и если не находится то опять проваливается в
           missing уже в str виде и пораждает KeyError"""
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


str_key_dict = StrKeyDict([('2', 'two'), ('4', 'four')])
str_key_dict['3'] = 'three'
print(str_key_dict)

print(3 in str_key_dict)
print(str_key_dict[2])
