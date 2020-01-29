from django.shortcuts import render
from lawyer.models import Lawyer
from django.contrib.auth.models import User
from django.views import generic


# Create your views here.

class LawyerListView(generic.ListView):
    model = Lawyer


class LawyerDetailView(generic.DetailView):
    model = Lawyer
