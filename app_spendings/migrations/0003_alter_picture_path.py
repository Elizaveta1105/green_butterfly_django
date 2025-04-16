# Generated by Django 4.2.19 on 2025-03-09 16:12

import app_spendings.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_spendings', '0002_picture_user_alter_picture_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='path',
            field=models.ImageField(upload_to=app_spendings.models.upload_image, validators=[app_spendings.models.validate_file_size]),
        ),
    ]
