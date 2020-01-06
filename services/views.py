from django.shortcuts import render
from services.models import Service
from django.views import generic


# Create your views here.


class ServiceListView(generic.ListView):
    model = Service


class ServiceDetailView(generic.DetailView):
    model = Service


from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


def send_email(request):
    result = send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, ['danya.sokolov98@gmail.com'])
    return result
