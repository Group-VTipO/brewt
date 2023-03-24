from django.urls import path
from . import views
from .views import handle_invalid_email
from .Errors.handlers import handle_not_found, handle_server_error

app_name = 'users'

urlpatterns = [
    path('', views.brewtopia_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('create_user/', views.create_user, name='create_user')
]

handler404 = handle_not_found
handler500 = handle_server_error
handler400 = handle_invalid_email

