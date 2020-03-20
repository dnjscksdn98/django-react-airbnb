from rest_framework import serializers
from users import models as user_models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'id',
            'email',
            'username',
        )


class UserProfileSerializer(serializers.ModelSerializer):

    gender = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = user_models.User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'avatar',
            'bio',
            'gender',
            'birthdate',
            'language',
            'currency',
        )

    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_language(self, obj):
        return obj.get_language_display()

    def get_currency(self, obj):
        return obj.get_currency_display()
