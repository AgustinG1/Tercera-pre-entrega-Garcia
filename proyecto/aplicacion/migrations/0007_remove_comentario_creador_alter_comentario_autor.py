# Generated by Django 4.2.7 on 2023-11-23 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion', '0006_comentario_creador_receta_creador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='creador',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
