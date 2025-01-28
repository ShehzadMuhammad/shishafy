import re
from .interactor import Interactor
from core.models import OrderAddress
from django.core.exceptions import ValidationError


class CreateOrderAddressInteractor(Interactor):
    class Inputs:
        primary_street_address: str
        secondary_street_address: str = None
        postal_code: str
        city: str

    def validate(self):
        postal_code_pattern = r"^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$"
        if not re.match(postal_code_pattern, self.postal_code):
            raise ValidationError(
                "Invalid postal code format. Must be in the format 'A1A 1A1'."
            )

    def _execute(self):
        return OrderAddress.objects.create(
            primary_street_address=self.primary_street_address,
            secondary_street_address=self.secondary_street_address,
            postal_code=self.postal_code,
            city=self.city,
        )
