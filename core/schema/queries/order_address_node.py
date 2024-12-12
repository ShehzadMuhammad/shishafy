from graphene_django import DjangoObjectType
from core.models import OrderAddress
from core.filtersets import OrderAddressFilterSet
from graphene import relay


class OrderAddressNode(DjangoObjectType):
    class Meta:
        model = OrderAddress
        filterset_class = OrderAddressFilterSet
        interfaces = (relay.Node,)
