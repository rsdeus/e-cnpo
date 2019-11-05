from django.contrib import admin

from apps.organic_fair.models import OrganicFair, OrganicFairAddress, OrganicFairContact
from leaflet.admin import LeafletGeoAdmin


class OrganicFairAdmin(admin.ModelAdmin):

    list_display = ['name', 'address', 'contact']
    search_fields = ['name', 'address__city']
    list_filter = ['address__city']


admin.site.register(OrganicFair, OrganicFairAdmin)
admin.site.register(OrganicFairAddress, LeafletGeoAdmin)
admin.site.register(OrganicFairContact)
