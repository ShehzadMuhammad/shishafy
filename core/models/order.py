from django.db.models import (
    Model,
    CharField,
    DecimalField,
    ManyToManyField,
    DateTimeField,
    ForeignKey,
    PROTECT,
)

from .order_item import OrderItem
from .order_address import OrderAddress


class Order(Model):
    items = ManyToManyField(OrderItem, related_name="orders")
    total_cost = DecimalField(max_digits=10, decimal_places=2)
    order_address = ForeignKey(OrderAddress, on_delete=PROTECT)
    expected_time_of_arrival = DateTimeField()
    customer_note = CharField(max_length=255, null=True, blank=True)
    created_on = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - Created: {self.created_on} - Total: ${self.total_cost} - Address: {self.order_address.primary_street_address}, {self.order_address.city} - ETA: {self.expected_time_of_arrival}"
