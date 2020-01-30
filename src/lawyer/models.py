from django.db.models import Model, CharField, EmailField, TextField, DecimalField
from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Lawyer(Model):
    """
    Юрист
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    rating = DecimalField(max_digits=10, decimal_places=2, default=0)
    photo = models.CharField(max_length=30, blank=True)

    def get_absolute_url(self):
        return reverse('lawyer_detail', args=[str(self.user_id)])


@receiver(post_save, sender=User)
def create_lawyer_profile(sender, instance, created, **kwargs):
    if created:
        Lawyer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_lawyer_profile(sender, instance, **kwargs):
    instance.lawyer.save()
