from dataclasses import dataclass, asdict


@dataclass
class DemoNTClass:
    a: int
    b: float = 1.1
    c: str = 'spam'


nt = DemoNTClass(8)
print(asdict(nt))
print(nt.__annotations__)


class Trash:
    def __init__(self, lst: list = []) -> None:
        # нельзя добавлять списки в классы (будет один list на всех)
        self.lst = lst

    def __repr__(self):
        return str(self.__dict__)


t1 = Trash()
t1.lst.append('1')
print(t1)

t2 = Trash()
print(t2)
