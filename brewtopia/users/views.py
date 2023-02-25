from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def Brewtopia_view(request):
    return render(request, 'Brewtopia.html')


def Contact_view(request) -> HttpResponse:
    template = loader.get_template('users/Brewtopia.html')
    context = {} # variables you use in your template go here- read the reference at the end for more info

    return HttpResponse(template.render(context, request))