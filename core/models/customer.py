from django.db.models import CharField, EmailField, Model


class Customer(Model):
    first_name = CharField(max_length=65)
    last_name = CharField(max_length=65)
    email = EmailField(unique=True)
    phone_number = CharField(max_length=10, unique=True)

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} - {self.phone_number} - {self.email}"
        )
