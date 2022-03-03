from django.urls import path,include
from flight import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flight',views.FlightViewSet),
router.register('reservation',views.ReservationViewSet),

urlpatterns = [
    path('flightService/',include(router.urls)),
    path('flightService/findFlights/',views.find_flights),
    path('flightService/saveReservation/',views.save_reservation)
]