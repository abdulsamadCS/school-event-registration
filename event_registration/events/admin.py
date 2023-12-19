from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Event, Participant
from .resources import EventResource, ParticipantResource

# Register your models here.

class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource
    list_display = ('name', 'date_time', 'location', 'max_participants')
    search_fields = ('name', 'location')
    list_filter = ('date_time',)

class ParticipantAdmin(ImportExportModelAdmin):
    resource_class = ParticipantResource
    list_display = ('event', 'first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('event__name', 'first_name', 'last_name', 'email')
    list_filter = ('event__name',)

admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)