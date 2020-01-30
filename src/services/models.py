from django.db.models import Model, CharField, EmailField, TextField, DecimalField
from django.urls import reverse


# Create your models here.

class Service(Model):
    """
    Услуга
    """
    name = CharField(max_length=64)
    description = TextField(blank=True, null=True, default=None)
    min_price = DecimalField(max_digits=10, decimal_places=2, default=0)

    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.id)])

    def __str__(self):
        return "Name: {}, Price: {}".format(self.name, self.min_price)
