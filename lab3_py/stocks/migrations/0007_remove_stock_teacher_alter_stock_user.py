# Generated by Django 5.0.4 on 2024-05-30 06:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_alter_appuser_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='stock',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Создатель заявки'),
        ),
    ]
