# Generated by Django 4.2.7 on 2023-11-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(choices=[('salada', 'Comida Salada'), ('dulce', 'Comida Dulce'), ('vegetariana', 'Comida Vegetariana')], default='salada', max_length=100),
        ),
    ]
