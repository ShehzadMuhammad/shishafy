from graphene import relay, ObjectType, Schema
from graphene_django.filter import DjangoFilterConnectionField
from core.schema.queries import OrderItemNode, OrderAddressNode, OrderNode
from core.schema.queries.order_item_node import CategoryTypeEnum


class Query(ObjectType):
    order_item = relay.Node.Field(OrderItemNode)
    all_order_items = DjangoFilterConnectionField(OrderItemNode)
    order_address = relay.Node.Field(OrderAddressNode)
    all_order_addresses = DjangoFilterConnectionField(OrderAddressNode)
    order = relay.Node.Field(OrderNode)
    all_orders = DjangoFilterConnectionField(OrderNode)


schema = Schema(query=Query, types=[CategoryTypeEnum])
