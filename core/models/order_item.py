from django.db.models import Model, CharField, DecimalField, TextChoices


class CategoryType(TextChoices):
    FLAVOUR = "FLAVOUR", "Flavour"
    EXTRA = "EXTRA", "Extra"


class OrderItem(Model):
    name = CharField(max_length=100)
    category = CharField(max_length=20, choices=CategoryType.choices)
    cost = DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Category - {self.category} - {self.name} - Cost: ${self.cost}"
