# Generated by Django 4.2.7 on 2023-11-26 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion', '0011_alter_message_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='usuario_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_as_user_1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='usuario_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_as_user_2', to=settings.AUTH_USER_MODEL),
        ),
    ]
