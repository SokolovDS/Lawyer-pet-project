from django.contrib.admin import site, ModelAdmin

from services.models import Service


class SubscriberAdmin(ModelAdmin):
    service_fields = [field.name for field in Service._meta.fields]
    list_display = service_fields
    search_fields = service_fields

    class Meta:
        model = Service


# Register your models here.
site.register(Service, SubscriberAdmin)
