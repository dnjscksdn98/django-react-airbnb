from rest_framework import serializers
from django_countries.serializer_fields import CountryField

from rooms import models as room_models
from core.api import serializers as core_serializers
from users.api import serializers as user_serializers


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = room_models.Photo
        fields = (
            'id',
            'caption',
            'file'
        )


class RoomSerializer(serializers.ModelSerializer):
    country = CountryField()
    host = serializers.SerializerMethodField()
    room_type = core_serializers.StringSerializer()
    amenities = core_serializers.StringSerializer(many=True)
    facilities = core_serializers.StringSerializer(many=True)
    house_rules = core_serializers.StringSerializer(many=True)
    photos = serializers.SerializerMethodField()

    class Meta:
        model = room_models.Room
        fields = (
            'id',
            'name',
            'description',
            'country',
            'city',
            'price',
            'address',
            'guests',
            'beds',
            'bedrooms',
            'bathrooms',
            'check_in',
            'check_out',
            'host',
            'room_type',
            'amenities',
            'facilities',
            'house_rules',
            'photos',
        )

    def get_host(self, obj):
        return user_serializers.UserSerializer(obj.host).data

    def get_photos(self, obj):
        return PhotoSerializer(obj.photos.all(), many=True).data
