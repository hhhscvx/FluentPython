import quantity_nonblank as model


class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description: str, weight: float, price: float) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price


li = LineItem('guts sword', weight=150, price=999)
# li = LineItem('', weight=150, price=999)  # err
