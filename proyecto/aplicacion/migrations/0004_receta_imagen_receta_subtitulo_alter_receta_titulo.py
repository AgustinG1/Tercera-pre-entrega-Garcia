# Generated by Django 4.2.7 on 2023-11-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(default='images/receta_default.jpg', upload_to='recetas/'),
        ),
        migrations.AddField(
            model_name='receta',
            name='subtitulo',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='titulo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
