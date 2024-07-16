from rest_framework import serializers
from .models import Event,Venue

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )

    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )
    class Meta:
        model = Event
        fields = ('id','venue','artist','genre','Date','price','over18','ticket_limit','image_url','venue_id',)


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(
        many=True,
        read_only=True
    )
    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue_detail'
    )
    class Meta:
        model = Venue
        fields = ('id', 'name', 'location', 'capacity','parking','events','venue_url',)


