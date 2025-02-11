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
        self.customer_3 = CustomerFactory()
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

    def test_It_Returns_CustomerById(self):
        result = client.execute(
            self.customer_query,
            variables={"id": to_global_id(CustomerNode, self.customer_1.id)},
        )
        data = result["data"]["customer"]
        print(data)
