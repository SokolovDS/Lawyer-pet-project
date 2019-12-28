from django.db.models import Model, CharField, EmailField


# Create your models here.

class Subscriber(Model):
    """
    Clients
    -Name
    -Surname
    -patronymic
    -email
    -phone
    """
    name = CharField(max_length=64)
    surname = CharField(max_length=64, null=True)
    patronymic = CharField(max_length=64, null=True)
    email = EmailField()
    phone = CharField(max_length=64, null=True)

    def __str__(self):
        return "id: {}, email: {}".format(self.id, self.email)
