from django.shortcuts import render
from services.models import Service
from django.views import generic


# Create your views here.


class ServiceListView(generic.ListView):
    model = Service


class ServiceDetailView(generic.DetailView):
    model = Service

# def service_list(request):
#     service_list = Service.objects.filter()
#     return render(request, 'services/service_list.html', locals())
