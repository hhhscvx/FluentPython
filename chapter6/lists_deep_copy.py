import copy
from typing import Iterable


class Bus:
    passengers: list

    def __init__(self, passengers: Iterable | None = None) -> None:
        if not passengers:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2: Bus = copy.copy(bus1)
bus3: Bus = copy.deepcopy(bus1)

print(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')
print(bus2.passengers)  # copy     | внутренний list лишь ссылка на list в bus1
print(bus3.passengers)  # deepcopy | внутренний list скопировался в отдельный
