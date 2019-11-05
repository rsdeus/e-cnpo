from django.views import generic
from watson import search as watson

from apps.organic_fair.models import OrganicFair


class OrganicFairListView(generic.ListView):

    model = OrganicFair
    template_name = 'organic_fair/organic_fair_list.html'
    context_object_name = 'organic_fair_list'

    def get_queryset(self):
        queryset = OrganicFair.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)

        return queryset
