from django.contrib import admin

from apps.contacts.models import Phone, SocialNetwork

admin.site.register(Phone)
admin.site.register(SocialNetwork)
