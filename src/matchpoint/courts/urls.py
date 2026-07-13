from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courts.views import CourtViewSet

router = DefaultRouter()
router.register(r"courts", CourtViewSet, "courts")

urlpatterns = [path("", include(router.urls))]
