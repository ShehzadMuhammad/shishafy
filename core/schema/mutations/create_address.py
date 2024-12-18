import graphene
from graphene.relay import ClientIDMutation
from core.schema.queries import OrderAddressNode


class CreateAddress(ClientIDMutation):

    class Input:
        primary_street_address = graphene.String(required=True)
        secondary_street_address = graphene.String()
        postal_code = graphene.String(required=True)
        city = graphene.String(required=True)

    order_address = graphene.Field(OrderAddressNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **inputs):
        return "HELLO"
