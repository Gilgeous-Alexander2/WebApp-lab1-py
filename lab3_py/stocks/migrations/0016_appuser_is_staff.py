# Generated by Django 5.0.4 on 2024-05-31 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0015_appuser_first_name_appuser_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Является ли пользователь менеджером?'),
        ),
    ]