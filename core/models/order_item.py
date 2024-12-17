from django.db.models import (
    Model,
    CharField,
    DecimalField,
    TextChoices,
    ForeignKey,
    PROTECT,
)


class CategoryType(TextChoices):
    FLAVOUR = "FLAVOUR", "Flavour"
    EXTRA = "EXTRA", "Extra"


class OrderItem(Model):
    name = CharField(max_length=100)
    category = CharField(max_length=20, choices=CategoryType.choices)
    cost = DecimalField(max_digits=4, decimal_places=2)
    associated_flavour = ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=PROTECT,
        limit_choices_to={"category": CategoryType.FLAVOUR},
        related_name="extras",
        help_text="Associate this extra with a flavour.",
    )

    def __str__(self):
        if self.category == CategoryType.EXTRA and self.associated_flavour:
            return f"Category - {self.category} - {self.name} (Flavour: {self.associated_flavour.name}) - Cost: ${self.cost}"
        return f"Category - {self.category} - {self.name} - Cost: ${self.cost}"
