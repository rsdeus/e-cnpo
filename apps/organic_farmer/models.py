from django.db import models
#from django.contrib.auth.models import User

from apps.address.models import Address
from apps.contacts.models import Contact


class OrganicFarmerAddress(Address):
    pass


class OrganicFarmerContact(Contact):
    pass


class EntityType(models.Model):

    ENTITY_TYPE = [
        ('CERTIFICADORA', 'Certificadora'),
        ('OPAC', 'Organismo Participativo de Avaliação da Conformidade'),
        ('OCS', 'Organizações de Controle Social'),
    ]

    name = models.CharField('Tipo de Entidade', choices=ENTITY_TYPE, max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Tipo de Entidade'
        verbose_name_plural = 'Tipos de Entidade'

    def __str__(self):
        return self.name


class Entity(models.Model):
    name = models.CharField('Entidade', max_length=255, blank=True, unique=True)
    entity_type = models.ForeignKey('EntityType', on_delete='CASCADE', null=True, verbose_name='Tipo de Entidade')

    class Meta:
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return self.name


class Scope(models.Model):
    name = models.CharField('Escopo', max_length=255, blank=True, unique=True)

    class Meta:
        verbose_name = 'Escopo'
        verbose_name_plural = 'Escopos'

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField('Atividade', max_length=255, blank=True, unique=True)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.name


class OrganicFarmer(models.Model):
    
    cnpo_register = models.CharField('Registro CNPO', max_length=255, db_index=True)
    name = models.CharField('Nome de Registro', max_length=255, null=False)
    date_registered = models.DateTimeField('Data de Registro', auto_now_add=True)
    cnpo_situation = models.BooleanField(default=True)
    address = models.ForeignKey('OrganicFarmerAddress', on_delete=models.CASCADE, related_name='endereco', verbose_name='Endereço', null=True)
    entity = models.ForeignKey('Entity', on_delete='CASCADE', verbose_name='Entidade', null=True)
    scope = models.ManyToManyField('Scope', verbose_name='Escopo')
    activities = models.ManyToManyField('Activity', verbose_name='Atividades')
    contact = models.ForeignKey('OrganicFarmerContact', on_delete='CASCADE', verbose_name='Contatos', null=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produtor Orgânico'
        verbose_name_plural = 'Produtores Orgânicos'
        
    def __str__(self):
        return (self.name)


class CNPOFile(models.Model):

    name = models.CharField('Nome do Arquivo', max_length=255, db_index=True)
    cnpo_file = models.FileField('Arquivo CNPO', upload_to='cnpo_files')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Arquivo CNPO'
        verbose_name_plural = 'Arquivos CNPO'
        
    def __str__(self):
        return(self.name)
