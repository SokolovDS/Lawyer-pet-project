from django.shortcuts import render

from .forms import SubscriberForm

# Create your views here.

from django.shortcuts import render
import time


def index(request):
    return render(request, 'main/index.html', locals())


def coming(request):
    name = "Daniil"
    currentDay = time.ctime(time.time())
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

    return render(request, 'main/coming.html', locals())
