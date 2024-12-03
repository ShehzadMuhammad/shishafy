from graphene import relay, ObjectType, Schema
from graphene_django.filter import DjangoFilterConnectionField
from core.schema.queries import OrderItemNode


class Query(ObjectType):
    order_item = relay.Node.Field(OrderItemNode)
    all_order_items = DjangoFilterConnectionField(OrderItemNode)


schema = Schema(query=Query)
