class Quantity:
    def __init__(self, storage_name) -> None:
        self.storage_name = storage_name

    def __set__(self, instance: object, value: int) -> None:
        if value <= 0:
            raise ValueError(f'{self.storage_name} must be > 0')
        instance.__dict__[self.storage_name] = value

    def __get__(self, instance: object, owner: object) -> str:
        return instance.__dict__[self.storage_name]


class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description: str, weight: float, price: float) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price


li = LineItem('guts sword', weight=150, price=999)
print(li.subtotal())
print(li.weight)
# li = LineItem('guts sword', weight=-150, price=999) # err
