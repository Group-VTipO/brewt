from django.shortcuts import render
from shop.models import Product


def home(request):
    products = Product.objects.all().filter(in_stock=True)

    context = {
        'products':products,
    }
    return render(request, 'users/home.html')