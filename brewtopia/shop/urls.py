from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('category/<slug:category_slug>/', views.shop, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_info, name='product_info'),
    path('search/', views.search, name='search'),
] 