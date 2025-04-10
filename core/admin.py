from django.contrib import admin

# Register your models here.
from .models import Customer, Order, OrderAddress, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderAddress)
admin.site.register(Customer)
