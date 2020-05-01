from django.db.models import Model, CharField, EmailField, TextField, DecimalField, DO_NOTHING
from django.contrib.auth.models import User
from django.conf import settings

from django.db import models

from services.models import Service


# Create your models here.

class Event(Model):
    """
    Обращение
    """
    client_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='client_id'
    )
    person_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='person_id'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Заказ {}. Id клиента: {}, Id юриста: {}".format(self.id, self.client_id, self.person_id)


class ServicesInEvent(Model):
    """
    Услуги в обращении
    """
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
