# Generated by Django 2.2.3 on 2020-12-08 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yt', '0002_canais_id_canal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canais',
            name='area',
        ),
        migrations.AddField(
            model_name='canais',
            name='nome_canal',
            field=models.CharField(default=None, max_length=100, verbose_name='nome do canal'),
        ),
    ]
