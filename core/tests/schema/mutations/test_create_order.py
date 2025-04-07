from datetime import datetime

from django.test import TestCase
from freezegun import freeze_time
from graphene.test import Client

from core.models.order_item import CategoryType
from core.schema import schema
from core.tests.factories import (
    CustomerFactory,
    OrderAddressFactory,
    OrderFactory,
    OrderItemFactory,
)

client = Client(schema)


class TestCreateOrder(TestCase):
    def setUp(self):
        self.order = OrderFactory()
        self.order_address = OrderAddressFactory()
        self.customer = CustomerFactory()
        self.create_order_mutation = """
        mutation createOrder($input: CreateOrderInput!){
            createOrder(input: $input){
                order{
                    id
                }
            }
        }
        """

    @freeze_time("2025-04-06 05:30:00")
    def test_It_CreatesOrder(self):
        item_1 = OrderItemFactory(name="Aloha Nights", category=CategoryType.FLAVOUR)
        item_2 = OrderItemFactory()
        variables = {
            "input": {
                "items": [item_1.id, item_2.id],
                "orderAddressId": self.order_address.id,
                "customerId": self.customer.id,
                "expectedTimeOfArrival": datetime(2025, 4, 6, 5, 30).isoformat(),
                "customerNote": "Come to side of house and knock on door.",
            }
        }

        response = client.execute(self.create_order_mutation, variables=variables)
        print(response)
