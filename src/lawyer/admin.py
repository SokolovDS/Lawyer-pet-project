from django.contrib.admin import site

# Register your models here.

from lawyer.models import Lawyer

# Register your models here.
site.register(Lawyer)