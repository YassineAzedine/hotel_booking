from django.shortcuts import get_object_or_404, render
from .models import Hotel
from rooms.models import Room
def home(request):
    top_hotels = Hotel.objects.filter(rating__gte=4, rating__lte=5)[:5]
    print("Top Hotels:", top_hotels)  # Affichage pour débogage
    return render(request, 'hotels/home.html', {'hotels': top_hotels})
def hotel_list(request):
    hotels = Hotel.objects.all()
  
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})
def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = hotel.rooms.all()
        
    print("Rooms:" , rooms)
    for room in rooms:
        print(room.available , room.id , room.max_occupancy , room.price , room.room_type , room.description) 
  
    
    

    return render(request, 'hotels/hotel_detail.html',  {'hotel': hotel, 'rooms': rooms})