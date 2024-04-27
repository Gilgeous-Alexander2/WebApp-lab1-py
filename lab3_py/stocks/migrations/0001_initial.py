# Generated by Django 5.0.4 on 2024-04-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('second_name', models.CharField(blank=True, max_length=255, null=True)),
                ('degree1', models.CharField(blank=True, null=True)),
                ('degree2', models.CharField(blank=True, null=True)),
                ('urls', models.CharField(blank=True, null=True)),
            ],
        ),
    ]