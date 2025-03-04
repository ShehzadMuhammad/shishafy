from django_filters import FilterSet

from core.models import Order


class OrderFilterSet(FilterSet):
    class Meta:
        model = Order
        fields = {
            "order_address__city": ["exact"],
            "order_address__postal_code": ["exact"],
            "customer__first_name": ["exact"],
            "customer__last_name": ["exact"],
            "customer__email": ["exact"],
            "total_cost": ["exact", "gt", "lt"],
            "items": ["exact", "contains"],
            "created_on": ["exact", "lt", "gt"],
        }
