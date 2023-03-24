from .models import UserProfile
from django import forms
from django.forms import ModelForm, TextInput
from django.core.validators import RegexValidator, EmailValidator


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

    def clean_email(self):
        email = self.cleaned_data['email']
        if not EmailValidator()(email):
            raise forms.ValidationError('Please enter a valid email address.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if len(password) < 8:
            raise forms.ValidationError('Password should be at least 8 characters long.')

        if password != password2:
            raise forms.ValidationError("Passwords don't match.")

        return password

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError('First name should contain only letters.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError('Last name should contain only letters.')
        return last_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not RegexValidator(r'^\?\d{10,12}$', message='Please enter a valid phone number.')(phone_number):
            raise forms.ValidationError('Please enter a valid phone number.')
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        if 'password' in cleaned_data and 'password2' in cleaned_data:
            if cleaned_data['password'] != cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match.")
        return cleaned_data