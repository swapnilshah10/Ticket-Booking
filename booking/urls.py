from django.urls import path
from booking.views import ticket_list, make_booking, booking_confirmation
from . import views

urlpatterns = [
    path('', ticket_list, name='ticket_list'),
    # path('booking/<int:ticket_id>/', make_booking, name='make_booking'),
    path('booking/confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
    path('signup/', views.signup, name='signup'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('ticket/<int:ticket_id>/make_booking/', views.book_ticket, name='make_booking')
]
