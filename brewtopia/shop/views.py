from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from orders.models import Order, OrderItem
from orders.views import _order_id

def shop(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category=categories, in_stock=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(in_stock=True).order_by('id')
        product_count = products.count() 

    context = {
        'products':products,
        'product_count':product_count,
    }
    return render(request, 'shop/shop.html', context)

def product_info(request, category_slug, product_slug):
    try:
        one_product = Product.objects.get(category__slug=category_slug, slug = product_slug)
        in_order = OrderItem.objects.filter(order__order_id=_order_id(request), product = one_product).exists()
    except Exception as e:
        raise e
    
    context = {
        'one_product':one_product,
        'in_order':in_order,
    }

    return render(request, 'shop/product_info.html', context)

