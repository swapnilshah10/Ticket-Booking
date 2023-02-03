# booking/views.py
from django.shortcuts import render, redirect
from .models import Ticket, Booking
# booking/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm

@login_required
def my_tickets(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_tickets.html', {'tickets': bookings})

@login_required
def ticket_detail(request, ticket_id):
    ticket = Booking.objects.get(id = ticket_id)
    print(ticket)
    return render(request, 'booking/ticket_detail.html', {'ticket': ticket})

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

@login_required
def make_booking(request, ticket_id , quantity = 1):
    ticket = Ticket.objects.get(id=ticket_id)
    user = request.user
    booking = ticket.make_booking(user, quantity)
    return redirect('booking_confirmation', booking_id = booking.id)

@login_required
def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})


@login_required
def cancel_booking(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    booking = Booking.objects.get(ticket=ticket, user=request.user)
    ticket.cancel_booking(booking)
    return redirect('my_tickets')


@login_required
def book_ticket(request , ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = ticket.make_booking(user=request.user, ticket_quantity=form.cleaned_data['ticket_quantity'])
            if booking:
                return redirect('booking_confirmation', booking_id=booking.id)
            else:
                form.add_error(None, "Ticket not available.")
    else:
        form = BookingForm()
    return render(request, 'booking/book_ticket.html', {'ticket': ticket, 'form': form})

# @login_required
# def cancel_ticket(request , ticket_id , booking_id):
#     ticket = Ticket.objects.get(id=ticket_id)
#     if request.method == 'POST':
#             booking = Booking.objects.get(ticket=ticket, user=request.user , id = booking_id)
#             res = ticket.cancel_booking(user=request.user , booking)
#     return render(request, 'booking/book_ticket.html')

@login_required
def cancel_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        if booking.ticket.cancel_booking(booking):
            return redirect('my_tickets')
        else:
            return render(request, 'booking/error.html', {'message': 'Unable to cancel booking'})
    except Booking.DoesNotExist:
        return render(request, 'booking/error.html', {'message': 'Booking not found'})