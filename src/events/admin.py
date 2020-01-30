from django.contrib.admin import site, ModelAdmin

from events.models import Event, ServicesInEvent

# class SubscriberAdmin(ModelAdmin):
#     event_fields = [field.name for field in Event._meta.fields]
#     list_display = event_fields
#     search_fields = event_fields
#
#     class Meta:
#         model = Event


# Register your models here.
site.register(Event)
site.register(ServicesInEvent)
