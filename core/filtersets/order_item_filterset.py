from core.models.order_item import OrderItem, CategoryType
from django_filters import FilterSet, ChoiceFilter


class OrderItemFilterSet(FilterSet):
    category = ChoiceFilter(choices=CategoryType.choices)

    class Meta:
        model = OrderItem
        fields = ["name", "category"]
