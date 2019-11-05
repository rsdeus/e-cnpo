# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth import get_user_model

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
