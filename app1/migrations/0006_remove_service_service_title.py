# Generated by Django 5.1.3 on 2024-12-07 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_service_service_button_service_service_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_title',
        ),
    ]
