from django.shortcuts import render, redirect
from .forms import UserProfileForm



def brewtopia_view(request):
    return render(request, 'users/Brewtopia.html')


def contact_view(request):
    return render(request, 'users/Contact.html')


def handle_invalid_email(request, exception):
    return render(request, 'errors/invalid_email.html', {'error_message': str(exception)}, status=400)


def create_user(request):
    error = ''

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('users:home')
    else:
        form = UserProfileForm()

    data = {
        'form': form
    }

    return render(request, 'users/create_user.html', data)