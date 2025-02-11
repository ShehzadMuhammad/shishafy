from graphene import ObjectType, Schema, relay
from graphene_django.filter import DjangoFilterConnectionField

from core.schema.mutations import CreateOrderAddress
from core.schema.queries import OrderAddressNode, OrderItemNode, OrderNode, CustomerNode
from core.schema.queries.order_item_node import CategoryTypeEnum


class Query(ObjectType):
    order_item = relay.Node.Field(OrderItemNode)
    all_order_items = DjangoFilterConnectionField(OrderItemNode)
    order_address = relay.Node.Field(OrderAddressNode)
    all_order_addresses = DjangoFilterConnectionField(OrderAddressNode)
    order = relay.Node.Field(OrderNode)
    all_orders = DjangoFilterConnectionField(OrderNode)
    customer = relay.Node.Field(CustomerNode)
    all_customers = DjangoFilterConnectionField(CustomerNode)


class Mutation(ObjectType):
    create_order_address = CreateOrderAddress.Field()


schema = Schema(query=Query, mutation=Mutation, types=[CategoryTypeEnum])
