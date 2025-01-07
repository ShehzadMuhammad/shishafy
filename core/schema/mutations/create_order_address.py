import graphene
from graphene.relay import ClientIDMutation
from core.schema.queries import OrderAddressNode
from core.interactors import CreateOrderAddressInteractor
from django.core.exceptions import ValidationError
from graphql import GraphQLError


class CreateOrderAddress(ClientIDMutation):

    class Input:
        primary_street_address = graphene.String(required=True)
        secondary_street_address = graphene.String()
        postal_code = graphene.String(required=True)
        city = graphene.String(required=True)

    order_address = graphene.Field(OrderAddressNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        try:
            order_address = CreateOrderAddressInteractor(
                primary_street_address=input.get("primary_street_address"),
                secondary_street_address=input.get("secondary_street_address"),
                postal_code=input.get("postal_code"),
                city=input.get("city"),
            ).run()

        except ValidationError as e:
            raise GraphQLError(f"Validation Error: {str(e)}")

        return cls(order_address=order_address)
