from django.test import TestCase
from graphene.test import Client
from core.tests.factories import OrderItemFactory
from graphql_relay.node.node import to_global_id
from core.schema import schema, OrderItemNode

client = Client(schema)


class TestOrderItemNode(TestCase):
    def setUp(self):
        self.order_item = OrderItemFactory()
        self.order_item_query = """
            query getOrderItem($id: ID!){
                    orderItem(id: $id){
                    id
                    name 
                    cost
                    category
                }
            }
        """

    def test_It_ReturnsOrderItem(self):
        result = client.execute(
            self.order_item_query,
            variables={"id": to_global_id(OrderItemNode, self.order_item.id)},
        )

        print(result)
