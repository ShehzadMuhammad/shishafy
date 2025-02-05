from django.core.validators import RegexValidator
from django.db.models import CharField, Model


class Customer(Model):
    name = CharField(max_length=65)
    email = CharField(max_length=65)
    phone_number = CharField(
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\d{10}$",
                message="Phone Number mustb be exactly 10 digits ie 4162341111",
            )
        ],
    )

    def __str__(self):
        return f"{self.name} - {self.phone_number} - {self.email}"
