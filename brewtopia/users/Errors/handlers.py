from django.http import HttpResponseNotFound, HttpResponseServerError

def handle_not_found(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404: Страница не найдена и не думаю перейти в Starbucks</h1>'),

def handle_server_error(request):
    return HttpResponseServerError('<h1>Ошибка 500: Внутренняя ошибка сервера</h1>')

