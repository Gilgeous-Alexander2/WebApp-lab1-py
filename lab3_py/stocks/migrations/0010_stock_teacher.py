# Generated by Django 5.0.4 on 2024-05-30 06:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0009_remove_stock_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='teacher_stocks', to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель'),
        ),
    ]