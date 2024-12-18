from .interactor import Interactor
from core.models import OrderAddress


class CreateAddressInteractor(Interactor):
    class Inputs:
        primary_street_address: str
        secondary_street_address: str = None
        postal_code: str
        city: str

    def _execute(self, **inputs):
        return OrderAddress.objects.create(
            primary_street_address=inputs.get("primary_street_address"),
            secondary_street_address=inputs.get("secondary_street_address"),
            postal_code=inputs.get("postal_code"),
            city=inputs.get("city"),
        )
