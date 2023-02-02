# booking/views.py
from django.shortcuts import render, redirect
from .models import Ticket, Booking
# booking/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def my_tickets(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_tickets.html', {'tickets': bookings})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'booking/ticket_list.html', {'tickets': tickets})

def make_booking(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    user = request.user
    booking = Booking.objects.create(ticket=ticket, ticket_quantity=1, user=user)
    return redirect('booking_confirmation', booking_id=booking.id)
 # type: ignore
def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})
