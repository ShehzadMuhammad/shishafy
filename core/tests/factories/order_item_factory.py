from factory.django import DjangoModelFactory
from core.models.order_item import OrderItem, CategoryType
from factory import LazyAttribute, post_generation
from .providers import faker
from random import uniform


class OrderItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem

    name = LazyAttribute(lambda _: faker.order_item()[0])
    category = LazyAttribute(lambda _: faker.order_item()[1])
    cost = LazyAttribute(lambda _: round(uniform(15.00, 45.00), 2))
    associated_flavour = None

    @classmethod
    def create_extra_with_flavour(cls, available_flavours):
        extra_item = cls(name="Head", category=CategoryType.EXTRA)
        if available_flavours:
            extra_item.associated_flavour = faker.random_element(available_flavours)
        return extra_item
