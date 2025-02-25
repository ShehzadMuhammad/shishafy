from django.test import TestCase
from graphene.test import Client
from graphql_relay.node.node import to_global_id

from core.schema import OrderAddressNode, schema
from core.tests.factories import OrderAddressFactory

client = Client(schema)


class TestOrderAddressNode(TestCase):
    def setUp(self):
        self.order_address_1 = OrderAddressFactory(city="Milton")
        self.order_address_2 = OrderAddressFactory()
        self.order_address_3 = OrderAddressFactory(city="Milton")
        self.order_address_query = """
            query getOrderAddress($id: ID!){
                orderAddress(id: $id){
                    id
                    primaryStreetAddress
                    postalCode
                    city
                }
            }
        """
        self.all_order_addresses_query = """
            query getAllOrderAddresses{
                allOrderAddresses{
                    edges{
                        node{
                            id
                            primaryStreetAddress
                            postalCode
                            city
                        }
                    }
                }
            }
        """

        self.order_addresses_by_city = """
            query getAllOrderAddressesByCity($city: String){
                allOrderAddresses(city: $city){
                    edges{
                        node{
                            id
                            primaryStreetAddress
                            postalCode
                            city
                        }
                    }
                }
            }
        """

    def test_It_ReturnsOrderAddressById(self):
        result = client.execute(
            self.order_address_query,
            variables={"id": to_global_id(OrderAddressNode, self.order_address_1.id)},
        )
        data = result["data"]["orderAddress"]

        self.assertEqual(self.order_address_1.postal_code, data["postalCode"])
        self.assertEqual(self.order_address_1.city, data["city"])
        self.assertEqual(
            self.order_address_1.primary_street_address, data["primaryStreetAddress"]
        )

    def test_It_ReturnsAllOrderAddresses(self):
        result = client.execute(self.all_order_addresses_query)
        data = result["data"]["allOrderAddresses"]["edges"]

        self.assertEqual(len(data), 3)
        with self.subTest("Assert each postal code is in query"):
            postal_codes = [address["node"]["postalCode"] for address in data]
            self.assertIn(self.order_address_1.postal_code, postal_codes)
            self.assertIn(self.order_address_2.postal_code, postal_codes)
            self.assertIn(self.order_address_3.postal_code, postal_codes)

    def test_It_ReturnsOrderAddressesByCity(self):
        result = client.execute(
            self.order_addresses_by_city, variables={"city": "Milton"}
        )
        data = result["data"]["allOrderAddresses"]["edges"]

        self.assertEqual(len(data), 2)
