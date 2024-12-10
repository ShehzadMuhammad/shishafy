from django.test import TestCase
from graphene.test import Client
from core.tests.factories import OrderItemFactory
from graphql_relay.node.node import to_global_id
from core.schema import schema, OrderItemNode, CategoryTypeEnum

client = Client(schema)


class TestOrderItemNode(TestCase):
    def setUp(self):
        self.order_item_1 = OrderItemFactory()
        self.order_item_2 = OrderItemFactory()
        self.order_item_3 = OrderItemFactory()
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
        self.all_order_items_query = """
            query getAllOrderItems{
                allOrderItems{
                    edges{
                        node{
                            id
                            name
                            cost
                            category
                        }
                    }
                }
            }
        """
        self.order_items_by_category_query = """
            query getAllOrderItemsByCategory($category: String){
                allOrderItems(category: $category){
                    edges{
                        node{
                            id
                            name
                            cost
                            category
                        }
                    }
                }
            }
        """

    def test_It_ReturnsOrderItem(self):
        result = client.execute(
            self.order_item_query,
            variables={"id": to_global_id(OrderItemNode, self.order_item_1.id)},
        )
        data = result["data"]["orderItem"]

        self.assertEquals(self.order_item_1.name, data["name"])
        self.assertEquals(self.order_item_1.cost, float(data["cost"]))
        self.assertEquals(self.order_item_1.category, data["category"])

    def test_It_ReturnsAllOrderItems(self):
        result = client.execute(self.all_order_items_query)
        data = result["data"]["allOrderItems"]["edges"]
        self.assertEquals(len(data), 3)

        with self.subTest("Assert item exists is in query"):
            items = [item["node"] for item in data]
            self.assertIn(self.order_item_2.name, [item["name"] for item in items])
            self.assertIn(
                self.order_item_2.cost, [float(item["cost"]) for item in items]
            )
            self.assertIn(
                self.order_item_2.category, [item["category"] for item in items]
            )

    def test_It_ReturnsOrderItemByCategory(self):
        result = client.execute(
            self.order_items_by_category_query,
            variables={"category": "FLAVOUR"},
        )

        data = result["data"]["allOrderItems"]["edges"]

        with self.subTest("Assert only flavour items exist"):
            items = [item["node"] for item in data]
            self.assertNotIn("EXTRA", [item["category"] for item in items])
