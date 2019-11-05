from django.urls import path

from apps.organic_fair import views

app_name = 'organic_fair'

urlpatterns = [
    path('', views.OrganicFairListView.as_view(), name='organic_fair_list'),
]
