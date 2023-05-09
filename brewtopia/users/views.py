from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from orders.models import Order, OrderItem
from orders.views import _order_id

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = UserProfile.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request,'Registration succesful')
            return redirect('users:register')
    else:
        form = RegistrationForm()
    
    context = {
        'form':form,
    }
    return render(request, 'user_accounts/register.html', context)
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            try:
                order = Order.objects.get(order_id=_order_id(request))
                is_order_item_exists = OrderItem.objects.filter(order=order).exists()
                if is_order_item_exists:
                    order_item = OrderItem.objects.filter(order=order)
                    
                    for item in order_item:
                        item.user = user
                        item.save()

            except:
                pass
            auth.login(request, user)
            # messages.success(request, 'You are now logged in.')
            return redirect('users:dashboard')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')
    return render(request, 'user_accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,'You are logged out')
    return redirect('users:login')

@login_required(login_url = 'login')
def dashboard(request):
    return render(request, 'shop/shop.html')
