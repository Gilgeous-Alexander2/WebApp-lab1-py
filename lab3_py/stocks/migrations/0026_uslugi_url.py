# Generated by Django 5.0.4 on 2024-05-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0025_stock_change_date_alter_stock_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='uslugi',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Фото логотипа компании'),
        ),
    ]