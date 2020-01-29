from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from apps.organic_farmer.models import OrganicFarmer, OrganicFarmerAddress, OrganicFarmerContact, Entity, EntityType, Activity, Scope, CNPOFile

from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin


class OrganicFarmerResource(resources.ModelResource):

    name = fields.Field(
        attribute='name',
        column_name='NOME DO PRODUTOR',
        readonly=False,
    )

    cnpo_register = fields.Field(
        attribute='cnpo_register',
        column_name='CNPF/CNPJ/NIF',
        readonly=False,
    )

    class Meta:
        model = OrganicFarmer
        import_id_fields = ('cnpo_register',)
        exclude = ('created', 'modified',)
        fields = ('name', 'cnpo_register',)


class OrganicFarmerAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ['name', 'cnpo_register', 'address', 'entity']
    search_fields = ['name', 'cnpo_register', 'entity__entity_type', 'entity__name']
    list_filter = ['address__city', 'entity__entity_type', 'entity']

    resource_class = OrganicFarmerResource


class CNPOFileAdmin(admin.ModelAdmin):

    list_display = ['name', 'created', 'modified']


admin.site.register(OrganicFarmer, OrganicFarmerAdmin)
admin.site.register(OrganicFarmerAddress, LeafletGeoAdmin)
admin.site.register(Entity)
admin.site.register(EntityType)
admin.site.register(Activity)
admin.site.register(Scope)
admin.site.register(OrganicFarmerContact)
admin.site.register(CNPOFile, CNPOFileAdmin)
