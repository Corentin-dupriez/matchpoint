from django.urls import include, path
from .views import ClubViewSet, GetClubView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"clubs", ClubViewSet, "clubs")

urlpatterns = [path("", include(router.urls))]
