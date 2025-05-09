# rooms/urls.py
from django.urls import path
from . import views

urlpatterns = [
      path('rooms/', views.room_list, name='room_list'),
    path('hotel/<int:hotel_id>/rooms/', views.room_list, name='room_list'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    
]
