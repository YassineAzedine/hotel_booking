# rooms/models.py
from django.db import models
from hotels.models import Hotel

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    room_type = models.CharField(
           choices=[
        ("normal", 'normal'),
        ("double", 'double')
    ],
        
        max_length=100)  # Type of room (e.g., Single, Double, Suite)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    cover = models.ImageField(upload_to='room_cover/')
    max_occupancy = models.IntegerField()  # Max number of people
    available = models.IntegerField(
    choices=[
        (1, 'Available'),
        (0, 'Not Available')
    ],
    default=1
    )
   # List of amenities (e.g., Wi-Fi, TV, etc.)
    
    
    def __str__(self):
        return f'{self.room_type} - {self.hotel.name} - {self.price} , av'
class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f'Image for {self.room}'