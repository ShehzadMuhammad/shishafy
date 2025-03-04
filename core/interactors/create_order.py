from datetime import datetime

from django.core.exceptions import ValidationError

from core.models import Customer, Order, OrderAddress
from core.models.order_item import CategoryType, OrderItem

from .interactor import Interactor


class CreateOrder(Interactor):
    class Inputs:
        items: list[int]
        expected_time_of_arrival: datetime
        customer_note: str
        order_address_id: int
        customer_id: int

    def _clean(self):
        self.customer_note = self.customer_note.lower()

    def _validate(self):
        self.items = [
            OrderItem.objects.filter(id=item.id).first() for item in self.items
        ]
        if not self.items.filter(category=CategoryType.FLAVOUR).exists():
            raise ValidationError("A Flavour wasn't provided for this order")

        if not OrderAddress.objects.filter(id=self.order_address_id).exists():
            raise ValidationError("There isn't a valid address attached to this order.")

        if not Customer.objects.filter(id=self.customer_id).exists():
            raise ValidationError(
                "There isn't a valid customer attached to this order."
            )

    def _execute(self):
        total_cost = sum(item.cost for item in self.items)
        return Order.objects.create(
            items=self.items,
            total_cost=total_cost,
            order_address=self.order_address_id,
            customer=self.customer_id,
        )
