# Generated by Django 5.0.6 on 2025-01-25 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Perfiles', '0005_perfil_background_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='background_image',
        ),
    ]
