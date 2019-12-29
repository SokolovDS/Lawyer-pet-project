from django.shortcuts import render
from services.models import Service


# Create your views here.

def service_list(request):
    service_list = Service.objects.filter()
    return render(request, 'services/service_list.html', locals())
