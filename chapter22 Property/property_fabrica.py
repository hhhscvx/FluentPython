def quantity(storage_name: str) -> property:
    """
        Одинаково может работать для weight, price, и чего угодно еще,
        и не надо создавать кучу getter`ов и setter`ов для каждого атрибута,
        дублируя код
    """

    def quantity_getter(instance: object) -> int:
        return instance.__dict__[storage_name]

    def quantity_setter(instance: object, value: int) -> None:
        if value <= 0:
            raise ValueError('value must be > 0')
        instance.__dict__[storage_name] = value

    return property(fget=quantity_getter, fset=quantity_setter)


class LiteItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description: str, weight: float, price: float) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price
