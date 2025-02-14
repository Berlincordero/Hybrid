# Generated by Django 5.0.6 on 2025-02-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_categoria', models.CharField(choices=[('productos', 'Productos'), ('insumos', 'Insumos'), ('animales', 'Animales')], help_text='Seleccione la categoría principal.', max_length=20)),
                ('sub_categoria', models.CharField(blank=True, choices=[('carnes', 'Carnes'), ('granos', 'Granos'), ('vegetales', 'Vegetales'), ('frutas', 'Frutas'), ('lacteos', 'Lácteos')], help_text='Solo para Productos: seleccione una subcategoría.', max_length=20, null=True)),
                ('fecha', models.DateField(help_text='Fecha del índice')),
                ('porcentaje', models.DecimalField(decimal_places=2, help_text='Porcentaje (por ejemplo, 13.00)', max_digits=5)),
                ('antes', models.IntegerField(help_text="Valor 'Antes' (por ejemplo, 56)")),
                ('sube', models.IntegerField(help_text="Valor 'Sube' (por ejemplo, 24)")),
                ('total', models.IntegerField(help_text="Valor 'Total' (por ejemplo, 80)")),
                ('precio_actual', models.DecimalField(decimal_places=2, help_text='Precio actual (por ejemplo, 100.00)', max_digits=10)),
                ('inflacion', models.DecimalField(decimal_places=2, help_text='Inflación (por ejemplo, 33.00)', max_digits=5)),
                ('image', models.ImageField(blank=True, help_text='Imagen representativa (opcional)', null=True, upload_to='indices/')),
            ],
        ),
    ]
