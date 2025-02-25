from django.test import TestCase
from graphene.test import Client

from core.models import Customer
from core.schema import schema
from core.tests.factories import CustomerFactory

client = Client(schema)


class TestCreateCustomer(TestCase):
    def setUp(self):
        self.customer = CustomerFactory(
            phone_number="4166665555", email="robin@batmanin.com"
        )
        self.create_customer_mutation = """
        mutation createCustomer($input: CreateCustomerInput!) {
            createCustomer(input: $input) {
             customer{
                id
             }
            }
        }
    """

    def test_It_CreatesnewCustomer(self):
        variables = {
            "input": {
                "firstName": "Bruce",
                "lastName": "Wayne",
                "email": "batman@batmaninc.com",
                "phoneNumber": "4155555555",
            }
        }
        response = client.execute(self.create_customer_mutation, variables=variables)

        self.assertNotIn("errors", response)

        customer = Customer.objects.filter(first_name="Bruce").first()

        with self.subTest("Newly Create Customer has right values"):
            self.assertEqual("Wayne", customer.last_name)
            self.assertEqual("batman@batmaninc.com", customer.email)
            self.assertEqual("4155555555", customer.phone_number)

    def test_It_RaisesError_WhenUsingPhoneNumberAlreadyInUse(self):
        variables = {
            "input": {
                "firstName": "Bruce",
                "lastName": "Wayne",
                "email": "batman@batmaninc.com",
                "phoneNumber": "4166665555",
            }
        }
        response = client.execute(self.create_customer_mutation, variables=variables)

        self.assertIn("errors", response)

        error_message = response["errors"][0]["message"]
        self.assertIn("Validation Error", error_message)

    def test_It_RaisesError_WhenUsingEmailAlreadyInUse(self):
        variables = {
            "input": {
                "firstName": "Bruce",
                "lastName": "Wayne",
                "email": "robin@batmaninc.com",
                "phoneNumber": "4166665555",
            }
        }
        response = client.execute(self.create_customer_mutation, variables=variables)

        self.assertIn("errors", response)

        error_message = response["errors"][0]["message"]
        self.assertIn("Validation Error", error_message)
