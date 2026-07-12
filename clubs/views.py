from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.exceptions import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Club
from .serializers import ClubSerializer
from courts.serializers import CourtSerializer


class GetClubView(generics.RetrieveAPIView):
    model = Club
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ClubViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def update(self, request, *args, **kwargs):
        user = request.user
        print(request.__dict__)
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

    @action(methods=["get"], detail=True)
    def courts(self, request, pk=None) -> Response:
        club = self.get_object()
        serializer = CourtSerializer(club.courts.all(), many=True)
        return Response(serializer.data)
