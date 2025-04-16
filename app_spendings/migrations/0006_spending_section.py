# Generated by Django 4.2.19 on 2025-03-14 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_sections', '0003_section_user'),
        ('app_spendings', '0005_alter_spending_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='spending',
            name='section',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_sections.section'),
        ),
    ]
