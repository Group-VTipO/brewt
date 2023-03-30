from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login


def home_view(request):
    return render(request, 'users/home.html')


def contact_view(request):
    return render(request, 'users/Contact.html')


def handle_invalid_email(request, exception):
    return render(request, 'errors/invalid_email.html', {'error_message': str(exception)}, status=400)


def create_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # сохранение нового пользователя
            user = form.save(commit=False)
            # установка пароля
            user.set_password(form.cleaned_data['password'])
            user.save()
            # аутентификация и вход
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request, user)
            # перенаправление на главную страницу
            return redirect('users:home')
        else:
            print(form.errors)  # выведет ошибки в консоль

    else:
        form = UserProfileForm()

    return render(request, 'users/create_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = LoginForm()
            return render(request, 'create_user.html', {'form': form, 'error_message': 'Invalid login'})
    else:
        form = LoginForm()
        return render(request, 'create_user.html', {'form': form})
