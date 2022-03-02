from django.urls import path,include
from flight import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flight',views.FlightViewSet)

urlpatterns = [
    path('flightService/', include(router.urls)),
]