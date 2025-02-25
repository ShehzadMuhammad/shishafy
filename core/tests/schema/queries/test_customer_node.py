from django.test import TestCase
from graphene.test import Client
from graphql_relay.node.node import to_global_id

from core.schema import CustomerNode, schema
from core.tests.factories import CustomerFactory

client = Client(schema)


class TestCustomerNode(TestCase):
    def setUp(self):
        self.customer_1 = CustomerFactory(first_name="Peter", last_name="Parker")
        self.customer_2 = CustomerFactory(first_name="Bruce", last_name="Wayne")
        self.customer_3 = CustomerFactory(first_name="Damian", last_name="Wayne")
        self.customer_4 = CustomerFactory()
        self.customer_query = """
            query getCustomer($id: ID!){
                customer(id: $id){
                    id
                    firstName
                    lastName
                    email
                    phoneNumber
                }
            }
        """
        self.all_customers_query = """
            query getAllCustomers{
                allCustomers{
                    edges{
                        node{
                            id
                            firstName
                            lastName
                            email
                            phoneNumber
                        }
                    }
                }
            }
        """

        self.customer_by_last_name = """
            query getAllCustomers($lastName: String){
                allCustomers(lastName: $lastName){
                    edges{
                        node{
                            id
                            firstName
                            lastName
                            email
                            phoneNumber
                        }
                    }
                }
            }
        """

    def test_It_ReturnsCustomerById(self):
        result = client.execute(
            self.customer_query,
            variables={"id": to_global_id(CustomerNode, self.customer_1.id)},
        )
        data = result["data"]["customer"]

        self.assertEqual(self.customer_1.first_name, data["firstName"])
        self.assertEqual(self.customer_1.email, data["email"])

    def test_It_ReturnsAllCustomers(self):
        result = client.execute(self.all_customers_query)
        data = result["data"]["allCustomers"]["edges"]

        self.assertEqual(len(data), 4)
        with self.subTest("Assert each customer exists"):
            customers = [customer["node"]["email"] for customer in data]
            self.assertIn(self.customer_1.email, customers)
            self.assertIn(self.customer_2.email, customers)
            self.assertIn(self.customer_3.email, customers)
            self.assertIn(self.customer_4.email, customers)

    def test_It_ReturnsCustomersByLastName(self):
        result = client.execute(
            self.customer_by_last_name, variables={"lastName": "Wayne"}
        )
        data = result["data"]["allCustomers"]["edges"]

        self.assertEqual(len(data), 2)
