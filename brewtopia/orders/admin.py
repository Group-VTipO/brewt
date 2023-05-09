from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'date_added')
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'is_active')
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
