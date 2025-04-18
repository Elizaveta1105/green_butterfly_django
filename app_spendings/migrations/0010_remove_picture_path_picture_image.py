# Generated by Django 4.2.19 on 2025-03-20 16:44

import cloudinary.models
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_spendings', '0009_alter_picture_spending_alter_picture_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='path',
        ),
        migrations.AddField(
            model_name='picture',
            name='image',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
