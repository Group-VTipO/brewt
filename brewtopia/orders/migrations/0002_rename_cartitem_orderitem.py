# Generated by Django 4.1.7 on 2023-05-09 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItem',
            new_name='OrderItem',
        ),
    ]
