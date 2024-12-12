from factory.django import DjangoModelFactory
from core.models import Order
from factory import LazyAttribute, SubFactory, post_generation
from random import uniform
from .order_address_factory import OrderAddressFactory
from .order_item_factory import OrderItemFactory
from .providers import faker


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    order_address = SubFactory(OrderAddressFactory)
    total_cost = LazyAttribute(lambda _: round(uniform(45.00, 45.00), 2))
    estimated_time_of_arrival = LazyAttribute(lambda _: faker.date())

    @post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for item in extracted:
                self.items.add(item)
        else:
            for _ in range(faker.random_int(min=1, max=3)):
                self.items.add(OrderItemFactory())
