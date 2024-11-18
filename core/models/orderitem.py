from django.db.models import (
    Model,
    CharField,
    DecimalField,
)


class OrderItem(Model):
    CATEGORY_TYPES = [("FLAVOUR", "Flavour"), ("EXTRA", "Extra")]
    name = CharField(max_length=100)
    category = CharField(max_length=20, choices=CATEGORY_TYPES)
    cost = DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Category - {self.category} - {self.name} - Cost: ${self.cost}"
