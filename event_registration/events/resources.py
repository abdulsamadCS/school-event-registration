from import_export import resources
from .models import Event, Participant

class EventResource(resources.ModelResource):
    class Meta:
        model = Event
        import_id_fields = ('name',)
        fields = ('name', 'date_time', 'location', 'description', 'max_participants')

class ParticipantResource(resources.ModelResource):
    class Meta:
        model = Participant
        import_id_fields = ('first_name', 'last_name', 'email')
        fields = ('event', 'first_name', 'last_name', 'profile_picture', 'email', 'phone_number')