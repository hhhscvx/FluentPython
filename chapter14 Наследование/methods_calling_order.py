class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        return f'<instance of {cls_name}'


class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()


class B(Root):
    """Метод, вызывающий super называется кооперативным (как ping)"""
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')


class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()


l1 = Leaf()
l1.ping()  # Leaf -> A -> B -> Root (от самого себя, вверх по цепочке родителей)
print()
l1.pong()  # A -> B (у самого себя нет pong, а B не вызывает super)

# эти последовательности определяет MRO
