import graphene
from graphene.relay import ClientIDMutation
from core.schema.queries import OrderNode


class CreateOrder(ClientIDMutation):
    class Input:
        items = graphene.List(graphene.ID, required=True)
        order_address = graphene.ID(required=True)
        expected_time_of_arrival = graphene.DateTime(required=True)
        customer_note = graphene.String()

    order = graphene.Field(OrderNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **inputs):
        return "HELLO"
