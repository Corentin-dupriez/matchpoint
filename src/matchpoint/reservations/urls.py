from django.urls import include, path
from .views import ReservationViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"reservations", ReservationViewset)

urlpatterns = [path("", include(router.urls))]
