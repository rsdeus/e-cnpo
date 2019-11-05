from django.views import generic
from watson import search as watson

from leaflet.admin import LeafletGeoAdmin

from apps.organic_farmer.models import OrganicFarmer
from apps.organic_farmer.forms import OrganicFarmerForm, OrganicFarmerAddressFormSet, OrganicFarmerContactFormSet

from django.forms import ModelForm, inlineformset_factory, modelformset_factory, formset_factory, TextInput

from django.db import transaction
from django.urls import reverse_lazy
from django.shortcuts import render #, request


class OrganicFarmerPageView(generic.ListView):

    model = OrganicFarmer
    var_list_or_map = ''
    kwargs = []

    def setup(args, kwargs):
        super().setup(kwargs)
        var_list_or_map = args
        return(var_list_or_map)

    def get_template_names(self, **kwargs):
        var_list_or_map = 'list'
        if var_list_or_map == 'list':
            self.template_name = 'organic_farmer/organic_farmer_page.html'
        else:
            self.template_name = 'organic_farmer/organic_farmer_map.html'

        return (self.template_name)

    def get_queryset(self):
        queryset = OrganicFarmer.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)

        return queryset

    def get_context_object_name(self, object_list):
        var_list_or_map = 'list'
        if var_list_or_map == 'list':
            self.context_object_name = 'organic_farmer_list'
        else:
            self.context_object_name = 'organic_farmer_map'

        return(self.context_object_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_or_map'] = 'list'

        return (context)


class OrganicFarmerListView(generic.ListView):

    model = OrganicFarmer
    template_name = 'organic_farmer/organic_farmer_list.html'
    context_object_name = 'organic_farmer_list'

    def get_queryset(self):
        queryset = OrganicFarmer.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)

        return queryset


'''
class OrganicFarmerCreate(generic.CreateView):
    #model = OrganicFarmer
    form_class = OrganicFarmerForm
    template_name = 'organic_farmer/organic_farmer.html'
    success_url = reverse_lazy('organic_farmer:organic_farmer_list')

    def get_context_data(self, **kwargs):
        data = super(OrganicFarmerCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['organic_farmer_address'] = OrganicFarmerAddressFormSet(self.request.POST)
            data['organic_farmer_contact'] = OrganicFarmerContactFormSet(self.request.POST)
        else:
            data['organic_farmer_address'] = OrganicFarmerAddressFormSet()
            data['organic_farmer_contact'] = OrganicFarmerContactFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        organic_farmer_address = context['organic_farmer_address']
        organic_farmer_contact = context['organic_farmer_contact']
        with transaction.atomic():
            self.object = form.save()
            if organic_farmer_address.is_valid():
                organic_farmer_address.instance = self.object
                organic_farmer_address.form.save()
            if organic_farmer_contact.is_valid():
                organic_farmer_contact.instance = self.object
                organic_farmer_contact.form.save()
        return super(OrganicFarmerCreate, self).form_valid(form)
'''


def OrganicFarmerCreate(request):
    OrganicFarmerFormSet = formset_factory(OrganicFarmerForm)
    if request.method == 'POST':
        formset = OrganicFarmerFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = OrganicFarmerFormSet()
    return render(request, 'organic_farmer/organic_farmer.html', {'formset': formset})


class OrganicFarmerUpdate(generic.UpdateView):
    model = OrganicFarmer
    form_class = OrganicFarmerForm
    template_name = 'organic_farmer/organic_farmer.html'
    success_url = reverse_lazy('organic_farmer:organic_farmer_list')

    def get_context_data(self, **kwargs):
        data = super(OrganicFarmerUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['organic_farmer_address'] = OrganicFarmerAddressFormSet(self.request.POST)
        else:
            data['organic_farmer_address'] = OrganicFarmerAddressFormSet()
        return data
