import keyword
from collections.abc import Iterable, MutableSequence, Mapping
from typing import Any, Self, TypeVar


T = TypeVar('T')


class FrozenJSON:
    """my_dict.key вместо my_dict['key']"""
    def __new__(cls, arg: T) -> Self | list | T:
        if isinstance(arg, Mapping):
            return super().__new__(cls)
        elif isinstance(arg, MutableSequence):
            return [cls(item) for item in arg]
        return arg

    def __init__(self, mapping: Mapping) -> None:
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):  # зарезервированное слово
                key += '_'

    def __getattr__(self, name: str) -> Any:
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return FrozenJSON(self.__data[name])

    def __dir__(self) -> Iterable[str]:
        return self.__data.keys()
