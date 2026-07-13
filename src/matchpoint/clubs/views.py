from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.exceptions import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from users.serializers import UserListSerializer, UserSerializer
from .models import Club
from .serializers import ClubSerializer
from courts.serializers import CourtSerializer


class ClubViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                data={
                    "status": "error",
                    "message": "You are not allowed to create a new club",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = request.user
        club = self.get_object()
        if user not in club.employees.all():
            return Response(
                data={
                    "status": "error",
                    "message": "You are not allowed to modify this resource",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        serializer = self.get_serializer(instance=club, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"status": "success", "message": "The resource was updated successfully"},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                data={
                    "status": "error",
                    "message": "You are not allowed to delete clubs",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return super().destroy(request, *args, **kwargs)

    @action(methods=["get"], detail=True)
    def employees(self, request, pk=None) -> Response:
        club = self.get_object()
        if request.user not in club.employees.all():
            return Response(
                {
                    "status": "error",
                    "message": "You are not allowed to view the details of this club",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        serializer = UserListSerializer(club.employees.all(), many=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    def courts(self, request, pk=None) -> Response:
        club = self.get_object()
        serializer = CourtSerializer(club.courts.all(), many=True)
        return Response(serializer.data)
