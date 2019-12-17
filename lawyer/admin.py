from django.contrib.admin import site, ModelAdmin

from lawyer.models import Subscriber


class SubscriberAdmin(ModelAdmin):
    subscribers_fields = [field.name for field in Subscriber._meta.fields]
    list_display = subscribers_fields
    search_fields = subscribers_fields

    class Meta:
        model = Subscriber


# Register your models here.
site.register(Subscriber, SubscriberAdmin)
