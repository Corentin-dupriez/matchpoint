from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView
from typing import Any


class IsClubEmployeeOrAdmin(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        return (
            obj.employees.filter(pk=request.user.pk).exists() or request.user.is_staff
        )
