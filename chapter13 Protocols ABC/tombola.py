from abc import ABC, abstractmethod
from collections.abc import Iterable


class Tombola(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def load(self, iterable: Iterable):
        """Добавить элементы из итерируемого объекта в контейнер"""

    @abstractmethod
    def pick(self):
        """Удалить случайный элемент и вернуть его

        Должен возбуждать LookupError, если объект пуст
        """

    def loaded(self):
        """Вернуть True, если есть хотя бы 1 элемент"""
        return bool(self.inspect())

    def inspect(self):
        """Вернуть отсортированный кортеж, содержащий оставшиеся в данный момент элементы"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)


# Интерфейс - это чисто абстракция, а абстрактный класс - когда есть какой-то функционал
# Абстрактные методы могут иметь функционал, но дочерние классы энивей должны его переопределить, но можно и юзать через super()
