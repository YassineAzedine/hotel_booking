# bookings/models.py
from django.db import models
from rooms.models import Room
from django.contrib.auth.models import User

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    nights = models.PositiveIntegerField(default=0) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(
             choices=[
        ("pending", 'pending'),
        ("confirmed", 'Confirmed'),
        ("cancelled", 'cancelled'),

    ],
        max_length=20, default='pending')  # e.g., Pending, Confirmed, Cancelled
      # Automatically set the field to now when the object is first created


    def __str__(self):
        return f'{self.user.username} - {self.room} from {self.check_in} to {self.check_out}'
