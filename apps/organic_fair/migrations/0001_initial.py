# Generated by Django 2.2.2 on 2019-08-20 16:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
        ('organic_farmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganicFairAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(blank=True, max_length=255, verbose_name='Localidade')),
                ('street_number', models.CharField(blank=True, max_length=20, verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=255, verbose_name='Complemento')),
                ('neighborhood', models.CharField(blank=True, max_length=100, verbose_name='Bairro')),
                ('postal_code', models.CharField(blank=True, max_length=8, verbose_name='CEP')),
                ('city', models.CharField(blank=True, max_length=165, null=True, verbose_name='Cidade')),
                ('state', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=165, null=True, verbose_name='Estado')),
                ('country', models.CharField(blank=True, choices=[('BR', 'Brasil')], max_length=40, null=True, verbose_name='País')),
                ('geolocation', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
                'ordering': ['locality', 'street_number', 'neighborhood', 'city', 'state', 'country'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganicFairContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('site', models.CharField(blank=True, max_length=50, verbose_name='Site')),
                ('phone', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='contacts.Phone', verbose_name='Telefone')),
                ('social_network', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='contacts.SocialNetwork', verbose_name='Rede Social')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganicFair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome da Feira')),
                ('address', models.OneToOneField(null=True, on_delete='CASCADE', to='organic_fair.OrganicFairAddress', verbose_name='Endereço')),
                ('contact', models.OneToOneField(null=True, on_delete='CASCADE', to='organic_fair.OrganicFairContact', verbose_name='Contatos')),
                ('farmers', models.ManyToManyField(blank=True, to='organic_farmer.OrganicFarmer', verbose_name='Produtores Orgânicos')),
            ],
            options={
                'verbose_name': 'Feira Orgânica',
                'verbose_name_plural': 'Feiras Orgânicas',
            },
        ),
    ]
