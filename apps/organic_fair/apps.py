from django.apps import AppConfig
from watson import search as watson


class OrganicFairConfig(AppConfig):
    name = 'apps.organic_fair'
    verbose_name = 'Feiras Orgânicas'

    def ready(self):
        OrganicFair = self.get_model("OrganicFair")
        watson.register(OrganicFair, fields=("name", "address", "farmers"))
