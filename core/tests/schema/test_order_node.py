from django.test import TestCase
from core.tests.factories import OrderFactory, OrderItemFactory
from graphene.test import Client
from graphql_relay.node.node import to_global_id
from core.schema import schema, OrderNode, OrderItemNode

client = Client(schema)


class TestOrderNode(TestCase):
    def setUp(self):
        self.order_1 = OrderFactory(total_cost=60)
        self.order_2 = OrderFactory(total_cost=60)
        self.order_3 = OrderFactory(total_cost=35)

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
                          associatedFlavour {
                            id
                            name
                          }
                        }
                      }
                    }
                    totalCost
                    expectedTimeOfArrival
                }
            }
        """

        self.order_by_total_cost_query = """
            query getAllOrdersGreaterThan($totalCost: Decimal){
                allOrders(totalCost_Gt: $totalCost){
                    edges{
                        node {
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
                          expectedTimeOfArrival
                        }
                    }
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
                "associatedFlavour": (
                    None
                    if not order_item.associated_flavour
                    else {
                        "id": to_global_id(
                            OrderItemNode, order_item.associated_flavour.id
                        ),
                        "name": order_item.associated_flavour.name,
                    }
                ),
            }

            self.assertIn(order_item_data, query_items)

    def test_It_ReturnsOrdersWithTotalCostGreaterThan40(self):
        result = client.execute(
            self.order_by_total_cost_query, variables={"totalCost": 40}
        )
        data = result["data"]["allOrders"]["edges"]
        self.assertEquals(len(data), 2)
