from django.test import TestCase
from graphene.test import Client
from core.tests.factories import OrderAddressFactory
from graphql_relay.node.node import to_global_id
from core.schema import schema, OrderAddressNode

client = Client(schema)


class TestOrderAddressNode(TestCase):
    def setUp(self):
        self.order_address_1 = OrderAddressFactory()
        self.order_address_2 = OrderAddressFactory()
        self.order_address_3 = OrderAddressFactory()
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

    def test_It_ReturnsOrderAddress(self):
        result = client.execute(
            self.order_address_query,
            variables={"id": to_global_id(OrderAddressNode, self.order_address_1.id)},
        )
        data = result["data"]["orderAddress"]

        self.assertEquals(self.order_address_1.postal_code, data["postalCode"])
        self.assertEquals(self.order_address_1.city, data["city"])
        self.assertEquals(
            self.order_address_1.primary_street_address, data["primaryStreetAddress"]
        )
