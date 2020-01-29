from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from apps.organic_map import views
from djgeojson.views import GeoJSONLayerView
from apps.organic_farmer.models import OrganicFarmer, OrganicFarmerAddress

app_name = 'organic_map'

urlpatterns = [
    path('', views.OrganicMap.as_view(), name='organic_map'),
    path('data.geojson', GeoJSONLayerView.as_view(model=OrganicFarmerAddress, geometry_field='geolocation', properties=('city',)), name='data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
