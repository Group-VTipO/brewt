from .models import UserProfile
from django import forms
from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from password_strength import PasswordPolicy


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'first_name', 'last_name', 'phone_number']

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
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError('Пожалуйста, введите действительный адрес электронной почты.')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        self.validate_phone_number(phone_number)
        return phone_number

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not re.match(r'^[A-Za-z]{1,30}$', first_name):
            raise forms.ValidationError('Неверный формат имени')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.match(r'^[A-Za-z]{1,30}$', last_name):
            raise forms.ValidationError('Неверный формат фамилии')
        return last_name

    @staticmethod
    def validate_phone_number(value):
        phone_regex = r''
        if not re.match(phone_regex, value):
            raise ValidationError('Неправильный номер телефона.')

    def clean_password(self):
        password = self.cleaned_data['password']
        policy = PasswordPolicy.from_names(
            length=25,
            numbers=1,
        )
        if policy.test(password):
            return password
        else:
            raise forms.ValidationError(
                "Password"
            )