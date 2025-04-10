from datetime import datetime, timezone

from django.test import TestCase
from freezegun import freeze_time
from graphene.test import Client
from graphql_relay import from_global_id

from core.models import Order
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

    @freeze_time("2025-04-06 05:30:00", tz_offset=-4)
    def test_It_CreatesOrder(self):
        item_1 = OrderItemFactory(name="Aloha Nights", category=CategoryType.FLAVOUR)
        item_2 = OrderItemFactory()
        variables = {
            "input": {
                "items": [item_1.id, item_2.id],
                "orderAddressId": self.order_address.id,
                "customerId": self.customer.id,
                "expectedTimeOfArrival": datetime(
                    2025, 4, 6, 5, 30, tzinfo=timezone.utc
                ),
                "customerNote": "Come to side of house and knock on door.",
            }
        }

        response = client.execute(self.create_order_mutation, variables=variables)
        new_order_result = response["data"]["createOrder"]["order"]["id"]

        new_order_id = from_global_id(new_order_result)[1]

        new_order = Order.objects.filter(id=new_order_id).first()
        self.assertNotIn("errors", response)

        with self.subTest("New Order has right values"):
            self.assertEqual(self.order_address.id, new_order.order_address.id)
            self.assertEqual(self.customer.id, new_order.customer.id)
            self.assertEqual(
                datetime(2025, 4, 6, 5, 30, tzinfo=timezone.utc),
                new_order.expected_time_of_arrival,
            )
            self.assertEqual(
                "come to side of house and knock on door.", new_order.customer_note
            )

    @freeze_time("2025-04-06 05:30:00", tz_offset=-4)
    def test_It_RaisesError_WhenDateTimeSetInPast(self):
        item_1 = OrderItemFactory(name="Aloha Nights", category=CategoryType.FLAVOUR)
        variables = {
            "input": {
                "items": [item_1.id],
                "orderAddressId": self.order_address.id,
                "customerId": self.customer.id,
                "expectedTimeOfArrival": datetime(
                    2025, 2, 6, 5, 30, tzinfo=timezone.utc
                ),
                "customerNote": "Come to side of house and knock on door.",
            }
        }

        response = client.execute(self.create_order_mutation, variables=variables)
        self.assertIn("errors", response)

        error_message = response["errors"][0]["message"]
        self.assertIn("Validation Error", error_message)

    @freeze_time("2025-04-06 05:30:00", tz_offset=-4)
    def test_It_RaisesError_WhenFlavourIsntApartOfTheOrder(self):
        item_1 = OrderItemFactory(category=CategoryType.EXTRA)
        variables = {
            "input": {
                "items": [item_1.id],
                "orderAddressId": self.order_address.id,
                "customerId": self.customer.id,
                "expectedTimeOfArrival": datetime(
                    2025, 4, 6, 5, 30, tzinfo=timezone.utc
                ),
            }
        }

        response = client.execute(self.create_order_mutation, variables=variables)
        self.assertIn("errors", response)

        error_message = response["errors"][0]["message"]
        self.assertIn("Validation Error", error_message)

    @freeze_time("2025-04-06 05:30:00", tz_offset=-4)
    def test_It_RaisesError_WhenOrderAddressIsntLegitimate(self):
        item_1 = OrderItemFactory(category=CategoryType.FLAVOUR)
        variables = {
            "input": {
                "items": [item_1.id],
                "orderAddressId": 1231,
                "customerId": self.customer.id,
                "expectedTimeOfArrival": datetime(
                    2025, 4, 6, 5, 30, tzinfo=timezone.utc
                ),
            }
        }

        response = client.execute(self.create_order_mutation, variables=variables)
        self.assertIn("errors", response)
        error_message = response["errors"][0]["message"]
        self.assertIn("Validation Error", error_message)

    @freeze_time("2025-04-06 05:30:00", tz_offset=-4)
    def test_It_RaisesError_WhenCustomerIsntLegitimate(self):
        item_1 = OrderItemFactory(category=CategoryType.FLAVOUR)
        variables = {
            "input": {
                "items": [item_1.id],
                "orderAddressId": self.order_address.id,
                "customerId": 31312,
                "expectedTimeOfArrival": datetime(
                    2025, 4, 6, 5, 30, tzinfo=timezone.utc
                ),
            }
        }

        response = client.execute(self.create_order_mutation, variables=variables)
        self.assertIn("errors", response)
        error_message = response["errors"][0]["message"]
        self.assertIn("Validation Error", error_message)
