from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class Customer:
    name: str
    fidelity: int


@dataclass(frozen=True, slots=True)
class LineItem:
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity


@dataclass(frozen=True, slots=True)
class Order:
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Promotion | None = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = Decimal(self.promotion.discount(self))
        return self.total() - discount

    def __repr__(self) -> str:
        return f'Order(total={self.total():.2f}, due={self.due():.2f})'


class Promotion(ABC):
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Вернуть скидку в виде положительной суммы в долларах"""


class FidelityPromo(Promotion):
    """5% скидка для заказчиков с 1000+ баллов лояльности"""

    def discount(self, order: Order) -> Decimal:
        rate = Decimal('0.05')
        if order.customer.fidelity >= 1000:
            return order.total() * rate
        return Decimal(0)


class BulkItemPromo(Promotion):
    """10% скидка для каждой позиции LineItem, где заказано 20+ единиц товара"""

    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal('0.1')
            return discount


class LargeOrderPromo(Promotion):
    """7% скидки для заказа, имеющего 10+ позиций"""

    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * Decimal('0.07')
        return Decimal(0)
