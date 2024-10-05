from abc import ABC, abstractmethod


class Validate(ABC):
    def __set_name__(self, owner: object, name: str) -> None:
        self.storage_name = name

    def __set__(self, instance: object, value: str) -> None:
        value = self.validate(self.storage_name, value)
        instance.__dict__[self.storage_name] = value

    @abstractmethod
    def validate(self, name: str, value: str):
        """Вернуть проверенное значение value, либо возбудить ValueError"""
