from django.db import models


class Phone(models.Model):
    phone = models.CharField('Telefone', max_length=12, blank=True)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return self.phone


class SocialNetwork(models.Model):

    SOCIAL_NETWORKS = [
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Twitter', 'Twitter'),
    ]

    name = models.CharField('Nome da Rede Social', choices=SOCIAL_NETWORKS, max_length=30)
    link = models.CharField('Link da Rede Social', max_length=50, null=True)

    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'

    def __str__(self):
        return (self.name + ': ' + self.link)


class Contact(models.Model):
    email = models.EmailField('E-mail', blank=True)
    site = models.CharField('Site', max_length=50, blank=True)
    phone = models.ManyToManyField('contacts.Phone', blank=True, verbose_name='Telefone')
    social_network = models.ManyToManyField('contacts.SocialNetwork', blank=True, verbose_name='Rede Social')

    class Meta:
        abstract = True
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        full_contact = ''
        email = self.email
        site = self.site
        phone = self.phone
        social_network = self.social_network

        if email:
            full_contact = '%s' % email
        if site:
            full_contact += ', %s' % site
        if phone:
            full_contact += ', %s' % phone
        if social_network:
            full_contact += ', %s' % social_network

        return (full_contact)
