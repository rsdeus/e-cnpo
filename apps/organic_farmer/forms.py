# coding=utf-8

from django.forms import ModelForm, inlineformset_factory, modelformset_factory, formset_factory, TextInput
from apps.organic_farmer.models import OrganicFarmer, OrganicFarmerAddress, OrganicFarmerContact, Entity
from apps.address.models import Address
from location_field.forms.plain import PlainLocationField


class OrganicFarmerForm(ModelForm):
    class Meta:
        model = OrganicFarmer
        exclude = ['address', 'contact', 'entity']


class OrganicFarmerAddressForm(ModelForm):
    class Meta:
        model = OrganicFarmerAddress
        fields = '__all__'


class OrganicFarmerContactForm(ModelForm):
    class Meta:
        model = OrganicFarmerContact
        fields = '__all__'


class EntityForm(ModelForm):
    class Meta:
        model = Entity
        fields = '__all__'


OrganicFarmerAddressFormSet = formset_factory(OrganicFarmerAddressForm)

OrganicFarmerContactFormSet = formset_factory(OrganicFarmerContactForm)

EntityFormSet = formset_factory(EntityForm)
