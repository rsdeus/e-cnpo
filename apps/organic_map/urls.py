from django.urls import path

from apps.organic_map import views

app_name = 'organic_map'

urlpatterns = [
    path('', views.OrganicMap.as_view(), name='organic_map'),
]
