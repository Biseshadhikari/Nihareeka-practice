# Generated by Django 5.2 on 2025-04-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
