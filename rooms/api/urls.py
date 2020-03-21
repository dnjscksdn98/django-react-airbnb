from django.urls import path
from . import views as room_views


urlpatterns = [
    path('', room_views.RoomView.as_view(), name='home'),
]
