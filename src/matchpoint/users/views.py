from rest_framework import viewsets
from rest_framework.exceptions import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer, UserListSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = UserListSerializer
        return super().list(request, *args, **kwargs)

    def update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response(
                data={
                    "status": "error",
                    "message": "You are not allowed to modify this user",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return super().update(request, pk)
