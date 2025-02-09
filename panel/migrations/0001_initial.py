# Generated by Django 5.0.6 on 2025-01-25 09:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(choices=[('oscuro', 'Modo Oscuro'), ('claro', 'Modo Claro')], default='oscuro', max_length=50)),
                ('idioma', models.CharField(choices=[('es', 'Español'), ('en', 'Inglés'), ('fr', 'Francés')], default='es', max_length=50)),
                ('notificaciones', models.BooleanField(default=True)),
                ('actualizaciones_automaticas', models.BooleanField(default=False)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='configuracion', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
