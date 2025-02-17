# Generated by Django 5.0.6 on 2025-02-13 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fincas', '0003_alter_finca_tamaño'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_division', models.CharField(choices=[('casa', 'Casa o estructura'), ('cultivo', 'Terreno de cultivo'), ('potrero', 'Potrero'), ('estanque', 'Estanque o lago'), ('caminos', 'Caminos')], max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('tipo_terreno', models.CharField(choices=[('plano', 'Plano'), ('semiplano', 'Semiplano'), ('irregular', 'Irregular'), ('empinado', 'Empinado'), ('terraceo', 'Terraceo'), ('hundido', 'Hundido')], max_length=50)),
                ('tamaño', models.FloatField(help_text='Tamaño en metros cuadrados de la división')),
                ('ubicacion', models.CharField(choices=[('izquierdo', 'Lado izquierdo'), ('derecho', 'Lado derecho'), ('centro', 'En el centro'), ('a_lo_largo', 'A lo largo')], max_length=50)),
                ('cantidad_arboles', models.PositiveIntegerField(default=0)),
                ('rios', models.PositiveIntegerField(default=0)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='divisiones/')),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisiones', to='Fincas.finca')),
            ],
        ),
    ]
