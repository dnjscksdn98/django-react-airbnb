from rest_framework import generics
from rest_framework import permissions
from rest_framework import status

from rooms import models as room_models
from . import serializers as room_serializers


class RoomView(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = room_serializers.RoomSerializer
    queryset = room_models.Room.objects.all()
