from django.forms import ValidationError
from rest_framework import serializers
from .models import Flight,Reservation
import re

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__' 

    def validate_flightNumber(self,flightNumber):
        if(re.match('^[a-zA-Z0-9]*$',flightNumber) == None):
            raise serializers.ValidationError("Invalid Flight Number. Make Sure it is alpha numberic")
        return flightNumber

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'