from graphene_django import DjangoObjectType
from core.models.order_item import OrderItem, CategoryType
from core.filtersets import OrderItemFilterSet
from graphene import Enum, relay


class CategoryTypeEnum(Enum):
    FLAVOUR = CategoryType.FLAVOUR
    EXTRA = CategoryType.EXTRA


class OrderItemNode(DjangoObjectType):
    class Meta:
        model = OrderItem
        filterset_class = OrderItemFilterSet
        interfaces = (relay.Node,)
