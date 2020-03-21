from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework import filters
from rest_framework import pagination

from rooms import models as room_models
from . import serializers as room_serializers


class RoomView(generics.ListAPIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = room_serializers.RoomSerializer
    pagination_class = pagination.PageNumberPagination
    queryset = room_models.Room.objects.all()

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'country',
                     'city', 'address', 'room_type__name']
    ordering_fields = ['-total_rating']
