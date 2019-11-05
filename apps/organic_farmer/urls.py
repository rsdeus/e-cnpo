from django.shortcuts import render
from django.urls import path

from apps.organic_farmer import views

app_name = 'organic_farmer'

urlpatterns = [
    path('', views.OrganicFarmerListView.as_view(), name='organic_farmer_list'),
    # path('cadastrar/', views.OrganicFarmerCreate.as_view(), name='organic_farmer_create'),
    # path('atualizar/<int:pk>/', views.OrganicFarmerUpdate.as_view(), name='organic_farmer_update')
]
