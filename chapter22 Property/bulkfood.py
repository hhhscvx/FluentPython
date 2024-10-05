

class LiteItem:
    def __init__(self, description: str, weight: float, price: float) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value: float) -> None:
        if value > 0:
            self.__weight = value
            return
        raise ValueError('Value must be > 0')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(description={self.description}, weight={self.weight}, price={self.price})"


li = LiteItem('desc', weight=.1, price=10.05)
print(li)
