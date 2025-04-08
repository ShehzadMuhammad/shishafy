from django.test import TestCase
from graphene.test import Client

from core.models import OrderAddress
from core.schema import schema
from core.tests.factories import OrderAddressFactory

client = Client(schema)


class TestCreateOrderAddress(TestCase):
    def setUp(self):
        self.order_address = OrderAddressFactory(
            primary_street_address="433 String Cres", postal_code="L9T4A3"
        )
        self.create_order_address_mutation = """
        mutation createOrderAddress($input: CreateOrderAddressInput!) {
            createOrderAddress(input: $input) {
                orderAddress{
                    id
                }
            }
        }
        """

    def test_It_CreatesNewOrderAddress(self):
        variables = {
            "input": {
                "primaryStreetAddress": "453 Nairn Circle",
                "postalCode": "L9T 8A8",
                "city": "Milton",
            }
        }
        response = client.execute(
            self.create_order_address_mutation, variables=variables
        )

        self.assertNotIn("errors", response)

        order_address = OrderAddress.objects.filter(city="Milton").first()

        with self.subTest("Newly Created Order Address has right values"):
            self.assertEqual("453 Nairn Circle", order_address.primary_street_address)
            self.assertEqual("L9T8A8", order_address.postal_code)
            self.assertEqual("Milton", order_address.city)

    def test_It_RaisesError_When_AddressIsAlreadyInUse(self):
        variables = {
            "input": {
                "primaryStreetAddress": "433 String Cres",
                "postalCode": "LWFS@",
                "city": "Milton",
            }
        }

        response = client.execute(
            self.create_order_address_mutation, variables=variables
        )

        self.assertIn("errors", response)

        error_message = response["errors"][0]["message"]
        self.assertIn("Validation Error", error_message)

    def test_It_RaisesError_When_PostalCodeIsAlreadyInUse(self):
        variables = {
            "input": {
                "primaryStreetAddress": "2221 Yonge Street",
                "postalCode": "L9T 4A3",
                "city": "Milton",
            }
        }

        response = client.execute(
            self.create_order_address_mutation, variables=variables
        )

        self.assertIn("errors", response)

        error_message = response["errors"][0]["message"]
        self.assertIn("Validation Error", error_message)
