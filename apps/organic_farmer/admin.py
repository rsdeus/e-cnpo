from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from apps.organic_farmer.models import OrganicFarmer, OrganicFarmerAddress, OrganicFarmerContact, Entity, EntityType, Activity, Scope


class OrganicFarmerAdmin(admin.ModelAdmin):

    list_display = ['fantasy_name', 'address', 'entity']
    search_fields = ['fantasy_name', 'entity__name']
    list_filter = ['address__city', 'entity__entity_type', 'entity']


admin.site.register(OrganicFarmer, OrganicFarmerAdmin)
admin.site.register(OrganicFarmerAddress, LeafletGeoAdmin)
admin.site.register(Entity)
admin.site.register(EntityType)
admin.site.register(Activity)
admin.site.register(Scope)
admin.site.register(OrganicFarmerContact)
