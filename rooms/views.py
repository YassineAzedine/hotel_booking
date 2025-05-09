# rooms/views.py
from inspect import isawaitable
from django.shortcuts import render, get_object_or_404
from .models import Room, RoomImage
from hotels.models import Hotel

def room_list(request):
    filters = {
        'hotel': request.GET.get('hotel', ''),
        'type': request.GET.get('type', ''),
        'available': request.GET.get('available', ''),
        'max_price': request.GET.get('max_price', '')
    }
    print(f"Filters: {filters}")  # Affichage pour débogage

    rooms = Room.objects.all()

    # Filtrer par hôtel
    if filters['hotel']:
        rooms = rooms.filter(hotel_id=filters['hotel'])

    # Filtrer par type de chambre
    if filters['type']:
        rooms = rooms.filter(room_type=filters['type'])

    # Filtrer par disponibilité
    if filters['available']:
      
       rooms = rooms.filter(available=filters["available"])

    if filters['max_price']:
      rooms = rooms.filter(price__lte=filters['max_price'])

    hotels = Hotel.objects.all()  # Liste de tous les hôtels pour le filtre
    print(f"Rooms: {rooms}")  # Affichage pour débogage
    return render(request, 'rooms/room_list.html', {'rooms': rooms, 'hotels': hotels, 'filters': filters})
def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    images = RoomImage.objects.filter(room=room)

    # Affichage pour débogage
    print(f"Room: {room}")
    for img in images:
        print(f"Image: {img.image.url}")

    return render(request, 'rooms/room_detail.html', {
        'room': room,
        'images': images
    })
