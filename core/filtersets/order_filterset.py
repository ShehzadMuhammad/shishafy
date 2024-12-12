from core.models import Order
from django_filters import FilterSet


class OrderFilterSet(FilterSet):
    class Meta:
        model = Order
        fields = {
            "order_address__city": ["exact"],
            "order_address__postal_code": ["exact"],
            "total_cost": ["exact", "gt", "lt"],
            "items": ["exact", "contains"],
            "created_on": ["exact", "lt", "gt"],
        }
