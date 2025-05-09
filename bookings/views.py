from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from rooms.models import Room
from .forms import BookingForm
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)  # Retrieve the room based on the room_id provided

    if request.method == 'POST':  # Check if the form has been submitted
        form = BookingForm(request.POST)  # Instantiate the form with POST data
        
        if form.is_valid():  # Check if the form data is valid
            check_in_date = form.cleaned_data['check_in']  # Extract the cleaned data for check-in date
            check_out_date = form.cleaned_data['check_out']  # Extract the cleaned data for check-out date
            guests = form.cleaned_data['guests']  # Extract the cleaned data for number of guests

            # Calculate the number of nights between check-in and check-out dates
            nights = (check_out_date - check_in_date).days
            print(f"Nombre de nuits : {nights}")

            if nights <= 0:
                # If the number of nights is 0 or negative, return an error (e.g., show a message)
                form.add_error(None, "La date de départ doit être après la date d'arrivée.")
                return render(request, 'bookings/book_room.html', {'form': form, 'room': room})

            # Calculate the total price based on the number of nights and the room price per night
            total_price = nights * room.price

            # If the user is authenticated, use the logged-in user, otherwise use a guest user
            if request.user.is_authenticated:
                user = request.user
            else:
                # Create a guest user if not authenticated
                user, created = User.objects.get_or_create(username='guest_' + str(room_id))  # Create a unique guest username
                if created:
                    user.first_name = "Anonyme"  # Default name for guest user
                    user.save()

            # Create the booking object
            booking = Booking.objects.create(
                room=room,
                user=user,
                check_in=check_in_date,
                check_out=check_out_date,
                guests=guests,
                nights=nights,
                total_price=total_price,  # Assuming you have a 'total_price' field in the Booking model
            )
            # 👉 Marquer la chambre comme non disponible
            room.available = False
            room.save()


            # Log the booking details for debugging purposes (can be removed in production)
            print(f"✅ Réservation créée : {booking} pour {nights} nuit(s), {total_price}€")

            # Redirect the user to the booking confirmation page
            return redirect('booking_confirmation', booking_id=booking.id)

    else:
        form = BookingForm()  # Create an empty form if the request method is GET

    return render(request, 'bookings/book_room.html', {
        'room': room,  # Pass the room details to the template
        'form': form,  # Pass the form to the template
    })
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})