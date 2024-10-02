from django.db.models import (
    Model,
    CharField,
    DecimalField,
    ManyToManyField,
    DateTimeField,
)


# Create your models here.
class OrderItem(Model):
    ITEM_TYPES = [("FLAVOUR", "Flavour"), ("EXTRA_HEAD", "Extra_Head")]
    name = CharField(max_length=100)
    item_type = CharField(max_length=20, choices=ITEM_TYPES)
    cost = DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Item Type - {self.item_type} - {self.name} - Cost: {self.cost}"


class Order(Model):
    items = ManyToManyField(OrderItem, related_name="orders")
    total_cost = DecimalField(max_digits=10, decimal_places=2)
    order_address = CharField(max_length=255)
    estimated_time_of_arrival = DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id} - Total: ${self.total_cost} - Address: {self.order_address} - ETA: {self.estimated_time_of_arrival}"
