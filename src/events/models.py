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

    def __str__(self):
        return "Id клиента: {}, Id юриста: {}".format(self.client_id, self.person_id)


class ServicesInEvent(Model):
    """
    Услуги в обращении
    """
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
