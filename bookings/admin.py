from django.contrib import admin

from rooms.models import RoomImage
from .models import Booking

admin.site.register(Booking)
admin.site.register(RoomImage)