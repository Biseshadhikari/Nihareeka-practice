# Generated by Django 5.2 on 2025-04-23 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_userame_students_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='username',
        ),
    ]
