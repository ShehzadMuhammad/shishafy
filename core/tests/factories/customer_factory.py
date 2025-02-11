from factory import LazyAttribute
from factory.django import DjangoModelFactory

from core.models import Customer

from .providers import faker


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    first_name = LazyAttribute(lambda _: faker.first_name())
    last_name = LazyAttribute(lambda _: faker.first_name())
    email = LazyAttribute(lambda _: faker.email())
    phone_number = LazyAttribute(lambda _: faker.phone_number())
