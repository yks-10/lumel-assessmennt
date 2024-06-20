import uuid

from django.db import models
from salesdata.constants import CATEGORY, PAYMENT_TYPE
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(blank=False, null=False)
    address = models.TextField(max_length=200, blank=True, null=False)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-pk']

        def __str__(self):
            return str(self.name)

class Product(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    product_name = models.CharField(max_length=25, null=False, blank=False)
    categories = models.CharField(max_length=20, choices=CATEGORY, default="OTHERS")
    sale_date = models.DateTimeField()
    unit_price = models.FloatField(max_length=8)
    discount = models.IntegerField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-pk']

        def __str__(self):
            return str(self.product_name)


class Order(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shipment_cost = models.IntegerField()
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE, default="CASH")
    quantity_sold = models.IntegerField()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-pk']

        def __str__(self):
            return str(self.id, self.product.product_name)




