from factory.django import DjangoModelFactory
from core.models import OrderAddress
from .providers import faker
from factory import LazyAttribute


class OrderAddressFactory(DjangoModelFactory):
    class Meta:
        model = OrderAddress

    primary_street_address = LazyAttribute(lambda _: faker.address())
    city = LazyAttribute(lambda _: faker.city())
    postal_code = LazyAttribute(lambda _: faker.postal_code())
