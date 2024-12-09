from factory.django import DjangoModelFactory
from core.models import OrderItem
from factory import LazyAttribute
from .providers import faker
from random import uniform


class OrderItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem

    name = LazyAttribute(lambda _: faker.order_item()[0])
    category = LazyAttribute(lambda _: faker.order_item()[1])
    cost = LazyAttribute(lambda _: round(uniform(15.00, 45.00), 2))
