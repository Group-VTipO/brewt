from django.contrib.auth.models import User
from django.db import models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # добавляем дополнительные поля профиля пользователя и не забудьте миграцию
    email = models.CharField('Почта', max_length=50)
    password = models.CharField('Пароль', max_length=50)
    password2 = models.CharField('Пароль', max_length=50)
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    phone_number = models.CharField('Номер Телефона', max_length=20)

