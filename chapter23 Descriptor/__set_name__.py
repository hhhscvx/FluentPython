class Quantity:
    def __set_name__(self, owner: object, name: str) -> None:
        """
        :param str name: содержит имя присваиваемой переменной (ахуеть)
        """
        print('Name:', name)
        self.storage_name = name

    def __set__(self, instance: object, value: int) -> None:
        if value <= 0:
            raise ValueError(f'{self.storage_name} must be > 0')
        instance.__dict__[self.storage_name] = value



class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description: str, weight: float, price: float) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price


li = LineItem('guts sword', weight=150, price=999)
