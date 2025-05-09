# rooms/urls.py
from django.urls import path
from . import views

urlpatterns = [
      path('room/<int:room_id>/', views.book_room, name='book_room'),   
      path('booking/confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
      path('booking/list/', views.booking_list, name='booking_list'),

]
