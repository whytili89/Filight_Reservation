from django.db import models
from passenger.models import Passenger

# Create your models here.

class Flight(models.Model):
    flightNumber = models.CharField(max_length=20)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDepature = models.TimeField()

    class Meta:
        db_table = 'flight'

class Reservation(models.Model):
    flight = models.ForeignKey(Flight,related_name='flight',on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger,related_name='passenger',on_delete=models.CASCADE) 

    class Meta:
        db_table = 'reservation'