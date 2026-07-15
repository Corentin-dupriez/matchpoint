from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import Reservation


class IsStaffOrReservationOwner(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: APIView, obj: Reservation
    ) -> bool:
        return request.user.is_staff or request.user == obj.user
