from django.db.models import Model, CharField
from django.core.validators import RegexValidator


class OrderAddress(Model):
    primary_street_address = CharField(max_length=100)
    secondary_street_address = CharField(max_length=50, blank=True, null=True)
    postal_code = CharField(
        max_length=7,
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$",
                message="Enter a valid postal code in the format of 'A1A '1A1'.",
            )
        ],
    )
    city = CharField(max_length=25)

    def __str__(self):
        return f"Address: {self.primary_street_address} {self.secondary_street_address if self.secondary_street_address else None}, {self.postal_code}, {self.city}."

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
