# Generated by Django 5.0.4 on 2024-05-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0024_remove_uslugi_stocks_stock_uslugi_alter_stock_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='change_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]