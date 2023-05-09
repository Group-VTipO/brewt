from django.urls import path
from . import views
urlpatterns = [
    path('', views.order, name='order'),
    path('add_order/<int:product_id>/', views.add_order, name='add_order'),
    path('remove_order/<int:product_id>/', views.remove_order, name='remove_order'),
    path('remove_order_item/<int:product_id>/', views.remove_order_item, name='remove_order_item'),
]