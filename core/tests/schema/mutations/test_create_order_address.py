from django.test import TestCase
from graphene.test import Client
from core.schema import schema
from core.models import OrderAddress
from django.core.exceptions import ValidationError

client = Client(schema)


class TestCreateOrderAddress(TestCase):
    def setUp(self):
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
            self.assertEquals("453 Nairn Circle", order_address.primary_street_address)
            self.assertEquals("L9T 8A8", order_address.postal_code)
            self.assertEquals("Milton", order_address.city)

    def test_If_IncorrectPostalCodeProvided_It_RaisesError(self):
        variables = {
            "input": {
                "primaryStreetAddress": "453 Nairn Circle",
                "postalCode": "LWFS@",
                "city": "Milton",
            }
        }

        with self.assertRaises(ValidationError):
            response = client.execute(
                self.create_order_address_mutation, variables=variables
            )
