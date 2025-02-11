from graphene import relay
from graphene_django import DjangoObjectType

from core.filtersets import CustomerFilterSet
from core.models import Customer


class CustomerNode(DjangoObjectType):
    class Meta:
        model = Customer
        filterset_class = CustomerFilterSet
        interfaces = (relay.Node,)
