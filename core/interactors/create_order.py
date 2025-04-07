from datetime import datetime

import pytz
from django.core.exceptions import ValidationError
from django.utils.timezone import is_aware, localtime, make_aware, now

from core.models import Customer, Order, OrderAddress
from core.models.order_item import CategoryType, OrderItem

from .interactor import Interactor


class CreateOrderInteractor(Interactor):
    class Inputs:
        items: list[int]
        expected_time_of_arrival: datetime
        customer_note: str
        order_address_id: int
        customer_id: int

    def _clean(self):
        self.customer_note = self.customer_note.lower()

        EST = pytz.timezone("America/Toronto")
        self.expected_time_of_arrival = (
            localtime(self.expected_time_of_arrival, timezone=EST)
            if is_aware(self.expected_time_of_arrival)
            else make_aware(self.expected_time_of_arrival)
        )

    def _validate(self):
        self.items = OrderItem.objects.filter(id__in=self.items)
        if not self.items.filter(category=CategoryType.FLAVOUR).exists():
            raise ValidationError("A Flavour wasn't provided for this order")

        if not OrderAddress.objects.filter(id=self.order_address_id).exists():
            raise ValidationError("There isn't a valid address attached to this order.")

        if not Customer.objects.filter(id=self.customer_id).exists():
            raise ValidationError(
                "There isn't a valid customer attached to this order."
            )

        current_time = now()

        if self.expected_time_of_arrival < current_time:
            raise ValidationError("You can't book a time in the past.")

    def _execute(self):
        total_cost = sum(item.cost for item in self.items)
        order_address = OrderAddress.objects.filter(id=self.order_address_id).first()
        customer = Customer.objects.filter(id=self.customer_id).first()
        order = Order.objects.create(
            total_cost=total_cost,
            order_address=order_address,
            customer=customer,
            expected_time_of_arrival=self.expected_time_of_arrival,
            customer_note=self.customer_note,
        )

        order.items.add(*self.items)

        return order
