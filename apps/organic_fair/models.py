from django.db import models

from apps.address.models import Address
from apps.contacts.models import Contact
from apps.organic_farmer.models import OrganicFarmer


class OrganicFairAddress(Address):
    pass


class OrganicFairContact(Contact):
    pass


class OrganicFair(models.Model):

    name = models.CharField('Nome da Feira', max_length=255, null=False)
    address = models.OneToOneField('organic_fair.OrganicFairAddress', on_delete='CASCADE', verbose_name='Endereço', null=True)
    contact = models.OneToOneField('organic_fair.OrganicFairContact', on_delete='CASCADE', verbose_name='Contatos', null=True)
    farmers = models.ManyToManyField('organic_farmer.OrganicFarmer', verbose_name='Produtores Orgânicos', blank=True)

    class Meta:
        verbose_name = 'Feira Orgânica'
        verbose_name_plural = 'Feiras Orgânicas'

    def __str__(self):
        return (self.name)
