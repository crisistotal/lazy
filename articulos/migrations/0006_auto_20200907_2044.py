# Generated by Django 3.1 on 2020-09-07 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0005_articulo_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='descripcion',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Descripcion'),
        ),
    ]
