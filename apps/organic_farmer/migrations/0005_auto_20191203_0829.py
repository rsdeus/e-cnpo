# Generated by Django 2.2.6 on 2019-12-03 11:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organic_farmer', '0004_auto_20190825_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='organicfarmer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organicfarmer',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em'),
        ),
    ]