from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from users import models as user_models
from . import serializers as user_serializers


class UserIdView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Reponse(request.user.id)


class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = user_serializers.UserRegisterSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user.'
            data['username'] = user.username
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['email'] = user.email
            token = Token.objects.get(user=user).key
            data['token'] = token

        else:
            data = serializer.errors

        return Response(data)


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = user_serializers.UserProfileSerializer

    def get_queryset(self):
        return user_models.User.objects.filter(id=self.request.user.id)

    def put(self, request, *args, **kwargs):
        user = user_models.User.objects.get(id=self.request.user.id)
        serializer = user_serializers.UserProfileSerializer(
            user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Profile update successed.'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
