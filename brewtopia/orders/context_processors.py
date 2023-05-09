from .models import Order, OrderItem
from .views import _order_id
def counter(request):
    order_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            order = Order.objects.filter(order_id=_order_id(request))
            order_items = OrderItem.objects.all().filter(order=order[:1]) 
            for order_item in order_items:
                order_count += order_item.quantity
        except Order.DoesNotExist:
            order_count = 0
    return dict(order_count=order_count)

