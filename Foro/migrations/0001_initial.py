# Generated by Django 5.0.6 on 2025-01-19 10:48

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
            name='Foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido_texto', models.TextField(blank=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='foro/images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='foro/videos/')),
                ('post_type', models.CharField(choices=[('text', 'Texto'), ('image', 'Imagen'), ('video', 'Video')], default='text', max_length=10)),
                ('reposted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foros', to=settings.AUTH_USER_MODEL)),
                ('estrellas', models.ManyToManyField(blank=True, related_name='foros_estrellados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to=settings.AUTH_USER_MODEL)),
                ('foro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Foro.foro')),
            ],
        ),
    ]
