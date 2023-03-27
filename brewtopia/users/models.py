import uuid
from django.db import models
from django.contrib.auth.hashers import make_password


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # добавляем дополнительные поля профиля пользователя и не забудьте миграцию
    email = models.EmailField(default='')
    password = models.CharField('Password', max_length=50, default='',
                                error_messages={'required': 'Email is required', 'invalid': 'Invalid email format'})
    first_name = models.CharField('Name', max_length=30, default='')
    last_name = models.CharField('Last Name', max_length=30, default='')
    phone_number = models.CharField('Number', max_length=20, default='')

    def __str__(self):
        return str(self.pk)

    def set_password(self, password):
        self.password = make_password(password)
