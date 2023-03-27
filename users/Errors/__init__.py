from django.shortcuts import render
from .handlers import handle_not_found, handle_server_error


def handle_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)

def handle_server_error(request):
    return render(request, 'errors/500.html', status=500)
