# Generated by Django 5.1.3 on 2024-12-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_aboutsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsection',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='about_backgrounds/'),
        ),
    ]