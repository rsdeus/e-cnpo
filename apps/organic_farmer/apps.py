from django.apps import AppConfig
from watson import search as watson


class OrganicFarmerConfig(AppConfig):
    name = 'apps.organic_farmer'
    verbose_name = 'Produtores Orgânicos'

    def ready(self):
        OrganicFarmer = self.get_model("OrganicFarmer")
        watson.register(OrganicFarmer, fields=("name", "cnpo_register", "address__city", "entity__name", "entity__entity_type__name", "scope__name", "activities__name"))
