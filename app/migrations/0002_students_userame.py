# Generated by Django 5.2 on 2025-04-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='userame',
            field=models.CharField(blank=True, null=True, unique=True),
        ),
    ]
