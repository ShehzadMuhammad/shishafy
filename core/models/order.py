from django.db.models import (
    Model,
    CharField,
    DecimalField,
    ManyToManyField,
    DateTimeField,
)

from .order_item import OrderItem


class Order(Model):
    items = ManyToManyField(OrderItem, related_name="orders")
    total_cost = DecimalField(max_digits=10, decimal_places=2)
    order_address = CharField(max_length=255)
    estimated_time_of_arrival = DateTimeField()
    customer_note = CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id} - Total: ${self.total_cost} - Address: {self.order_address} - ETA: {self.estimated_time_of_arrival}"
