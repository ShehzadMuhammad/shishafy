from django.test import TestCase
from core.tests.factories import OrderFactory, OrderItemFactory
from graphene.test import Client
from graphql_relay.node.node import to_global_id
from core.schema import schema, OrderNode, OrderItemNode

client = Client(schema)


class TestOrderNode(TestCase):
    def setUp(self):
        self.order_1 = OrderFactory()

        self.order_query = """
            query getOrder($id: ID!){
                order(id: $id){
                    id
                    orderAddress {
                        id
                        city
                    }
                    items{
                      edges {
                        node {
                          id
                          name
                          cost
                          category
                        }
                      }
                    }
                    totalCost
                    estimatedTimeOfArrival
                }
            }
"""

    def test_It_ReturnsOrderWithId(self):
        result = client.execute(
            self.order_query, variables={"id": to_global_id(OrderNode, self.order_1.id)}
        )
        data = result["data"]["order"]

        self.assertEquals(self.order_1.order_address.city, data["orderAddress"]["city"])
        self.assertEquals(self.order_1.total_cost, float(data["totalCost"]))

        with self.subTest("Assert each item matches"):
            query_items = [item["node"] for item in data["items"]["edges"]]
            order_items = list(self.order_1.items.all())

        for order_item in order_items:
            order_item_data = {
                "id": to_global_id(OrderItemNode, order_item.id),
                "name": order_item.name,
                "category": order_item.category,
                "cost": str(order_item.cost),
            }

            self.assertIn(order_item_data, query_items)
