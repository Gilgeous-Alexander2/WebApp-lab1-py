# Generated by Django 5.0.4 on 2024-05-31 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0016_appuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Является ли пользователь администратором?'),
        ),
    ]
