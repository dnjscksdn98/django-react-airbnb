from rest_framework import serializers
from users import models as user_models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = [
            'id',
            'email',
            'username',
        ]


class UserProfileSerializer(serializers.ModelSerializer):

    gender = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = user_models.User
        fields = [
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
        ]

    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_language(self, obj):
        return obj.get_language_display()

    def get_currency(self, obj):
        return obj.get_currency_display()


class UserRegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = user_models.User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = user_models.User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        return user

    def validate(self, data):
        try:
            user = user_models.User.objects.filter(
                username=data.get('username'))
            if user.exists():
                raise serializers.ValidationError(
                    {'username': 'Username already exists.'})
        except user_models.User.DoesNotExist:
            pass

        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError({'password': 'Empty password.'})

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})

        return data
