# Generated by Django 5.0.4 on 2024-05-30 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0012_alter_subject_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='teacher_subjects', to='stocks.subject', verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='uslugi',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название'),
        ),
    ]
