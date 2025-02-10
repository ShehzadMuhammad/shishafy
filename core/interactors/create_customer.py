import re

from django.core.exceptions import ValidationError

from core.models import Customer

from .interactor import Interactor


class CreateCustomerInteractor(Interactor):
    class Inputs:
        first_name: str
        last_name: str
        email: str
        phone_number: str

    def validate(self):
        phone_number = r"^\d{10}$"
        if not re.match(phone_number, self.phone_number):
            raise ValidationError(
                "Phone Number must be exactly 10 digits ie 4162341111"
            )

        if Customer.objects.filter(phone_number=self.phone_number).exists():
            raise ValidationError(
                "This Phone Number is already in use, please try another one."
            )

        if Customer.objects.filter(email=self.email).exists():
            raise ValidationError(
                "This Email is already in use, please use another one."
            )

    def _execute(self):
        return Customer.objects.create(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone_number=self.phone_number,
        )
