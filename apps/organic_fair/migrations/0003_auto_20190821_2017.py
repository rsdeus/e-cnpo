# Generated by Django 2.2.2 on 2019-08-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organic_fair', '0002_auto_20190820_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organicfaircontact',
            name='phone',
            field=models.ManyToManyField(blank=True, to='contacts.Phone', verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='organicfaircontact',
            name='social_network',
            field=models.ManyToManyField(blank=True, to='contacts.SocialNetwork', verbose_name='Rede Social'),
        ),
    ]
