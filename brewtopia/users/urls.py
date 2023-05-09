from django.urls import path
from . import views
from .Errors.handlers import handle_not_found, handle_server_error

app_name = 'users'

urlpatterns = [
    path('', views.home_view, name='user'),
]
