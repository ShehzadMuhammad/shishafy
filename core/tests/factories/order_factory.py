from random import uniform

from factory import LazyAttribute, SubFactory, post_generation
from factory.django import DjangoModelFactory

from core.models import Order
from core.models.order_item import CategoryType

from .customer_factory import CustomerFactory
from .order_address_factory import OrderAddressFactory
from .order_item_factory import OrderItemFactory
from .providers import faker


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    order_address = SubFactory(OrderAddressFactory)
    customer = SubFactory(CustomerFactory)
    total_cost = LazyAttribute(lambda _: round(uniform(35.00, 125.00), 2))
    expected_time_of_arrival = LazyAttribute(lambda _: faker.date())

    @post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            return

        flavour_items = [
            OrderItemFactory(category=CategoryType.FLAVOUR)
            for _ in range(faker.random_int(min=1, max=3))
        ]
        self.items.add(*flavour_items)

        if faker.boolean(chance_of_getting_true=50):
            extra_item = OrderItemFactory(
                name="Head",
                category=CategoryType.EXTRA,
                associated_flavour=OrderItemFactory.create_extra_with_flavour(
                    flavour_items
                ),
            )
            self.items.add(extra_item)

        if extracted:
            for item in extracted:
                self.items.add(item)
