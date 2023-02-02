# booking/admin.py
from django.contrib import admin
from .models import Ticket, Booking

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description','user', 'date_created', 'size')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'date_booked', 'ticket_quantity', 'user')
