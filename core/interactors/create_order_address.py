import re

from django.core.exceptions import ValidationError

from core.models import OrderAddress

from .interactor import Interactor


class CreateOrderAddressInteractor(Interactor):
    class Inputs:
        primary_street_address: str
        secondary_street_address: str = None
        postal_code: str
        city: str

    def _clean(self):
        self.city = self.city.title()
        self.postal_code = re.sub(r"[^A-Za-z0-9]", "", self.postal_code).upper()

    def _validate(self):
        if OrderAddress.objects.filter(
            primary_street_address=self.primary_street_address
        ).exists():
            raise ValidationError("This Address already exists.")

        if OrderAddress.objects.filter(postal_code=self.postal_code).exists():
            raise ValidationError("This Postal Code already exists.")

    def _execute(self):
        return OrderAddress.objects.create(
            primary_street_address=self.primary_street_address,
            secondary_street_address=self.secondary_street_address,
            postal_code=self.postal_code,
            city=self.city,
        )
