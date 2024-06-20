from django.contrib import admin
from salesapp.models import Customer, Product, Order
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)