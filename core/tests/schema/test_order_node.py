from django.test import TestCase
from core.tests.factories import OrderFactory, OrderItemFactory


class TestOrderNode(TestCase):
    def setUp(self):
        self.order_1 = OrderFactory()

    def test_It_ReturnsOrderWithItems(self):
        print(f"Order ID: {self.order_1.id}")
        print(f"Order Items: {list(self.order_1.items.all())}")
        print(f"Total Cost: {self.order_1.total_cost}")
