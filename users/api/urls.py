from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views as user_views


urlpatterns = [
    path('registration/', user_views.UserRegistrationView.as_view(),
         name='user-registration'),
    path('login/', obtain_auth_token, name='user-login'),
    path('id/', user_views.UserIdView.as_view(), name='user-id'),
    path('<pk>/profile/', user_views.UserProfileView.as_view(), name='user-profile'),
]
