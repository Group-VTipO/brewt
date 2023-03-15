from django.urls import path
from . import views
from .views import handle_invalid_email
from .Errors.handlers import handle_not_found, handle_server_error

app_name = 'users'

urlpatterns = [
    path('', views.Brewtopia_view, name='brewtopia'),
    path('contact/', views.Contact_view, name='contact'),
    path('register/', views.register, name='register')
]

handler404 = handle_not_found
handler500 = handle_server_error
handler400 = handle_invalid_email

