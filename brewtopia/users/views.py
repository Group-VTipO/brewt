from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserProfileForm, LoginForm


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
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('users:home')
    else:
        form = UserProfileForm()
    return render(request, 'users/create_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:home')
            else:
                form = LoginForm()
                error_message = 'Invalid login'
    else:
        form = LoginForm()
        error_message = ''
    return render(request, 'users/login.html', {'form': form, 'error_message': error_message})

