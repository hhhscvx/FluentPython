from types import MappingProxyType
"""Неизменяемый dict"""

secret_dict = {1: 'A'}

dict_proxy = MappingProxyType(secret_dict)
print(dict_proxy)
# dict_proxy[2] = 'negri'  # TypeError

secret_dict[2] = 'B'
print(dict_proxy)  # {1: 'A', 2: 'B'}
