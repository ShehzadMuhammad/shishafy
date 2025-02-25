import graphene
from django.core.exceptions import ValidationError
from graphene.relay import ClientIDMutation
from graphql import GraphQLError

from core.interactors import CreateCustomerInteractor
from core.schema.queries import CustomerNode


class CreateCustomer(ClientIDMutation):

    class Input:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone_number = graphene.String(required=True)

    customer = graphene.Field(CustomerNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        try:
            customer = CreateCustomerInteractor(
                first_name=input.get("first_name"),
                last_name=input.get("last_name"),
                email=input.get("email"),
                phone_number=input.get("phone_number"),
            ).run()

        except ValidationError as e:
            raise GraphQLError(f"Validation Error: {str(e)}")

        return cls(customer)
