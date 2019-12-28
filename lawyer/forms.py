from django.forms import ModelForm
from lawyer.models import Subscriber


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ["name", "email"]
