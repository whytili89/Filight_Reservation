from rest_framework import serializers
from .models import Flight,Reservation

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__' 

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        field = '__all__'