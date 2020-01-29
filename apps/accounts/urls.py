# coding=utf-8

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.IndexView.as_view(template_name='accounts/index.html'), name='index'),
    path('registro/', views.RegisterView.as_view(template_name='accounts/register.html'), name='register'),
    path('alterar-dados', views.UpdateUserView.as_view(), name='update-user'),
    path('alterar-senha', views.UpdatePasswordView.as_view(), name='update-password'),
    path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
]
