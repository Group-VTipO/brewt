from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserProfileForm, LoginForm


def home_view(request):
    return render(request, 'users/base.html')


