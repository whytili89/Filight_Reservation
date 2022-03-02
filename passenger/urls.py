from django.urls import path,include
from passenger import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('passengers',views.PassengerViewSet)

urlpatterns = [
    path('flightService/', include(router.urls))
]