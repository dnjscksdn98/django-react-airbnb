from django.urls import path
from rooms.api import views as room_views


urlpatterns = [
    path('rooms/', room_views.RoomView.as_view(), name='rooms'),
]
