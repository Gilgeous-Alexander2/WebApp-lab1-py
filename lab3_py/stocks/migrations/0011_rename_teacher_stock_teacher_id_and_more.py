# Generated by Django 5.0.4 on 2024-05-07 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0010_remove_authuser_role_remove_authuser_username_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='teacher',
            new_name='teacher_id',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='teacherid',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='last_login',
        ),
    ]