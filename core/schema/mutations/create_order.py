import graphene
from django.core.exceptions import ValidationError
from graphene.relay import ClientIDMutation
from graphql import GraphQLError

from core.interactors import CreateOrderInteractor
from core.schema.queries import OrderNode


class CreateOrder(ClientIDMutation):
    class Input:
        items = graphene.List(graphene.ID, required=True)
        order_address_id = graphene.ID(required=True)
        customer_id = graphene.ID(required=True)
        expected_time_of_arrival = graphene.DateTime(required=True)
        customer_note = graphene.String()

    order = graphene.Field(OrderNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **inputs):
        try:
            order = CreateOrderInteractor(
                itmems=input.get("items"),
                order_address_id=input.get("order_address"),
                customer_id=input.get("customer"),
                expected_time_of_arrival=input.get("expected_time_of_arrival"),
                customer_note=inputs.get("customer_note"),
            ).run()

        except ValidationError as e:
            raise GraphQLError(f"Validation Error: {str(e)}")

        return cls(order=order)
