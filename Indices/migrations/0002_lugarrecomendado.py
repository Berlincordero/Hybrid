# Generated by Django 5.0.6 on 2025-02-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LugarRecomendado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, help_text='Precio promedio', max_digits=10)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='lugares/')),
                ('url', models.URLField(blank=True, help_text='Sitio web del lugar (opcional)', null=True)),
            ],
        ),
    ]
