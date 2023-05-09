from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist

def _order_id(request):
    order = request.session.session_key
    if not order:
        order = request.session.create()
    return order

def add_order(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        order = Order.objects.get(order_id=_order_id(request))
    except Order.DoesNotExist:
        order=Order.objects.create(
        order_id = _order_id(request)
            )
        order.save()
    try:
        order_item = OrderItem.objects.get(product=product, order=order)
        order_item.quantity += 1
        order_item.save()
    except OrderItem.DoesNotExist:
        order_item = OrderItem.objects.create(
        product = product,
        quantity = 1,
        order = order,
         )
        order_item.save()
    return redirect('order')


def remove_order(request, product_id):
    order = Order.objects.get(order_id=_order_id(request))
    product = get_object_or_404(Product, id=product_id)
    order_item = OrderItem.objects.get(product=product, order=order)
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
    else:
        order_item.delete()
    return redirect('order')

def remove_order_item(request, product_id):
    order = Order.objects.get(order_id=_order_id(request))
    product = get_object_or_404(Product, id=product_id)
    order_item = OrderItem.objects.get(product=product, order=order)
    order_item.delete()
    return redirect('order')

def order(request,  total=0, quantity=0, order_items=None):
    try:
        tax = 0
        grand_total = 0
        order = Order.objects.get(order_id=_order_id(request))
        order_items = OrderItem.objects.filter(order=order, is_active=True)
        for order_item in order_items:
            total += (order_item.product.price*order_item.quantity)
            quantity += order_item.quantity
        tax = (2*total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total':total,
        'quantity':quantity,
        'order_items':order_items,
        'tax':tax,
        'grand_total':grand_total,
    }
    return render(request, 'shop/order.html', context)