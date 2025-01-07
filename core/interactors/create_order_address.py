from .interactor import Interactor
from core.models import OrderAddress


class CreateOrderAddressInteractor(Interactor):
    class Inputs:
        primary_street_address: str
        secondary_street_address: str = None
        postal_code: str
        city: str

    def validate(self):
        return True

    def _execute(self):
        return OrderAddress.objects.create(
            primary_street_address=self.primary_street_address,
            secondary_street_address=self.secondary_street_address,
            postal_code=self.postal_code,
            city=self.city,
        )
