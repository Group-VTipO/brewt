from .models import UserProfile
from django.forms import ModelForm, TextInput


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'password2', 'first_name', 'last_name', 'phone_number']

        widgets = {
            "email": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Email',
                'type': 'text'
            }),
            "password": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Password',
                'type': 'password'
            }),
            "password2": TextInput(attrs={
                'class': 'form',
                'placeholder': 'rePassword',
                'type': 'password'
            }),

            "first_name": TextInput(attrs={
                'class': 'form',
                'placeholder': 'First Name',
                'type': 'text'
            }),
            "last_name": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Last Name',
                'type': 'text'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Phone Number',
                'type': 'text'
            }),

        }
