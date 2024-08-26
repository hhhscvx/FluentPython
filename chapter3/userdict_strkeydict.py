from collections import UserDict
from typing import Any
"""Переопределять dict лучше от UserDict, а не от dict"""


class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key: object) -> bool:
        return str(key) in self.data  # self.data = dict

    def __setitem__(self, key: Any, item: Any) -> None:
        self.data[str(key)] = item

    def get_self_data(self) -> dict:
        return self.data


my_dict = StrKeyDict(a=12)

print(my_dict)
print(my_dict.get_self_data())
