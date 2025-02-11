from django_filters import FilterSet

from core.models import Customer


class CustomerFilterSet(FilterSet):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "phone_number", "email"]
