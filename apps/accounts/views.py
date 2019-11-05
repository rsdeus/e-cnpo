# coding=utf-8

from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    pass


class RegisterView(CreateView):

    model = get_user_model()
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')
