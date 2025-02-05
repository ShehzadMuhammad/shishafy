from core.models import Customer

from .interactor import Interactor


class CreateCustomerInteractor(Interactor):
    class Inputs:
        name: str
        email: str
        phone_number: str

    def validate(self):
        return None

    def _execute(self):
        return Customer.objects.create(
            name=self.name, email=self.email, phone_number=self.phone_number
        )
