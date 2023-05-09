from django.db import models
from shop.models import Product

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_id
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.price*self.quantity

    def __unicode__(self):
        return self.product