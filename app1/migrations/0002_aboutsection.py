# Generated by Django 5.1.3 on 2024-12-07 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_heading', models.CharField(max_length=50)),
                ('about_description1', models.TextField()),
                ('about_description2', models.TextField()),
            ],
        ),
    ]