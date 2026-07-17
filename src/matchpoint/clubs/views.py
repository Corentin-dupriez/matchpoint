from rest_framework.decorators import action
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from clubs.permissions import IsClubEmployeeOrAdmin
from users.serializers import UserListSerializer
from .models import Club
from .serializers import ClubSerializer
from courts.serializers import CourtSerializer
from common.serializers import ErrorSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List clubs", description="Returns a list of all the clubs in the app."
    ),
    retrieve=extend_schema(
        summary="Retrieve a club",
        description="Retrieve a specific club based on the PK provided in the path.",
    ),
    update=extend_schema(
        summary="Update a club",
        description="Update the details of a club. The action can only be performed by the staff of the club or by an admin.",
    ),
    partial_update=extend_schema(
        summary="Update a club",
        description="Update the details of a club. The action can only be performed by the staff of the club or by an admin.",
    ),
)
class ClubViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "employees"):
            return [IsAuthenticated(), IsClubEmployeeOrAdmin()]
        return []

    @extend_schema(
        summary="Retrieve the courts of a club",
        description="Retrieves all the courts of a specific club which PK is provided in the URL.",
    )
    @action(methods=["get"], detail=True, url_name="get-club-courts")
    def courts(self, request: Request, pk=None) -> Response:
        club = self.get_object()
        serializer = CourtSerializer(club.courts.all(), many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Retrieve the employees of a club",
        description="Retrieves the employees of a specific club which PK is provided in the URL. The endpoint is available to club employees and admins.",
        responses={201: UserListSerializer(many=True), 403: ErrorSerializer},
    )
    @action(
        methods=["get"],
        detail=True,
        permission_classes=[IsClubEmployeeOrAdmin, IsAdminUser],
    )
    def employees(self, request: Request, pk=None) -> Response:
        club: Club = self.get_object()
        serializer = UserListSerializer(club.employees.all(), many=True)
        return Response(serializer.data)
