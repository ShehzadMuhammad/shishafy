from django.db.models import CharField, EmailField, Model


class Customer(Model):
    name = CharField(max_length=65)
    email = EmailField(unique=True)
    phone_number = CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} - {self.phone_number} - {self.email}"
