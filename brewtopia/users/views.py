from django.shortcuts import render, redirect
from .Errors.exceptions import InvalidEmailException
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import UserProfileForm
from .models import UserProfile

def Brewtopia_view(request):
    return render(request, 'users/Brewtopia.html')


def Contact_view(request):
    return render(request, 'users/Contact.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if '@' not in email or '.' not in email:
            raise InvalidEmailException()
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = email
            user.save()
            login(request, user)
            return redirect('brewtopia')
    else:
        form = UserProfileForm()
    return render(request, 'users/register.html', {'form': form})

def handle_invalid_email(request, exception):
    return render(request, 'errors/invalid_email.html', {'error_message': str(exception)}, status=400)


def create(request):
    form = UserProfileForm()

    data = {
        'form': form
    }

    return render(request, 'users/register.html', data)