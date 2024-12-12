from graphene_django import DjangoObjectType
from core.models import Order
from core.filtersets.order_filterset import OrderFilterSet
from graphene import relay


class OrderNode(DjangoObjectType):
    class Meta:
        model = Order
        filterset_class = OrderFilterSet
        interfaces = (relay.Node,)
