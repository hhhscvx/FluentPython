from methods_calling_order import A


class U():
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()  # ебать, короче super вызывается от self в соотв. методе, а не от класса (логично)
        # Ну и тут короче от LeafUA тригеррится A и Root
        # Если бы этого тут не было, A вообще бы не вызвался, тут он вызывается как второй super

"""Это все скорее отображает неочевидное поведение наследование, а значит очередную его проблему"""

class LeafUA(U, A):
    def ping(self):
        print(f'{self}.ping() in LeafUA')
        super().ping()


u = U()
# u.ping() #  AttrErr

l2 = LeafUA()
l2.ping()
