from core.models import OrderAddress
from django_filters import FilterSet


class OrderAddressFilterSet(FilterSet):
    class Meta:
        model = OrderAddress
        fields = ["postal_code", "city"]
