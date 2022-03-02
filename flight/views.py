from rest_framework import viewsets
from .serializers import FlightSerializer,ReservationSerializer
from .models import Flight,Reservation

# Create your views here.

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer      