from django.db.models import Model, CharField, EmailField, TextField, DecimalField, DO_NOTHING
from django.contrib.auth.models import User
from django.conf import settings

from django.db import models


# Create your models here.


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
